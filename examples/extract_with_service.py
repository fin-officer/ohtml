"""
Przykład użycia vhtml z wybraną usługą ekstrakcji oraz wyborem formatu wyjściowego.
"""
import subprocess
import sys

# Przykład: ekstrakcja danych z faktury przez Invoice Extractor i generacja MHTML
subprocess.run([
    sys.executable, '-m', 'vhtml.main',
    'invoices/Invoice-30392B3C-0001.pdf',
    '--extractor-service', 'invoice',
    '--format', 'mhtml',
    '-o', 'output/examples/invoice_extractor_mhtml'
])

# Przykład: ekstrakcja danych z paragonu przez Receipt Analyzer i generacja HTML
subprocess.run([
    sys.executable, '-m', 'vhtml.main',
    'invoices/Receipt-2914-4703.pdf',
    '--extractor-service', 'receipt',
    '--format', 'html',
    '-o', 'output/examples/receipt_analyzer_html'
])
