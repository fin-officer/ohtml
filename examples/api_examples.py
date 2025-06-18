"""
API Examples for PDF-to-Image and Invoice Data Extraction
"""
import requests

API_URL = "http://localhost:8000"

# Example 1: PDF to Images
with open("invoices/Invoice-30392B3C-0001.pdf", "rb") as f:
    files = {"pdf": ("Invoice-30392B3C-0001.pdf", f, "application/pdf")}
    resp = requests.post(f"{API_URL}/pdf-to-images", files=files)
    print("PDF to Images Response:")
    print(resp.json())

# Example 2: Invoice Field Extraction
with open("invoices/Invoice-30392B3C-0001.pdf", "rb") as f:
    files = {"pdf": ("Invoice-30392B3C-0001.pdf", f, "application/pdf")}
    resp = requests.post(f"{API_URL}/extract-invoice-fields", files=files)
    print("\nInvoice Field Extraction Response:")
    print(resp.json())

# Example 3: Metadata Extraction
with open("invoices/Invoice-30392B3C-0001.pdf", "rb") as f:
    files = {"pdf": ("Invoice-30392B3C-0001.pdf", f, "application/pdf")}
    resp = requests.post(f"{API_URL}/extract-metadata", files=files)
    print("\nMetadata Extraction Response:")
    print(resp.json())
