"""
Examples of using the vHTML library to process PDF documents and generate MHTML.
"""
import os
import json
import shutil
from pathlib import Path
from datetime import datetime
from vhtml.main import DocumentAnalyzer, AdvancedAnalyzer
from vhtml.core.generate_mhtml import generate_mhtml

def print_header(title):
    """Print a formatted header."""
    print("\n" + "=" * 80)
    print(f"{title:^80}")
    print("=" * 80)

def process_single_document():
    """Example of processing a single PDF document."""
    print_header("EXAMPLE 1: PROCESS SINGLE DOCUMENT")
    
    # Initialize the analyzer
    analyzer = DocumentAnalyzer()
    
    # Input and output paths
    input_pdf = "invoices/Invoice-30392B3C-0001.pdf"
    output_dir = "output/single_document"
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    print(f"Processing: {input_pdf}")
    
    # Process the document
    try:
        start_time = datetime.now()
        html_path = analyzer.analyze_document(input_pdf, output_dir)
        processing_time = (datetime.now() - start_time).total_seconds()
        
        print(f"✅ Successfully processed in {processing_time:.2f} seconds")
        print(f"📄 Generated HTML: {os.path.abspath(html_path)}")
        
        # Display metadata
        metadata_path = html_path.replace('.html', '_metadata.json')
        with open(metadata_path, 'r', encoding='utf-8') as f:
            metadata = json.load(f)
            print("\n📋 Document Metadata:")
            print(f"   - Type: {metadata['doc_type']}")
            print(f"   - Language: {metadata['language']}")
            print(f"   - Layout: {metadata['layout']}")
            print(f"   - Confidence: {metadata['confidence']:.2f}")
            print(f"   - Blocks: {len(metadata['blocks'])}")
            
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

def process_multiple_documents():
    """Example of processing multiple PDF documents."""
    print_header("EXAMPLE 2: PROCESS MULTIPLE DOCUMENTS")
    
    # Initialize the advanced analyzer
    analyzer = AdvancedAnalyzer()
    
    # Input and output paths
    input_dir = "invoices"
    output_dir = "output/examples/multiple_documents"
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Get all PDF files in the input directory
    pdf_files = list(Path(input_dir).glob("*.pdf"))
    print(f"Found {len(pdf_files)} PDF files to process")
    
    if not pdf_files:
        print("No PDF files found in the input directory")
        return
    
    # Process all PDFs in the input directory
    start_time = datetime.now()
    results = analyzer.batch_analyze(input_dir, output_dir)
    processing_time = (datetime.now() - start_time).total_seconds()
    
    # Print summary
    success = sum(1 for r in results.values() if r['status'] == 'success')
    errors = len(results) - success
    
    print(f"\n📊 Processing Summary:")
    print(f"   - Total files: {len(results)}")
    print(f"   - Success: {success}")
    print(f"   - Errors: {errors}")
    print(f"   - Processing time: {processing_time:.2f} seconds")
    print(f"   - Avg. time per document: {processing_time/len(results):.2f} seconds")
    
    # Print results for each file
    print("\n📄 Results:")
    for pdf_file, result in results.items():
        status = "✅" if result['status'] == 'success' else "❌"
        print(f"{status} {os.path.basename(pdf_file)}: {result['status']}")
        if 'html_path' in result and result['status'] == 'success':
            print(f"   → {os.path.abspath(result['html_path'])}")

def custom_processing():
    """Example of custom processing with advanced options."""
    print_header("EXAMPLE 3: CUSTOM PROCESSING")
    
    # Initialize the analyzer
    analyzer = DocumentAnalyzer()
    
    # Process a document with custom settings
    input_pdf = "invoices/Invoice-30392B3C-0001.pdf"
    output_dir = "output/examples/custom_processing"
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    print(f"Processing with custom settings: {input_pdf}")
    
    # Here you would add custom processing logic
    # For example, you could modify the analyzer settings before processing
    
    try:
        # Process the document
        html_path = analyzer.analyze_document(input_pdf, output_dir)
        print(f"✅ Successfully processed")
        print(f"📄 Generated HTML: {os.path.abspath(html_path)}")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

def generate_mhtml_example():
    """Example of generating MHTML from processed documents."""
    print_header("EXAMPLE 4: GENERATE MHTML")
    
    # Initialize the analyzer
    analyzer = DocumentAnalyzer()
    
    # Input and output paths
    input_pdf = "invoices/Invoice-30392B3C-0001.pdf"
    output_dir = "output/mhtml_example"
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    print(f"Processing: {input_pdf}")
    
    try:
        start_time = datetime.now()
        html_path = analyzer.analyze_document(input_pdf, output_dir)
        processing_time = (datetime.now() - start_time).total_seconds()
        print(f"✅ Successfully processed in {processing_time:.2f} seconds")
        
        # Generate MHTML
        mhtml_path = os.path.join(output_dir, os.path.splitext(os.path.basename(input_pdf))[0] + ".mhtml")
        print("\n🔧 Generating MHTML file...")
        success = generate_mhtml(os.path.dirname(html_path), mhtml_path)
        if success:
            print(f"✅ Successfully generated MHTML: {mhtml_path}")
            # Optionally, copy to a custom filename
            faktura_path = "faktura-123.mhtml"
            shutil.copy(mhtml_path, faktura_path)
            print(f"📦 Created copy as: {faktura_path}")
        else:
            print(f"❌ Failed to generate MHTML")
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

def main():
    print("""
================================================================================
                                 vHTML EXAMPLES                                 
================================================================================
This script demonstrates various ways to use the vHTML library\n""")
    process_single_document()
    process_multiple_documents()
    custom_processing()
    generate_mhtml_example()

if __name__ == "__main__":
    main()
