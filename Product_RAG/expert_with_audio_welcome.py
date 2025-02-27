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
import tempfile
import pydub
from pydub import AudioSegment

app = Flask(__name__)

r = sr.Recognizer()

if torch.cuda.is_available():
    print(f"CUDA is available. using GPU: {torch.cuda.get_device_name(0)}")
else:
    print("CUDA is not available")

model_name = "deepseek-llm:latest"
system_prompt = "You are an advanced technical assistant specializing in answering questions based on provided documents and structured data in a concise manner. Your goal is to respond accurately and concisely, referencing specific details from the documents provided. If you don't know the answer, say so!, DO NOT HALLUCINATE."

llm = Ollama(model=model_name, temperature=0.7, system_prompt=system_prompt, max_tokens=100)
embed_model = LangchainEmbedding(
    HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
)

index_directory = "index_directory"

# Define available products
PRODUCTS = {
    "Holtek_Ceiling_fan_Controller": "Holtek_Ceiling_fan_Controller",
    "Jetson_AGX_Orin": "Jetson_AGX_Orin"
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
@app.route('/welcome-audio/<product_name>')
def welcome_audio(product_name):

    if product_name == "Holtek_Ceiling_fan_Controller":
        display_name = product_name.replace('_', ' ')
        welcome_text = f"Welcome to the {display_name} product assistant, Introducing the Holtek powered smart ceiling fan! Smooth, silent and efficient, it features sensorless FOC control, six speeds, and forward/reverse. Enjoy precise control with the RG remote. Built-in Safety features include over-voltage, over-current, and locked-rotor protection, if you need any more info on the HT32F65532G, please ask you query below."
    elif product_name == "Jetson_AGX_Orin":
        display_name = product_name.replace('_',' ')
        welcome_text = f"Welcome to the {display_name} product assistant, Introducing Jetson AGX Orin, where high capacity memory meets breakthrough AI performance. Experience unprecedented computing power designed for advanced robotics, automotive, and edge applications, empower your innovations with intelligence at scale. If you want anymore info on the Jetson AGX Orin, please ask you query below. "
    audio_fp = text_to_speech(welcome_text)
    return Response(
        audio_fp.read(),
        mimetype='audio/mpeg'
    )
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
    #html_name = product_name.replace(' ','_')
    return render_template(f'{product_name}.html', product_name=PRODUCTS[product_name])

@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    if 'audio' not in request.files:
        return jsonify({'error': 'No audio file received'}), 400
    
    audio_file = request.files['audio']
    
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Save the original file
        orig_filename = os.path.join(temp_dir, "original_audio")
        audio_file.save(orig_filename)
        
        # Convert to WAV using pydub - this can handle many formats
        try:
            # Try to determine the format from content
            audio = AudioSegment.from_file(orig_filename)
            wav_filename = os.path.join(temp_dir, "converted_audio.wav")
            audio.export(wav_filename, format="wav")
            
            with sr.AudioFile(wav_filename) as source:
                # Adjust for ambient noise
                r.adjust_for_ambient_noise(source)
                # Record audio
                audio_data = r.record(source)
                
                try:
                    # Use recognize_google
                    text = r.recognize_google(audio_data, language="en-US")
                    return jsonify({'text': text, 'status': 'success'})
                except sr.UnknownValueError:
                    return jsonify({'error': 'Could not understand audio', 'status': 'speech_not_recognized'}), 400
                except sr.RequestError as e:
                    return jsonify({'error': f'Speech service error: {str(e)}', 'status': 'service_error'}), 500
        except Exception as e:
            return jsonify({'error': f'Processing error: {str(e)}', 'status': 'processing_error'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001, ssl_context=("/home/rptech_server/cert.pem", "/home/rptech_server/key.pem"))
    