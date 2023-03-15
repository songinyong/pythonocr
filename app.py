# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 18:50:06 2023

@author: ttyy4
"""
from flask import Flask, request, jsonify, render_template
import pytesseract
from PIL import Image

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/ocr', methods=['POST'])
def ocr():
    if 'image' not in request.files:
        return jsonify({"error": "No image provided"}), 400

    image = Image.open(request.files['image'].stream)
    text = pytesseract.image_to_string(image)

    return jsonify({"text": text})

if __name__ == '__main__':
    app.run(debug=True)
