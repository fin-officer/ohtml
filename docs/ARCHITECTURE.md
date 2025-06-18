# PDF to HTML Conversion System with OCR

## 1. System Architecture

### Core Components:
- **PDF Processor** - converts PDF documents to images
- **Layout Analyzer** - analyzes page layout and segments content blocks
- **OCR Engine** - performs text recognition in content blocks
- **Language Detector** - identifies document language and format
- **HTML Generator** - creates structured HTML with metadata
- **Template Engine** - provides templates for different document types

## 2. Technology Stack

### Core Libraries:
- **OpenCV** - image processing and segmentation
- **Tesseract/EasyOCR** - optical character recognition
- **pdf2image** - PDF to image conversion
- **langdetect** - language detection
- **Jinja2** - HTML templating
- **scikit-image** - advanced image operations

### Additional Tools:
- **PyMuPDF (fitz)** - alternative PDF processing
- **layoutparser** - pre-trained layout analysis models
- **spaCy** - text analysis and NER
- **Pillow** - image manipulation

## 3. System Workflow

### Step 1: PDF Preprocessing
```
PDF → Page Images → Preprocessing (denoising, deskewing) → Layout Analysis
```

### Step 2: Block Segmentation
```
Image → Text Block Detection → Block Classification → Block Hierarchy
```

### Step 3: OCR and Analysis
```
Block → OCR → Language Detection → Format Analysis → Metadata
```

### Step 4: HTML Generation
```
Block Structure + Text + Metadata → HTML Template → Final HTML
```

## 4. Document Types and Templates

### Invoice Template (4 blocks):
- **Block A** (top left) - sender information
- **Block B** (top right) - recipient information
- **Block C** (middle) - line items table
- **Block D** (bottom) - payment summary

### 6-Column Template:
- **Blocks A,B** (top row)
- **Blocks C,D** (middle row)
- **Blocks E,F** (bottom row)

### Universal Template:
- Automatic block count detection
- Adaptive segmentation

## 5. Metadata Structure

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
      "content": "recognized text",
      "language": "en",
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
