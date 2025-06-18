"""
Example of generating standalone HTML with embedded images, JS, and JSON using vHTML.
"""
import os
from pathlib import Path
from vhtml.core.generate_standalone_html import create_standalone_html

def print_header(title):
    print("\n" + "=" * 80)
    print(f"{title:^80}")
    print("=" * 80)

def standalone_html_example():
    print_header("EXAMPLE: GENERATE STANDALONE HTML")
    input_pdf_folder = "output/mhtml_example/Invoice-30392B3C-0001"  # Example folder with HTML, images, JS, JSON
    output_html = "output/html_example/Invoice-30392B3C-0001_standalone.html"
    os.makedirs(os.path.dirname(output_html), exist_ok=True)
    print(f"Generating standalone HTML from: {input_pdf_folder}")
    try:
        create_standalone_html(input_pdf_folder, output_html)
        print(f"✅ Standalone HTML generated: {os.path.abspath(output_html)}")
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

def main():
    standalone_html_example()

if __name__ == "__main__":
    main()
