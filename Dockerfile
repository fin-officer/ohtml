FROM python:3.9-slim

# Instalacja systemowych zależności
RUN apt-get update && apt-get install -y \
    tesseract-ocr tesseract-ocr-pol tesseract-ocr-deu \
    poppler-utils \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

# Kopiowanie aplikacji
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src/ ./src/
EXPOSE 8000

CMD ["python", "src/pdf_analyzer.py"]