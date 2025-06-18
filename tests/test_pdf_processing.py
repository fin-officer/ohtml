import os
import pytest
from pathlib import Path
from vhtml.main import DocumentAnalyzer
from vhtml.core.generate_mhtml import generate_mhtml
from vhtml.core.generate_standalone_html import create_standalone_html

def test_pdf_to_html(tmp_path):
    analyzer = DocumentAnalyzer()
    input_pdf = "invoices/Invoice-30392B3C-0001.pdf"
    output_dir = tmp_path / "single_html"
    os.makedirs(output_dir, exist_ok=True)
    html_path = analyzer.analyze_document(input_pdf, str(output_dir))
    assert Path(html_path).exists()
    assert html_path.endswith(".html")

def test_html_to_mhtml(tmp_path):
    analyzer = DocumentAnalyzer()
    input_pdf = "invoices/Invoice-30392B3C-0001.pdf"
    output_dir = tmp_path / "mhtml"
    os.makedirs(output_dir, exist_ok=True)
    html_path = analyzer.analyze_document(input_pdf, str(output_dir))
    mhtml_path = output_dir / (Path(input_pdf).stem + ".mhtml")
    assert generate_mhtml(str(output_dir), str(mhtml_path))
    assert mhtml_path.exists()
    with open(mhtml_path, "r", encoding="utf-8") as f:
        content = f.read()
        assert "Content-Type: multipart/related" in content

def test_html_to_standalone_html(tmp_path):
    analyzer = DocumentAnalyzer()
    input_pdf = "invoices/Invoice-30392B3C-0001.pdf"
    output_dir = tmp_path / "standalone_html"
    os.makedirs(output_dir, exist_ok=True)
    html_path = analyzer.analyze_document(input_pdf, str(output_dir))
    standalone_html = output_dir / (Path(input_pdf).stem + "_standalone.html")
    create_standalone_html(str(output_dir), str(standalone_html))
    assert standalone_html.exists()
    with open(standalone_html, "r", encoding="utf-8") as f:
        content = f.read()
        assert "<html" in content
        assert "<img" in content or "data:image" in content

def test_invalid_pdf_raises(tmp_path):
    analyzer = DocumentAnalyzer()
    bad_pdf = tmp_path / "bad.pdf"
    with open(bad_pdf, "w") as f:
        f.write("not a real pdf")
    with pytest.raises(Exception):
        analyzer.analyze_document(str(bad_pdf), str(tmp_path))
