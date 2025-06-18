# Przykłady użycia vHTML z usługami ekstrakcji i wyborem formatu

## 1. Wywołanie z poziomu Pythona

```python
import subprocess
subprocess.run([
    'python', '-m', 'vhtml.main',
    'invoices/Invoice-30392B3C-0001.pdf',
    '--extractor-service', 'invoice',
    '--format', 'mhtml',
    '-o', 'output/examples/invoice_extractor_mhtml'
])
```

---

## 2. Wywołanie z linii poleceń (CLI)

```bash
# Ekstrakcja danych z faktury przez Invoice Extractor i generacja MHTML
poetry run python -m vhtml.main invoices/Invoice-30392B3C-0001.pdf --extractor-service invoice --format mhtml -o output/examples/invoice_extractor_mhtml

# Ekstrakcja danych z paragonu przez Receipt Analyzer i generacja HTML
poetry run python -m vhtml.main invoices/Receipt-2914-4703.pdf --extractor-service receipt --format html -o output/examples/receipt_analyzer_html
```

---

## 3. Opis argumentów

- `--extractor-service` – wybór usługi ekstrakcji (np. invoice, receipt, cv, contract, ...)
- `--format` – format wyjściowy: `html` (jeden plik) lub `mhtml` (multipart)
- `-o`/`--output` – katalog wyjściowy

---

## 4. Inne przykłady

- Przetwarzanie wsadowe:

```bash
poetry run python -m vhtml.main invoices/ --batch --extractor-service invoice --format mhtml -o output/examples/batch_mhtml
```

- Otwieranie wyniku w przeglądarce:

```bash
poetry run python -m vhtml.main invoices/Invoice-30392B3C-0001.pdf --extractor-service invoice --format html --view
```

---

## 5. Użycie wszystkich usług dockerowych (Invoice, Receipt, ...)

Dla poniższych przykładów używaj wyłącznie istniejących plików PDF z katalogu `invoices/`:

- Faktury: Invoice-30392B3C-0001.pdf, Invoice-30392B3C-0002.pdf, Invoice-34967F04-0002.pdf
- Paragony: Receipt-2914-4703.pdf, Receipt-2003-4795.pdf
- Transakcje Adobe: Adobe_Transaction_No_2878915736_20240920.pdf

### Sposób 1: Przez gateway (`docker-compose` w katalogu głównym projektu)

```bash
# Ekstrakcja faktury przez Invoice Extractor (MHTML)
poetry run python -m vhtml.main invoices/Invoice-30392B3C-0001.pdf --docker ../../ --extractor-service invoice --format mhtml -o output/examples/invoice_mhtml

# Ekstrakcja kolejnej faktury
poetry run python -m vhtml.main invoices/Invoice-34967F04-0002.pdf --docker ../../ --extractor-service invoice --format html -o output/examples/invoice_html

# Ekstrakcja paragonu przez Receipt Analyzer
poetry run python -m vhtml.main invoices/Receipt-2914-4703.pdf --docker ../../ --extractor-service receipt --format html -o output/examples/receipt_html

# Ekstrakcja kolejnego paragonu
poetry run python -m vhtml.main invoices/Receipt-2003-4795.pdf --docker ../../ --extractor-service receipt --format mhtml -o output/examples/receipt_mhtml

# Ekstrakcja transakcji Adobe przez Invoice Extractor
poetry run python -m vhtml.main invoices/Adobe_Transaction_No_2878915736_20240920.pdf --docker ../../ --extractor-service invoice --format html -o output/examples/adobe_invoice_html
```

### Sposób 2: Bezpośrednio do usługi (adapter, port)

```bash
# Ekstrakcja faktury bezpośrednio przez adapter (port 8001)
poetry run python -m vhtml.main invoices/Invoice-30392B3C-0001.pdf --adapter invoice --adapter-port 8001

# Ekstrakcja paragonu przez adapter (port 8002)
poetry run python -m vhtml.main invoices/Receipt-2914-4703.pdf --adapter receipt --adapter-port 8002

# Ekstrakcja CV przez adapter (port 8003)
poetry run python -m vhtml.main invoices/Invoice-30392B3C-0002.pdf --adapter cv --adapter-port 8003

# Ekstrakcja kontraktu przez adapter (port 8004)
poetry run python -m vhtml.main invoices/Invoice-34967F04-0002.pdf --adapter contract --adapter-port 8004

# Ekstrakcja sprawozdania finansowego przez adapter (port 8005)
poetry run python -m vhtml.main invoices/Adobe_Transaction_No_2878915736_20240920.pdf --adapter financial --adapter-port 8005

# Ekstrakcja dokumentacji medycznej przez adapter (port 8006)
poetry run python -m vhtml.main invoices/Invoice-AF90A26A-0005.pdf --adapter medical --adapter-port 8006

# Ekstrakcja dokumentów prawnych przez adapter (port 8007)
poetry run python -m vhtml.main invoices/Invoice-9BDC34D5-0001.pdf --adapter legal --adapter-port 8007

# Ekstrakcja formularza podatkowego przez adapter (port 8008)
poetry run python -m vhtml.main invoices/Invoice-9BDC34D5-0002.pdf --adapter tax --adapter-port 8008

# Ekstrakcja roszczenia ubezpieczeniowego przez adapter (port 8009)
poetry run python -m vhtml.main invoices/Invoice-9BDC34D5-0003.pdf --adapter insurance --adapter-port 8009

# Ekstrakcja świadectwa edukacyjnego przez adapter (port 8010)
poetry run python -m vhtml.main invoices/Invoice-34967F04-0001.pdf --adapter education --adapter-port 8010
```

---

## 6. Automatyczne testowanie dockerów tylko dla istniejących plików

```python
import subprocess
files = [
    ("invoice", "invoices/Invoice-30392B3C-0001.pdf"),
    ("invoice", "invoices/Invoice-34967F04-0002.pdf"),
    ("receipt", "invoices/Receipt-2914-4703.pdf"),
    ("receipt", "invoices/Receipt-2003-4795.pdf"),
    ("invoice", "invoices/Adobe_Transaction_No_2878915736_20240920.pdf"),
]
for service, pdf in files:
    subprocess.run([
        "python", "-m", "vhtml.main", pdf,
        "--docker", "../ścieżka/do/docker-compose/",
        "--extractor-service", service,
        "--format", "html",
        "-o", f"output/examples/{service}_{pdf.split('/')[-1].replace('.pdf','')}_html"
    ])
```

---

## 7. Sprawdzanie działania usług

- Po uruchomieniu z `--docker`, możesz sprawdzić status kontenerów:

```bash
docker ps
```

- Logi konkretnej usługi:

```bash
docker logs invoice-extractor
```

---

## 8. Ważne

- Upewnij się, że porty 8000-8010 są wolne.
- Katalog z docker-compose musi zawierać plik docker-compose.yml i wszystkie wymagane serwisy.
- Jeśli chcesz przetestować tylko jedną usługę, możesz podać jej nazwę w `--extractor-service`.

---
