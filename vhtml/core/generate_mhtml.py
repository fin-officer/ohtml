import os
import json
import base64
import logging
from datetime import datetime
from pathlib import Path
from typing import Optional, List, Dict, Any

# Configure logging
logger = logging.getLogger('vhtml.mhtml_generator')

def generate_mhtml(document_folder: str, output_file: str) -> bool:
    """
    Generate MHTML file from document folder containing HTML, JS, and JSON files.
    
    Args:
        document_folder: Path to folder containing document files
        output_file: Path where to save the MHTML file
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        logger.info(f"Generating MHTML from folder: {document_folder}")
        folder = Path(document_folder)
        name = folder.name
        
        # Find required files
        html_files = list(folder.glob("*.html"))
        js_files = list(folder.glob("*.js"))
        json_files = list(folder.glob("*.json"))
        png_files = list(folder.glob("*.png"))
        
        if not html_files or not json_files:
            logger.error("Missing required HTML or JSON files in the document folder")
            return False
            
        html_file = html_files[0]
        json_file = json_files[0]
        
        # JS file is optional
        js_content = ""
        if js_files:
            js_file = js_files[0]
            logger.debug(f"Found JS file: {js_file}")
            js_content = js_file.read_text(encoding='utf-8')
            js_content = f"<script>\n{js_content}\n</script>"

        # Read files
        logger.debug(f"Reading HTML file: {html_file}")
        html_content = html_file.read_text(encoding='utf-8')
        
        # Load and validate JSON
        logger.debug(f"Reading JSON file: {json_file}")
        try:
            json_data = json.loads(json_file.read_text(encoding='utf-8'))
            embedded_json = f"<script>window.data = {json.dumps(json_data, ensure_ascii=False, indent=2)};</script>"
        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON in {json_file}: {e}")
            return False
            
        # Prepare final HTML with embedded data and scripts
        final_html = html_content
        if "<!--DATA-->" in html_content:
            final_html = final_html.replace("<!--DATA-->", embedded_json)
        if js_content and "<!--SCRIPT-->" in html_content:
            final_html = final_html.replace("<!--SCRIPT-->", js_content)
            
        # If no placeholders found, append data and scripts at the end of body
        if "<!--DATA-->" not in html_content:
            final_html = final_html.replace("</body>", f"{embedded_json}\n</body>")
        if js_content and "<!--SCRIPT-->" not in html_content:
            final_html = final_html.replace("</body>", f"{js_content}\n</body>")

        # Process images in the HTML and embed them as base64
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(final_html, 'html.parser')
        
        # Find all images and replace with base64 data
        for img in soup.find_all('img'):
            if 'src' in img.attrs:
                img_src = img['src']
                if not img_src.startswith(('http://', 'https://', 'data:')):
                    img_path = folder / img_src
                    if img_path.exists():
                        try:
                            # Read image and convert to base64
                            with open(img_path, 'rb') as img_file:
                                img_data = img_file.read()
                                img_base64 = base64.b64encode(img_data).decode('utf-8')
                                
                                # Determine MIME type
                                if str(img_path).lower().endswith('.png'):
                                    mime_type = 'image/png'
                                elif str(img_path).lower().endswith(('.jpg', '.jpeg')):
                                    mime_type = 'image/jpeg'
                                elif str(img_path).lower().endswith('.gif'):
                                    mime_type = 'image/gif'
                                else:
                                    mime_type = 'image/png'  # default
                                
                                # Replace src with base64 data
                                img['src'] = f'data:{mime_type};base64,{img_base64}'
                                logger.debug(f"Embedded image: {img_path}")
                                
                        except Exception as e:
                            logger.error(f"Error embedding image {img_path}: {e}")
        
        final_html = str(soup)
        
        # Encode as base64 for MHTML
        encoded_html = base64.b64encode(final_html.encode('utf-8')).decode('utf-8')
        now = datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')

        # Create MHTML content
        mhtml = f"""From: <Saved by vHTML>
Subject: {name}
Date: {now}
MIME-Version: 1.0
Content-Type: multipart/related; boundary="----=_NextPart_000_0000"; type="text/html"

------=_NextPart_000_0000
Content-Type: text/html; charset="utf-8"
Content-Transfer-Encoding: base64
Content-Location: file://{name}.html

{encoded_html}
------=_NextPart_000_0000--
"""

        # Ensure output directory exists
        output_path = Path(output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Save the MHTML file
        with output_path.open('w', encoding='utf-8') as f:
            f.write(mhtml)
            
        logger.info(f"Successfully generated MHTML: {output_file}")
        print(f"✅ Generated MHTML: {output_file}")
        return True
        
    except Exception as e:
        logger.error(f"Error generating MHTML: {str(e)}", exc_info=True)
        print(f"❌ Error generating MHTML: {str(e)}")
        return False


def main():
    """Command line interface for MHTML generation"""
    import argparse
    import sys
    
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Generate MHTML file from document folder")
    parser.add_argument(
        "input_folder",
        help="Path to the folder containing document files (HTML, JSON, JS)"
    )
    parser.add_argument(
        "-o", "--output",
        help="Output MHTML file path (default: <input_folder>.mhtml)",
        default=None
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose output"
    )
    
    # Parse arguments
    args = parser.parse_args()
    
    # Set up logging
    log_level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(
        level=log_level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # Determine output file path
    input_path = Path(args.input_folder)
    output_file = args.output
    if not output_file:
        output_file = input_path.with_suffix('.mhtml')
    
    # Generate MHTML
    success = generate_mhtml(args.input_folder, output_file)
    
    # Exit with appropriate status code
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
