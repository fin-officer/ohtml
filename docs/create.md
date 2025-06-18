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