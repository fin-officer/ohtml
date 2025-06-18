import pytest
import os
from pathlib import Path
from PIL import Image
from vhtml.core.pdf_processor import PDFProcessor
from vhtml.core.ocr_engine import OCREngine
from vhtml.core.layout_analyzer import LayoutAnalyzer, Block, DocumentMetadata
from vhtml.core.html_generator import HTMLGenerator

@pytest.fixture
def sample_pdf_path():
    return "invoices/Invoice-30392B3C-0001.pdf"

@pytest.fixture
def pdf_processor():
    return PDFProcessor()

@pytest.fixture
def ocr_engine():
    return OCREngine()

@pytest.fixture
def layout_analyzer():
    return LayoutAnalyzer()

@pytest.fixture
def html_generator():
    return HTMLGenerator()

def test_pdf_to_images(pdf_processor, sample_pdf_path):
    """Test PDF to image conversion"""
    images = pdf_processor.pdf_to_images(sample_pdf_path)
    assert len(images) > 0
    assert all(isinstance(img, Image.Image) for img in images)

def test_ocr_engine(ocr_engine, sample_pdf_path):
    """Test OCR engine with a sample image"""
    images = PDFProcessor().pdf_to_images(sample_pdf_path)
    sample_image = images[0]
    
    # Test OCR on a small portion of the image
    text, lang, confidence = ocr_engine.extract_text_from_block(
        sample_image, 
        {'x': 0, 'y': 0, 'width': sample_image.width, 'height': 50}
    )
    assert isinstance(text, str)
    assert lang in ['pl', 'en', 'de', 'unknown']
    assert 0 <= confidence <= 1.0

def test_layout_analysis(layout_analyzer, sample_pdf_path):
    """Test layout analysis on a sample PDF"""
    images = PDFProcessor().pdf_to_images(sample_pdf_path)
    layout_type, blocks = layout_analyzer.analyze_layout(images[0])
    
    assert isinstance(layout_type, str)
    assert isinstance(blocks, list)
    if blocks:  # If blocks are found
        assert all('position' in block for block in blocks)

def test_html_generation(html_generator, sample_pdf_path, tmp_path):
    """Test HTML generation from document metadata"""
    # Create a simple document metadata structure
    sample_block = Block(
        id="test_block",
        type="content",
        position={"x": 0, "y": 0, "width": 100, "height": 100},
        content="Test content",
        language="en",
        confidence=0.9,
        formatting={"bold": False, "italic": False}
    )
    
    metadata = DocumentMetadata(
        doc_type="test",
        language="en",
        layout="test_layout",
        confidence=0.9,
        blocks=[sample_block]
    )
    
    # Generate HTML
    images = PDFProcessor().pdf_to_images(sample_pdf_path)
    html = html_generator.generate_html(metadata, images)
    
    # Test saving HTML
    output_path = os.path.join(tmp_path, "test_output.html")
    html_generator.save_html_with_metadata(html, metadata, output_path)
    
    assert os.path.exists(output_path)
    assert os.path.getsize(output_path) > 0
