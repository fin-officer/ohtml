from fastapi import APIRouter, UploadFile, File
from typing import List
import shutil
import tempfile
from services.pdf_utils import pdf_to_images
from services.extraction import extract_invoice_fields_from_text
from pathlib import Path
import fitz

router = APIRouter()

@router.post("/pdf-to-images")
def pdf_to_images_endpoint(pdf: UploadFile = File(...)) -> List[str]:
    """Accepts a PDF upload and returns a list of generated image paths."""
    with tempfile.TemporaryDirectory() as tmpdir:
        pdf_path = Path(tmpdir) / pdf.filename
        with open(pdf_path, "wb") as f:
            shutil.copyfileobj(pdf.file, f)
        output_dir = Path(tmpdir) / "images"
        image_paths = pdf_to_images(str(pdf_path), str(output_dir))
        # Optionally, return images as base64 or URLs
        return [str(p) for p in image_paths]

@router.post("/extract-invoice-fields")
def extract_invoice_fields_endpoint(pdf: UploadFile = File(...)):
    """Extract invoice fields from a PDF by running OCR on all pages and parsing the text."""
    import pytesseract
    from PIL import Image
    with tempfile.TemporaryDirectory() as tmpdir:
        pdf_path = Path(tmpdir) / pdf.filename
        with open(pdf_path, "wb") as f:
            shutil.copyfileobj(pdf.file, f)
        images_dir = Path(tmpdir) / "images"
        image_paths = pdf_to_images(str(pdf_path), str(images_dir))
        full_text = ""
        for img_path in image_paths:
            img = Image.open(img_path)
            full_text += pytesseract.image_to_string(img, lang="pol+eng") + "\n"
        fields = extract_invoice_fields_from_text(full_text)
        return fields

@router.post("/extract-metadata")
def extract_metadata_endpoint(pdf: UploadFile = File(...)):
    """Extracts basic metadata from the PDF (number of pages, size, etc)."""
    with tempfile.TemporaryDirectory() as tmpdir:
        pdf_path = Path(tmpdir) / pdf.filename
        with open(pdf_path, "wb") as f:
            shutil.copyfileobj(pdf.file, f)
        doc = fitz.open(str(pdf_path))
        meta = doc.metadata
        return {
            "pages": doc.page_count,
            "metadata": meta,
            "size_bytes": pdf_path.stat().st_size
        }
