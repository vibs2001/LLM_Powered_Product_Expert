from flask import Flask, request, render_template
import torch
import os
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.llms.huggingface import HuggingFaceLLM
from llama_index.core.prompts.prompts import SimpleInputPrompt
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from llama_index.embeddings.langchain import LangchainEmbedding
import pdfplumber
import fitz
import pytesseract
from PIL import Image
import sys
import camelot
from paddleocr import PaddleOCR
from huggingface_hub import login
from llama_index.core import Document
import mimetypes
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import json
import markdown
import re
from pathlib import Path

def convert_pdf_to_markdown(pdf_path):
    """Convert PDF to Markdown format while preserving structure."""
    markdown_content = []
    
    # Open PDF with PyMuPDF
    doc = fitz.open(pdf_path)
    
    for page_num in range(len(doc)):
        page = doc[page_num]
        
        # Extract text with formatting
        blocks = page.get_text("dict")["blocks"]
        
        for block in blocks:
            if "lines" in block:
                for line in block["lines"]:
                    for span in line["spans"]:
                        text = span["text"]
                        size = span["size"]
                        flags = span["flags"]
                        
                        # Convert formatting to Markdown
                        if size > 20:  # Likely a heading
                            text = f"# {text}"
                        elif size > 15:
                            text = f"## {text}"
                        elif flags & 2**4:  # Bold text
                            text = f"**{text}**"
                        elif flags & 2**1:  # Italic text
                            text = f"*{text}*"
                            
                        markdown_content.append(text)
                
                markdown_content.append("\n")  # Add line break between blocks
    
    # Extract tables using camelot
    tables = camelot.read_pdf(pdf_path)
    if len(tables) > 0:
        markdown_content.append("\n## Tables\n")
        for i, table in enumerate(tables):
            markdown_content.append(f"\nTable {i+1}:\n")
            markdown_content.append(table.df.to_markdown())
            markdown_content.append("\n")
    
    doc.close()
    return "\n".join(markdown_content)

def process_directory(input_dir, output_dir):
    """Process all PDFs in directory and convert to Markdown."""
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    for filename in os.listdir(input_dir):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(input_dir, filename)
            markdown_content = convert_pdf_to_markdown(pdf_path)
            
            # Save as Markdown file
            markdown_path = os.path.join(output_dir, filename.replace('.pdf', '.md'))
            with open(markdown_path, 'w', encoding='utf-8') as f:
                f.write(markdown_content)

def load_documents_and_metadata(directory):
    """Load documents and metadata, now supporting Markdown files."""
    # First convert any PDFs to Markdown
    markdown_dir = os.path.join(directory, 'markdown')
    process_directory(directory, markdown_dir)
    
    # Load all documents including newly created Markdown files
    documents = SimpleDirectoryReader(markdown_dir).load_data()
    
    # Load metadata
    metadata = {}
    for filename in os.listdir(directory):
        if filename.endswith("_metadata.json"):
            with open(os.path.join(directory, filename), 'r') as f:
                metadata[filename] = json.load(f)
    
    return documents, metadata

def save_metadata(metadata, output_file):
    with open(output_file, 'w') as f:
        json.dump(metadata, f, indent=4)

# Main execution
data_directory = "/home/rptech_server/llm_env/Product_RAG/data"
metadata_output_file = "/home/rptech_server/llm_env/Product_RAG/metadata_output.json"

# System prompt and model setup
system_prompt = """
You are an advanced technical assistant specializing in answering questions based on provided documents and structured data. Your goal is to respond accurately and concisely, referencing specific details from structured Q&A files and additional technical documentation if needed.
Use the structured Q&A file as your primary source. Refer to the datasheet to supplement responses only when extra details are required for precision. Avoid assumptions beyond the data provided, and answer questions with clarity and relevance to the technical content.
If a question seems ambiguous, request clarification. Each response should focus on delivering clear, specific information to address the user's question accurately.
"""

query_wrapper_prompt = SimpleInputPrompt("<|USER|>{query_str}<|ASSISTANT|>")

# Load and process documents
documents, metadata = load_documents_and_metadata(data_directory)

# Llama2 Model Setup
llm = HuggingFaceLLM(
    context_window=4096,
    max_new_tokens=256,
    generate_kwargs={"temperature": 0.1, "do_sample": False},
    system_prompt=system_prompt,
    query_wrapper_prompt=query_wrapper_prompt,
    tokenizer_name="meta-llama/Llama-2-7b-chat-hf",
    model_name="meta-llama/Llama-2-7b-chat-hf",
    device_map="auto",
    model_kwargs={"torch_dtype": torch.float16, "load_in_4bit": True}
)

# Embedding Model Setup
embed_model = LangchainEmbedding(HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2"))

# Update recursion limit
sys.setrecursionlimit(3000)

# Create and save index
index = VectorStoreIndex.from_documents(
    documents,
    llm=llm,
    embed_model=embed_model,
    chunk_size=1000
)

# Save the index
index.storage_context.persist(persist_dir='/home/rptech_server/llm_env/Product_RAG/index_directory/Jetson_AGX_Orin')
