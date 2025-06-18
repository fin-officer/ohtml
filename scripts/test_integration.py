#!/usr/bin/env python3
"""
Test Integration Script for vHTML
Tests the complete integration of all components in a simple workflow
"""

import os
import sys
import argparse
from pathlib import Path

# Add parent directory to path so we can import vhtml
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from vhtml.main import DocumentAnalyzer

def main():
    """Test the integrated vHTML system"""
    parser = argparse.ArgumentParser(description="vHTML Integration Test")
    parser.add_argument("pdf_file", help="Path to PDF file for testing")
    parser.add_argument("-o", "--output", help="Output directory", default="test_output")
    parser.add_argument("-v", "--view", help="Open HTML in browser after generation", action="store_true")
    
    args = parser.parse_args()
    
    # Validate input file
    if not os.path.exists(args.pdf_file):
        print(f"Error: File not found: {args.pdf_file}")
        sys.exit(1)
    
    if not args.pdf_file.lower().endswith('.pdf'):
        print(f"Error: File must be a PDF: {args.pdf_file}")
        sys.exit(1)
    
    # Create output directory if it doesn't exist
    os.makedirs(args.output, exist_ok=True)
    
    print(f"🔍 Testing vHTML integration with file: {args.pdf_file}")
    print(f"📁 Output directory: {args.output}")
    
    try:
        # Initialize the document analyzer
        analyzer = DocumentAnalyzer()
        
        # Process the document
        html_path = analyzer.analyze_document(args.pdf_file, args.output)
        
        print(f"\n✅ Integration test successful!")
        print(f"📄 Generated HTML: {html_path}")
        
        # Open in browser if requested
        if args.view:
            import webbrowser
            webbrowser.open(f'file://{os.path.abspath(html_path)}')
            print("🌐 Opening HTML in browser...")
        
    except Exception as e:
        print(f"\n❌ Integration test failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
