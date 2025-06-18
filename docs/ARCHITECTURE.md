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
