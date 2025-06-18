# vHTML - Optical HTML Generator

vHTML (Optic HyperText Markup Language) to system do automatycznej konwersji dokumentów do postaci HTML z wykorzystaniem technik optycznego rozpoznawania znaków (OCR) i analizy układu dokumentu.

## 🌟 Funkcje

- Automatyczna analiza układu dokumentu
- Wsparcie dla wielojęzycznego OCR (PL, EN, DE)
- Generowanie struktury HTML z metadanymi
- Obsługa dokumentów PDF i obrazów
- Prosta integracja z istniejącymi systemami



# System Analizy i Konwersji PDF do HTML z OCR

## 1. Architektura Systemu

### Główne Komponenty:
- **PDF Processor** - przetwarzanie PDF do obrazów
- **Layout Analyzer** - analiza układu i segmentacja bloków
- **OCR Engine** - rozpoznawanie tekstu w blokach
- **Language Detector** - rozpoznawanie języka i formatu
- **HTML Generator** - generowanie struktury HTML z metadanymi
- **Template Engine** - różne szablony dla typów dokumentów

## 2. Technologie i Biblioteki

### Główne Biblioteki:
- **OpenCV** - przetwarzanie obrazów i segmentacja
- **Tesseract/EasyOCR** - OCR
- **pdf2image** - konwersja PDF do obrazów
- **langdetect** - rozpoznawanie języka
- **Jinja2** - templating HTML
- **scikit-image** - dodatkowe operacje na obrazach

### Dodatkowe Narzędzia:
- **PyMuPDF (fitz)** - alternatywne przetwarzanie PDF
- **layoutparser** - gotowe modele do analizy layoutu
- **spaCy** - analiza tekstu i NER
- **Pillow** - manipulacja obrazami

## 3. Workflow Systemu

### Krok 1: Preprocessing PDF
```
PDF → Strony jako obrazy → Preprocessing (denoise, deskew) → Analiza layoutu
```

### Krok 2: Segmentacja Bloków
```
Obraz → Wykrywanie bloków tekstu → Klasyfikacja bloków → Hierarchia bloków
```

### Krok 3: OCR i Analiza
```
Blok → OCR → Rozpoznanie języka → Analiza formatowania → Metadane
```

### Krok 4: Generowanie HTML
```
Struktura bloków + Tekst + Metadane → HTML Template → Finalne HTML
```

## 4. Typy Dokumentów i Szablony

### Szablon Faktury (4 bloki):
- **Blok A** (lewy górny) - dane nadawcy
- **Blok B** (prawy górny) - dane odbiorcy  
- **Blok C** (środkowy) - tabela pozycji
- **Blok D** (dolny) - podsumowanie płatności

### Szablon 6-kolumnowy (6 bloków):
- **Bloki A,B** (górny rząd)
- **Bloki C,D** (środkowy rząd)
- **Bloki E,F** (dolny rząd)

### Szablon Uniwersalny:
- Automatyczne wykrywanie liczby bloków
- Adaptacyjna segmentacja

## 5. Struktura JSON Metadanych

```json
{
  "document": {
    "type": "invoice|form|letter|other",
    "language": "pl|en|de",
    "layout": "4-block|6-block|custom",
    "confidence": 0.95
  },
  "blocks": [
    {
      "id": "A",
      "type": "header|content|table|footer",
      "position": {"x": 0, "y": 0, "width": 300, "height": 200},
      "content": "rozpoznany tekst",
      "language": "pl",
      "confidence": 0.92,
      "formatting": {
        "bold": [0, 10],
        "tables": [],
        "lists": []
      }
    }
  ]
}
```

## 6. Plan Implementacji

### Faza 1: Podstawowa Segmentacja
1. ✅ Konwersja PDF do obrazów
2. ✅ Podstawowa segmentacja bloków OpenCV
3. ✅ Prosty OCR z Tesseract
4. ✅ Generowanie podstawowego HTML

