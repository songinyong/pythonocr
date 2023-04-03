# Use the official Python base image
FROM python:3.9-slim

# Install Tesseract and other dependencies
RUN apt-get update && apt-get install -y tesseract-ocr libtesseract-dev libleptonica-dev wget && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Download and install Tesseract's math-trained data
RUN wget https://github.com/tesseract-ocr/tessdata/raw/main/equ.traineddata -P /usr/share/tesseract-ocr/4.00/tessdata/

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the default Flask port
EXPOSE 5000

# Set environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Start the Flask app
CMD ["flask", "run"]
