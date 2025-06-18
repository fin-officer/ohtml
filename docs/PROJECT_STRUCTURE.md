# Struktura Projektu

```
vhtml/
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

## Opis komponentów

### Core
- **pdf_processor.py** - Konwersja PDF do obrazów i wstępne przetwarzanie
- **layout_analyzer.py** - Analiza układu dokumentu i segmentacja bloków
- **ocr_engine.py** - Interfejs do silników OCR (Tesseract, EasyOCR)
- **html_generator.py** - Generowanie HTML z rozpoznanego tekstu i metadanych

### Templates
- **invoice_template.html** - Szablon dla faktur
- **form_template.html** - Szablon dla formularzy
- **universal_template.html** - Uniwersalny szablon dla różnych typów dokumentów

### Models
- **document_classifier.py** - Klasyfikacja typów dokumentów

### Utils
- **image_utils.py** - Narzędzia do przetwarzania obrazów
- **text_utils.py** - Narzędzia do przetwarzania tekstu
