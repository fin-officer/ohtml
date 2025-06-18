from fastapi import FastAPI, UploadFile, File
from shared.utils.pdf_utils import pdf_to_images
from shared.utils.extraction import extract_invoice_fields_from_text
import tempfile
import shutil
from pathlib import Path
import pytesseract
from PIL import Image

app = FastAPI()

@app.post('/extract')
async def extract_invoice(file: UploadFile = File(...)):
    with tempfile.TemporaryDirectory() as tmpdir:
        pdf_path = Path(tmpdir) / file.filename
        with open(pdf_path, 'wb') as f:
            shutil.copyfileobj(file.file, f)
        images = pdf_to_images(str(pdf_path), str(Path(tmpdir) / 'images'))
        text = ''
        for img in images:
            text += pytesseract.image_to_string(Image.open(img), lang='pol+eng') + '\n'
        fields = extract_invoice_fields_from_text(text)
        return fields