### Faza 2: Inteligentna Analiza
1. 🔄 Klasyfikacja typów dokumentów
2. 🔄 Rozpoznawanie języka
3. 🔄 Analiza formatowania tekstu
4. 🔄 Szablon-specyficzne przetwarzanie

### Faza 3: Zaawansowane Funkcje
1. ⏳ Machine Learning dla klasyfikacji bloków
2. ⏳ Adaptacyjne szablony
3. ⏳ Batch processing
4. ⏳ API REST

### Faza 4: Optymalizacja
1. ⏳ Caching rezultatów
2. ⏳ Parallel processing
3. ⏳ UI dla konfiguracji
4. ⏳ Eksport do różnych formatów

## 7. Gotowe Rozwiązania do Wykorzystania

### Layout Analysis:
- **LayoutParser** - pretrenowane modele
- **PaddleOCR** - integrowane layout + OCR
- **Document AI** modele z Hugging Face

### OCR Engines:
- **Tesseract** + **pytesseract**
- **EasyOCR** 
- **TrOCR** (Transformer-based)

### Preprocessing:
- **OpenCV** kontury i segmentacja
- **scikit-image** filtering
- **Pillow** podstawowe operacje

## 8. Struktura Projektu

```
pdf_analyzer/
├── src/
│   ├── core/
│   │   ├── pdf_processor.py
│   │   ├── layout_analyzer.py
│   │   ├── ocr_engine.py
│   │   └── html_generator.py
│   ├── templates/
│   │   ├── invoice_template.html
│   │   ├── form_template.html
│   │   └── universal_template.html
│   ├── models/
│   │   └── document_classifier.py
│   └── utils/
│       ├── image_utils.py
│       └── text_utils.py
├── tests/
├── examples/
├── requirements.txt
└── main.py
```

## 9. Kryteria Sukcesu

- ✅ Dokładność segmentacji > 90%
- ✅ Dokładność OCR > 95% 
- ✅ Zachowanie formatowania oryginalnego
- ✅ Responsywny HTML output
- ✅ Metadane JSON dla każdego bloku
- ✅ Wsparcie dla języków PL/EN/DE
- ✅ Modularna architektura
- ✅ Możliwość dodawania nowych typów dokumentów

## 🚀 Szybki start

### Wymagania wstępne

- Python 3.8+
- Tesseract OCR
- Poppler (do przetwarzania PDF)

### Instalacja

1. Sklonuj repozytorium:
   ```bash
   git clone https://github.com/yourusername/vhtml.git
   cd vhtml
   ```

2. Uruchom skrypt instalacyjny:
   ```bash
   make setup
   ```
   
   Lub ręcznie:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/macOS
   # lub venv\Scripts\activate  # Windows
   pip install -r requirements.txt
   ```

3. Zainstaluj zależności systemowe (Linux/macOS):
   ```bash
   chmod +x scripts/install_dependencies.sh
   ./scripts/install_dependencies.sh
   ```

### Użycie

```python
from vhtml import process_document

# Przetwarzanie pliku PDF
result = process_document("dokument.pdf", output_format="html")

# Zapis wyników
with open("wynik.html", "w", encoding="utf-8") as f:
    f.write(result)
```

## 📦 Instalacja zaawansowana

Zobacz [INSTALLATION.md](docs/INSTALLATION.md) aby uzyskać szczegółowe instrukcje instalacji dla różnych systemów operacyjnych.

## 📚 Dokumentacja

Pełna dokumentacja dostępna jest w katalogu [docs/](docs/).

## 🤝 Wsparcie

Masz pytania lub problemy? Sprawdź [FAQ](docs/FAQ.md) lub zgłoś problem w zakładce Issues.

## 📄 Licencja

Ten projekt jest dostępny na licencji MIT. Zobacz plik [LICENSE](LICENSE) aby uzyskać więcej informacji.

print("✅ OpenCV:", cv2.__version__)
print("✅ Tesseract:", pytesseract.get_tesseract_version())
print("✅ PDF2Image: OK")
print("✅ Instalacja kompletna!")

# Test OCR
test_img = Image.new('RGB', (200, 50), color='white')
from PIL import ImageDraw, ImageFont
draw = ImageDraw.Draw(test_img)
draw.text((10, 10), "Test OCR", fill='black')
text = pytesseract.image_to_string(test_img, lang='eng')
print("✅ OCR Test:", text.strip())
```

