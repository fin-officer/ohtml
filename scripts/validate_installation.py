#!/usr/bin/env python
"""
Validate vHTML installation by checking all required dependencies.
"""

import importlib
import os
import subprocess
import sys
from typing import Dict, List, Tuple

# Colors for terminal output
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"
BOLD = "\033[1m"

def check_python_version() -> Tuple[bool, str]:
    """Check if Python version meets requirements."""
    required_version = (3, 8)
    current_version = sys.version_info
    
    if current_version >= required_version:
        return True, f"Python {current_version.major}.{current_version.minor}.{current_version.micro}"
    else:
        return False, f"Python {current_version.major}.{current_version.minor}.{current_version.micro} (wymagana wersja ≥ {required_version[0]}.{required_version[1]})"

def check_python_packages() -> Dict[str, bool]:
    """Check if required Python packages are installed."""
    required_packages = [
        "cv2",  # OpenCV
        "pytesseract",
        "easyocr",
        "pdf2image",
        "fitz",  # PyMuPDF
        "PIL",  # Pillow
        "skimage",  # scikit-image
        "numpy",
        "pandas",
        "langdetect",
        "jinja2",
        "spacy",
        "textblob"
    ]
    
    optional_packages = [
        "layoutparser",
        "detectron2",
        "torch"
    ]
    
    results = {}
    
    # Check required packages
    for package in required_packages:
        try:
            if package == "cv2":
                # Special case for OpenCV
                module = importlib.import_module(package)
                results[f"{package} (OpenCV)"] = True
            else:
                module = importlib.import_module(package)
                results[package] = True
        except ImportError:
            results[package] = False
    
    # Check optional packages
    for package in optional_packages:
        try:
            module = importlib.import_module(package)
            results[f"{package} (opcjonalny)"] = True
        except ImportError:
            results[f"{package} (opcjonalny)"] = False
    
    return results

def check_tesseract() -> Tuple[bool, str]:
    """Check if Tesseract OCR is installed and available."""
    try:
        output = subprocess.check_output(["tesseract", "--version"], stderr=subprocess.STDOUT, text=True)
        version = output.split("\n")[0]
        return True, version
    except (subprocess.SubprocessError, FileNotFoundError):
        return False, "Nie znaleziono"

def check_poppler() -> Tuple[bool, str]:
    """Check if Poppler utilities are installed and available."""
    try:
        output = subprocess.check_output(["pdftoppm", "-v"], stderr=subprocess.STDOUT, text=True)
        version = output.strip()
        return True, version
    except (subprocess.SubprocessError, FileNotFoundError):
        return False, "Nie znaleziono"

def main():
    """Run all validation checks and display results."""
    print(f"{BOLD}Walidacja instalacji vHTML{RESET}\n")
    
    # Check Python version
    python_ok, python_version = check_python_version()
    status = f"{GREEN}✓{RESET}" if python_ok else f"{RED}✗{RESET}"
    print(f"{status} Python: {python_version}")
    
    # Check system dependencies
    tesseract_ok, tesseract_version = check_tesseract()
    status = f"{GREEN}✓{RESET}" if tesseract_ok else f"{RED}✗{RESET}"
    print(f"{status} Tesseract OCR: {tesseract_version}")
    
    poppler_ok, poppler_version = check_poppler()
    status = f"{GREEN}✓{RESET}" if poppler_ok else f"{RED}✗{RESET}"
    print(f"{status} Poppler: {poppler_version}")
    
    # Check Python packages
    print("\nPakiety Python:")
    packages = check_python_packages()
    for package, installed in packages.items():
        status = f"{GREEN}✓{RESET}" if installed else f"{RED}✗{RESET}"
        print(f"{status} {package}")
    
    # Summary
    all_required_ok = python_ok and tesseract_ok and poppler_ok and all(
        installed for pkg, installed in packages.items() if "opcjonalny" not in pkg
    )
    
    print("\n" + "-" * 50)
    if all_required_ok:
        print(f"{GREEN}{BOLD}Wszystkie wymagane komponenty są zainstalowane poprawnie!{RESET}")
    else:
        print(f"{RED}{BOLD}Niektóre wymagane komponenty nie są zainstalowane poprawnie.{RESET}")
        print("Sprawdź dokumentację instalacji: docs/INSTALLATION.md")
    
    # Optional components
    missing_optional = [pkg for pkg, installed in packages.items() if "opcjonalny" in pkg and not installed]
    if missing_optional:
        print(f"\n{YELLOW}Uwaga: Niektóre opcjonalne komponenty nie są zainstalowane:{RESET}")
        for pkg in missing_optional:
            print(f"  - {pkg}")

if __name__ == "__main__":
    main()
