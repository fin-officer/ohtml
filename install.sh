#!/bin/bash

echo "🚀 PDF Extraction Services - Instalator"
echo "========================================"

# Sprawdzenie czy Docker jest zainstalowany
if ! command -v docker &> /dev/null; then
    echo "❌ Docker nie jest zainstalowany. Instaluję..."
    curl -fsSL https://get.docker.com -o get-docker.sh
    sh get-docker.sh
    sudo usermod -aG docker $USER
    echo "✅ Docker zainstalowany. Wyloguj się i zaloguj ponownie."
    exit 1
fi

# Sprawdzenie czy Docker Compose jest zainstalowany
if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose nie jest zainstalowany. Instaluję..."
    sudo curl -L "https://github.com/docker/compose/releases/download/v2.20.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose
fi

echo "📦 Tworzenie folderów..."
mkdir -p shared/{models,utils,sdk/{python,js}}
mkdir -p services/{01-invoice-extractor,02-receipt-analyzer,03-cv-parser,04-contract-analyzer,05-financial-statement,06-medical-records,07-legal-documents,08-tax-forms,09-insurance-claims,10-educational-transcripts}
mkdir -p gateway/config
mkdir -p monitoring/{prometheus,grafana}

echo "🔧 Generowanie konfiguracji..."

# Tworzenie requirements.txt dla każdej usługi
for i in {01..10}; do
    case $i in
        01) service="invoice-extractor" ;;
        02) service="receipt-analyzer" ;;
        03) service="cv-parser" ;;
        04) service="contract-analyzer" ;;
        05) service="financial-statement" ;;
        06) service="medical-records" ;;
        07) service="legal-documents" ;;
        08) service="tax-forms" ;;
        09) service="insurance-claims" ;;
        10) service="educational-transcripts" ;;
    esac
    
    cat > services/${i}-${service}/requirements.txt << EOF
fastapi==0.104.1
uvicorn==0.24.0
python-multipart==0.0.6
pdf2image==1.16.3
pytesseract==0.3.10
opencv-python==4.8.1.78
pillow==10.1.0
numpy==1.24.3
redis==5.0.1
pydantic==2.5.0
transformers==4.36.0
torch==2.1.0
torchvision==0.16.0
spacy==3.7.2
scikit-learn==1.3.2
pandas==2.1.4
requests==2.31.0
aiofiles==0.24.0
langdetect==1.0.9
EOF
done

echo "🐳 Tworzenie Dockerfile dla każdej usługi..."

# Generowanie Dockerfile dla każdej usługi
for i in {01..10}; do
    case $i in
        01) service="invoice-extractor" ;;
        02) service="receipt-analyzer" ;;
        03) service="cv-parser" ;;
        04) service="contract-analyzer" ;;
        05) service="financial-statement" ;;
        06) service="medical-records" ;;
        07) service="legal-documents" ;;
        08) service="tax-forms" ;;
        09) service="insurance-claims" ;;
        10) service="educational-transcripts" ;;
    esac
    
    cat > services/${i}-${service}/Dockerfile << EOF
FROM python:3.11-slim

# Instalacja zależności systemowych
RUN apt-get update && apt-get install -y \\
    tesseract-ocr \\
    tesseract-ocr-pol \\
    tesseract-ocr-eng \\
    tesseract-ocr-deu \\
    libglib2.0-0 \\
    libsm6 \\
    libxext6 \\
    libxrender-dev \\
    libgomp1 \\
    libgl1-mesa-glx \\
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Kopiowanie requirements i instalacja
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kopiowanie kodu aplikacji
COPY . .

# Tworzenie folderów
RUN mkdir -p /app/models /app/temp /app/output

EXPOSE 80${i}

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80${i}"]
EOF
done

echo "🔨 Budowanie obrazów Docker..."
docker-compose build

echo "🏃 Uruchamianie usług..."
docker-compose up -d

echo "🔍 Sprawdzanie statusu usług..."
sleep 10
docker-compose ps

echo "✅ Instalacja zakończona!"
echo ""
echo "📊 Dashboard dostępny na: http://localhost:8000"
echo "🔧 Poszczególne usługi:"
echo "   • Invoice Extractor: http://localhost:8001"
echo "   • Receipt Analyzer: http://localhost:8002"
echo "   • CV Parser: http://localhost:8003"
echo "   • Contract Analyzer: http://localhost:8004"
echo "   • Financial Statement: http://localhost:8005"
echo "   • Medical Records: http://localhost:8006"
echo "   • Legal Documents: http://localhost:8007"
echo "   • Tax Forms: http://localhost:8008"
echo "   • Insurance Claims: http://localhost:8009"
echo "   • Educational Transcripts: http://localhost:8010"
echo ""
echo "📚 Dokumentacja API: http://localhost:8000/docs"
echo "🖥️ Monitoring: http://localhost:3000 (Grafana)"
echo ""
echo "🚀 Przykład użycia SDK:"
echo "python -c \"from shared.sdk.python import PDFClient; client = PDFClient('http://localhost:8000'); print(client.extract_invoice('faktura.pdf'))\""