## 🚀 Pierwsze Uruchomienie

### Struktura Katalogów:
```
pdf_analyzer_project/
├── pdf_analyzer_env/          # Środowisko wirtualne
├── src/
│   ├── pdf_analyzer.py        # Główny kod systemu
│   ├── usage_examples.py      # Przykłady użycia
│   └── requirements.txt       # Zależności
├── input/                     # Katalog na PDF do analizy
├── output/                    # Katalog na wyniki
└── tests/                     # Pliki testowe
```

### Test Podstawowy:
[241002.pdf](invoices/241002.pdf)
```bash
# Uruchom analizę
python src/pdf_analyzer.py invoice/241002.pdf

# Sprawdź wyniki w katalogu output/
ls -la output/
```

## ⚙️ Konfiguracja i Dostrajanie

### Parametry OCR (w pdf_analyzer.py):

```python
# Dla lepszej jakości OCR
custom_config = r'--oem 3 --psm 6 -l pol+eng+deu -c tessedit_char_whitelist=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzĄĆĘŁŃÓŚŹŻąćęłńóśźż'

# Dla dokumentów z małym tekstem
custom_config = r'--oem 3 --psm 6 -l pol+eng+deu -c tessedit_char_whitelist=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzĄĆĘŁŃÓŚŹŻ'




# 📋 Przewodnik Instalacji i Konfiguracji PDF Analyzer

## 🎯 Przegląd Systemu

PDF Analyzer to modularny system do inteligentnej analizy dokumentów PDF z automatyczną segmentacją na bloki tekstu, OCR i generowaniem struktury HTML z metadanymi JSON. System wykorzystuje OpenCV do analizy układu, Tesseract/EasyOCR do rozpoznawania tekstu i generuje responsywne HTML z osadzonymi metadanymi.

## 🛠️ Wymagania Systemowe

### Obsługiwane Systemy:
- **Linux** (Ubuntu 18.04+, Debian 10+, CentOS 7+)
- **Windows** (10/11)
- **macOS** (10.14+)

### Wymagania Sprzętowe:
- **RAM**: minimum 4GB, zalecane 8GB+
- **CPU**: 2+ rdzenie
- **Miejsce na dysku**: 2GB dla instalacji + miejsce na dokumenty
- **GPU**: opcjonalnie dla przyspieszenia OCR

## 📦 Instalacja Krok po Kroku

### Krok 1: Przygotowanie Środowiska

```bash
# Utwórz katalog projektu
mkdir pdf_analyzer_project
cd pdf_analyzer_project

# Utwórz środowisko wirtualne Python
python3 -m venv pdf_analyzer_env

# Aktywuj środowisko wirtualne
# Linux/macOS:
source pdf_analyzer_env/bin/activate
# Windows:
pdf_analyzer_env\Scripts\activate
```

### Krok 2: Instalacja Tesseract OCR

#### Ubuntu/Debian:
```bash
sudo apt-get update
sudo apt-get install tesseract-ocr tesseract-ocr-pol tesseract-ocr-deu tesseract-ocr-eng
sudo apt-get install libtesseract-dev libleptonica-dev
```

#### Windows:
1. Pobierz installer z: https://github.com/UB-Mannheim/tesseract/wiki
2. Zainstaluj z obsługą języków polskiego, niemieckiego i angielskiego
3. Dodaj ścieżkę Tesseract do PATH (np. `C:\Program Files\Tesseract-OCR`)

#### macOS:
```bash
brew install tesseract tesseract-lang
```

### Krok 3: Instalacja Poppler (dla pdf2image)

#### Ubuntu/Debian:
```bash
sudo apt-get install poppler-utils
```

#### Windows:
1. Pobierz Poppler z: https://github.com/oschwartz10612/poppler-windows/releases
2. Rozpakuj i dodaj `bin` do PATH

#### macOS:
```bash
brew install poppler
```

### Krok 4: Instalacja Bibliotek Python

```bash
# Utwórz requirements.txt (skopiuj z artefaktu)
pip install --upgrade pip
pip install -r requirements.txt
```

### Krok 5: Sprawdzenie Instalacji

```python
# test_installation.py
import cv2
import pytesseract
from pdf2image import convert_from_path
import numpy as np
from PIL import Image
import langdetect

