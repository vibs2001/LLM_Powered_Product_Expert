from flask import Flask, request, render_template, Response, stream_with_context, redirect, url_for
import torch
import os
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage
from langchain_huggingface import HuggingFaceEmbeddings
from llama_index.embeddings.langchain import LangchainEmbedding
import sys
import json
import re
from langchain_ollama import ChatOllama
from gtts import gTTS
import io
from llama_index.llms.ollama import Ollama
from flask import jsonify
import speech_recognition as sr

app = Flask(__name__)

r = sr.Recognizer()

if torch.cuda.is_available():
    print(f"CUDA is available. using GPU: {torch.cuda.get_device_name(0)}")
else:
    print("CUDA is not available")

model_name = "deepseek-llm:latest"
system_prompt = "You are an advanced technical assistant specializing in answering questions based on provided documents and structured data. Your goal is to respond accurately and concisely, referencing specific details from the documents provided. If you don't know the answer, say so!, DO NOT HALLUCINATE."

llm = Ollama(model=model_name, temperature=0.7, system_prompt=system_prompt)
embed_model = LangchainEmbedding(
    HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
)

index_directory = "index_directory"

# Define available products
PRODUCTS = {
    "Holtek_Ceiling_fan": "Holtek_Ceiling_fan",
    "product2": "Holtek_Ceiling_fan"
}

def load_product_index(product_name):
    """Load the index for a specific product"""
    product_index_path = os.path.join(index_directory, f"{product_name}_index")
    if os.path.exists(product_index_path):
        storage_context = StorageContext.from_defaults(persist_dir=product_index_path)
        return load_index_from_storage(storage_context, embed_model=embed_model)
    return None

def text_to_speech(text):
    tts = gTTS(text=text, lang='en')
    mp3_fp = io.BytesIO()
    tts.write_to_fp(mp3_fp)
    mp3_fp.seek(0)
    return mp3_fp

@app.route('/')
def product_selection():
    """Landing page with product selection"""
    return render_template('product_selection.html', products=PRODUCTS)

@app.route('/qa/<product_name>', methods=['GET', 'POST'])
def qa_page(product_name):
    """QA page for specific product"""
    if product_name not in PRODUCTS:
        return redirect(url_for('product_selection'))
    
    if request.method == 'POST':
        query = request.form['query']
        response_format = request.form.get('format', 'text')
        
        index = load_product_index(product_name)
        
        if index:
            query_engine = index.as_query_engine(llm=llm, streaming=True, similarity_top_k=3)
            
            if response_format == 'audio':
                response_text = ""
                for chunk in query_engine.query(query).response_gen:
                    response_text += chunk
                
                audio_fp = text_to_speech(response_text)
                return Response(
                    audio_fp.read(),
                    mimetype='audio/mpeg'
                )
            else:
                def generate_response():
                    response = query_engine.query(query)
                    for chunk in response.response_gen:
                        yield chunk
                
                return Response(
                    stream_with_context(generate_response()),
                    content_type='text/plain'
                )
        else:
            error_message = f"No index found for product '{product_name}'"
            return Response(error_message, content_type='text/plain')
    
    return render_template('qa_page.html', product_name=PRODUCTS[product_name])

@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    if 'audio' not in request.files:
        return jsonify({'error': 'No audio file received'}), 400
    
    audio_file = request.files['audio']
    with sr.AudioFile(audio_file) as source:
        audio_data = r.record(source)
        try:
            text = r.recognize_google(audio_data)
            return jsonify({'text': text})
        except sr.UnknownValueError:
            return jsonify({'error': 'Could not understand audio'}), 400
        except sr.RequestError:
            return jsonify({'error': 'Speech service down'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000, ssl_context=("/home/rptech_server/cert.pem", "/home/rptech_server/key.pem"))