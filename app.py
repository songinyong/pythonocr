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
    custom_config = r"--psm 11 --oem 3 -c tessedit_char_whitelist=0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+-=*/^_(),.[]{}<>!@#$%&\'\"':;|\\? -l equ+eng"



    text = pytesseract.image_to_string(image, config=custom_config)

    return jsonify({"text": text})

if __name__ == '__main__':
    app.run(debug=True)