print("✅ OpenCV:", cv2.__version__)
print("✅ Tesseract:", pytesseract.get_tesseract_version())
print("✅ PDF2Image: OK")
print("✅ Instalacja kompletna!")

# Test OCR
test_img = Image.new('RGB', (200, 50), color='white')
from PIL import ImageDraw, ImageFont
draw = ImageDraw.Draw(test_img)
draw.text((10, 10), "Test OCR", fill='black')
text = pytesseract.image_to_string(test_img, lang='eng')
print("✅ OCR Test:", text.strip())
```

## 🚀 Pierwsze Uruchomienie

### Parametry OCR (w pdf_analyzer.py):

```python
# Dla lepszej jakości OCR
custom_config = r'--oem 3 --psm 6 -l pol+eng+deu -c tessedit_char_whitelist=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzĄĆĘŁŃÓŚŹŻąćęłńóśźż'

# Dla dokumentów z małym tekstem
custom_config = r'--oem 3 --psm 8 -l pol+eng+deu'

# Dla dokumentów z tabelami
custom_config = r'--oem 3 --psm 4 -l pol+eng+deu'
```

### Parametry Segmentacji OpenCV:

```python
class LayoutAnalyzer:
    def __init__(self):
        # Dostrajalne parametry
        self.min_contour_area = 1000      # Minimalna powierzchnia bloku
        self.morph_kernel_size = (50, 10) # Rozmiar kernela morfologii
        self.dilate_iterations = 2        # Iteracje dylatacji
        self.blur_kernel = (5, 5)         # Rozmiar kernela rozmycia
```

### Konfiguracja dla Różnych Typów Dokumentów:

```python
# Faktury - dokładna segmentacja
INVOICE_CONFIG = {
    'min_contour_area': 2000,
    'morph_kernel': (30, 15),
    'expected_blocks': 4
}

# Formularze - liberalna segmentacja
FORM_CONFIG = {
    'min_contour_area': 500,
    'morph_kernel': (20, 8),
    'expected_blocks': 6
}
```

### Test Manualny:
```bash
# Test z różnymi typami dokumentów
python src/pdf_analyzer.py tests/faktury/faktura1.pdf
python src/pdf_analyzer.py tests/formularze/formularz1.pdf
python src/pdf_analyzer.py tests/listy/list1.pdf
```

## 🔧 Rozwiązywanie Problemów

### Problem: "Tesseract not found"
```bash
# Linux
which tesseract
export PATH=$PATH:/usr/bin/tesseract

# Windows - dodaj do PATH:
C:\Program Files\Tesseract-OCR
```

### Problem: "pdf2image conversion failed"
```bash
# Sprawdź poppler
which pdftoppm

