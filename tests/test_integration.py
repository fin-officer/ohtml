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
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Process the document
    try:
        html_path = document_analyzer.analyze_document(input_pdf, output_dir)
        
        # Verify output
        assert html_path is not None
        assert os.path.exists(html_path)
        assert html_path.endswith(".html")
        assert os.path.getsize(html_path) > 0
        
        # Verify metadata was created
        metadata_path = html_path.replace('.html', '_metadata.json')
        assert os.path.exists(metadata_path)
        assert os.path.getsize(metadata_path) > 0
        
    except Exception as e:
        pytest.fail(f"Document analysis failed with error: {e}")

def test_batch_processing(document_analyzer, tmp_path):
    """Test batch processing of multiple PDFs"""
    from vhtml.main import AdvancedAnalyzer
    
    analyzer = AdvancedAnalyzer()
    input_dir = "invoices"
    output_dir = str(tmp_path / "batch_output")
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Get list of PDF files in the input directory
    pdf_files = [f for f in os.listdir(input_dir) if f.lower().endswith('.pdf')]
    if not pdf_files:
        pytest.skip("No PDF files found in the input directory")
    
    try:
        # Process all PDFs in the input directory
        results = analyzer.batch_analyze(input_dir, output_dir)
        
        # Verify results
        assert isinstance(results, dict)
        assert len(results) > 0
        
        # Check that output files were created for successful operations
        success_count = 0
        for pdf_file, result in results.items():
            assert 'status' in result
            if result['status'] == 'success':
                success_count += 1
                assert 'html_path' in result
                html_path = result['html_path']
                assert os.path.exists(html_path)
                assert os.path.getsize(html_path) > 0
                
                metadata_path = html_path.replace('.html', '_metadata.json')
                assert os.path.exists(metadata_path)
                assert os.path.getsize(metadata_path) > 0
        
        # Ensure at least one successful processing
        assert success_count > 0, "No documents were processed successfully"
        
    except Exception as e:
        pytest.fail(f"Batch processing failed with error: {e}")
