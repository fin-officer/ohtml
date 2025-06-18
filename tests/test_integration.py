import pytest
import os
from pathlib import Path
from vhtml.main import DocumentAnalyzer

@pytest.fixture
def document_analyzer():
    return DocumentAnalyzer()

def test_document_analysis(document_analyzer, tmp_path):
    """Test complete document analysis pipeline"""
    # Test with a sample invoice
    input_pdf = "invoices/Invoice-30392B3C-0001.pdf"
    output_dir = str(tmp_path / "output")
    
    # Process the document
    html_path = document_analyzer.analyze_document(input_pdf, output_dir)
    
    # Verify output
    assert os.path.exists(html_path)
    assert html_path.endswith(".html")
    assert os.path.getsize(html_path) > 0
    
    # Verify metadata was created
    metadata_path = html_path.replace('.html', '_metadata.json')
    assert os.path.exists(metadata_path)

def test_batch_processing(document_analyzer, tmp_path):
    """Test batch processing of multiple PDFs"""
    from vhtml.main import AdvancedAnalyzer
    
    analyzer = AdvancedAnalyzer()
    input_dir = "invoices"
    output_dir = str(tmp_path / "batch_output")
    
    # Process all PDFs in the input directory
    results = analyzer.batch_analyze(input_dir, output_dir)
    
    # Verify results
    assert isinstance(results, dict)
    assert len(results) > 0
    
    # Check that output files were created
    for pdf_file, result in results.items():
        if result['status'] == 'success':
            html_path = result['html_path']
            assert os.path.exists(html_path)
            assert os.path.getsize(html_path) > 0
            
            metadata_path = html_path.replace('.html', '_metadata.json')
            assert os.path.exists(metadata_path)