# Linux - reinstalacja
sudo apt-get install --reinstall poppler-utils
```

### Problem: Niska jakość OCR
1. **Zwiększ DPI**: `PDFProcessor(dpi=600)`
2. **Preprocessing obrazu**: Dodaj filtry denoise
3. **Dostrajanie parametrów Tesseract**:
   ```python
   # Dla skanowanych dokumentów
   custom_config = r'--oem 1 --psm 3 -l pol'
   
   # Dla cyfrowych PDF
   custom_config = r'--oem 3 --psm 6 -l pol+eng'
   ```

### Problem: Błędna segmentacja bloków
```python
# Dostraj parametry w LayoutAnalyzer
self.min_contour_area = 500      # Zmniejsz dla małych bloków
self.morph_kernel_size = (100, 20)  # Zwiększ dla łączenia bloków
```

## 📊 Monitoring i Optymalizacja

### Logowanie Diagnostyczne:
```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('pdf_analyzer.log'),
        logging.StreamHandler()
    ]
)
```

### Monitoring Wydajności:
```python
import time
from functools import wraps

def timing_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} zajęło: {end-start:.2f}s")
        return result
    return wrapper
```

## 🚀 Wdrożenie Produkcyjne

### API REST (Flask):
```python
from flask import Flask, request, jsonify, send_file
import os

app = Flask(__name__)
analyzer = DocumentAnalyzer()

@app.route('/analyze', methods=['POST'])
def analyze_pdf():
    if 'pdf' not in request.files:
        return jsonify({'error': 'Brak pliku PDF'}), 400
    
    pdf_file = request.files['pdf']
    temp_path = f"/tmp/{pdf_file.filename}"
    pdf_file.save(temp_path)
    
    try:
        html_path = analyzer.analyze_document(temp_path)
        return send_file(html_path, as_attachment=True)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)
```

## 📈 Rozszerzenia i Rozwój

### Możliwe Rozszerzenia:

1. **Machine Learning dla Klasyfikacji**:
   ```bash
   pip install scikit-learn tensorflow
   # Trenowanie modeli klasyfikacji dokumentów
   ```

2. **Wsparcie dla Więcej Formatów**:
   ```bash
   pip install python-docx openpyxl
   # Obsługa DOCX, XLSX
   ```

3. **Przetwarzanie Wsadowe z Kolejkami**:
   ```bash
   pip install celery redis
   # Asynchroniczne przetwarzanie
   ```

4. **Interfejs Webowy**:
   ```bash
   pip install streamlit
   # GUI dla użytkowników
   ```

### Integracje:

- **Google Drive API** - automatyczny import PDF
- **Elasticsearch** - indeksowanie treści
- **PostgreSQL** - baza metadanych
- **AWS S3** - storage dokumentów

## 💡 Najlepsze Praktyki

### Optymalizacja Wydajności:
1. **Cache wyników OCR** dla identycznych bloków
2. **Przetwarzanie równoległe** dla batch processing
3. **Optymalizacja parametrów** dla konkretnych typów dokumentów
4. **Monitoring użycia pamięci** dla dużych plików

### Bezpieczeństwo:
1. **Walidacja plików PDF** przed przetwarzaniem
2. **Sandbox dla OCR** - izolacja procesów
3. **Czyszczenie plików tymczasowych**
4. **Logowanie operacji** dla audytu

### Utrzymanie:
1. **Regularne aktualizacje** bibliotek
2. **Backup konfiguracji** i modeli
3. **Testy regresji** po aktualizacjach
4. **Dokumentacja zmian** w kodzie

## 📞 Wsparcie

### Przydatne Zasoby:
- **Tesseract Wiki**: https://github.com/tesseract-ocr/tesseract/wiki
- **OpenCV Tutorials**: https://docs.opencv.org/4.x/d9/df8/tutorial_root.html
- **PDF2Image Docs**: https://github.com/Belval/pdf2image

### Społeczność:
- **GitHub Issues** - problemy i feature requests
- **Stack Overflow** - pytania techniczne
- **Reddit r/computervision** - dyskusje OCR

## 🎉 Gotowe do Użycia!

System jest teraz gotowy do analizy dokumentów PDF! Rozpocznij od prostych testów i stopniowo dostrajaj parametry dla swoich konkretnych przypadków użycia.

```bash
# Ostatni test instalacji
python src/pdf_analyzer.py --help
python src/usage_examples.py
```

