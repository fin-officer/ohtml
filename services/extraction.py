import re
from typing import Dict, List

def extract_invoice_fields_from_text(text: str) -> Dict[str, str]:
    """Extract common invoice fields from plain text using regex heuristics."""
    fields = {}
    # Example regexes (customize for your invoices)
    invoice_no = re.search(r'(Faktura|Invoice)[\s:]*([A-Za-z0-9\-/]+)', text, re.IGNORECASE)
    date = re.search(r'(Data wystawienia|Issue date|Data)[\s:]*([0-9]{4}-[0-9]{2}-[0-9]{2})', text)
    total = re.search(r'(Razem|Total)[\s:]*([0-9\., ]+\s?PLN)', text, re.IGNORECASE)
    seller = re.search(r'(Sprzedawca|Seller)[\s:]*([\w\s\.\-]+)', text, re.IGNORECASE)
    buyer = re.search(r'(Nabywca|Buyer)[\s:]*([\w\s\.\-]+)', text, re.IGNORECASE)
    if invoice_no:
        fields['invoice_number'] = invoice_no.group(2).strip()
    if date:
        fields['issue_date'] = date.group(2).strip()
    if total:
        fields['total'] = total.group(2).strip()
    if seller:
        fields['seller'] = seller.group(2).strip()
    if buyer:
        fields['buyer'] = buyer.group(2).strip()
    return fields
