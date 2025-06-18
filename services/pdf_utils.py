from typing import List
from pathlib import Path
import fitz  # PyMuPDF
import os

def pdf_to_images(pdf_path: str, output_dir: str) -> List[str]:
    """Converts all pages of a PDF to PNG images. Returns list of image file paths."""
    doc = fitz.open(pdf_path)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    image_paths = []
    for page_num in range(doc.page_count):
        page = doc.load_page(page_num)
        img_path = output_dir / f"page_{page_num+1}.png"
        pix = page.get_pixmap()
        pix.save(str(img_path))
        image_paths.append(str(img_path))
    return image_paths
