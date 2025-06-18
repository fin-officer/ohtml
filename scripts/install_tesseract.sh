#!/bin/bash

# Detect the operating system
OS="$(uname -s)"

install_tesseract_linux() {
    echo "Detected Linux (Debian/Ubuntu)"
    echo "Installing Tesseract OCR and required language packs..."
    sudo apt-get update
    sudo apt-get install -y tesseract-ocr tesseract-ocr-pol tesseract-ocr-deu tesseract-ocr-eng
    sudo apt-get install -y libtesseract-dev libleptonica-dev
}

install_tesseract_macos() {
    echo "Detected macOS"
    echo "Installing Tesseract OCR and language packs using Homebrew..."
    brew install tesseract tesseract-lang
}

install_poppler_linux() {
    echo "Installing Poppler utilities..."
    sudo apt-get install -y poppler-utils
}

install_poppler_macos() {
    echo "Installing Poppler using Homebrew..."
    brew install poppler
}

# Main installation
case "${OS}" in
    Linux*)
        install_tesseract_linux
        install_poppler_linux
        ;;
    Darwin*)
        install_tesseract_macos
        install_poppler_macos
        ;;
    *)
        echo "Unsupported operating system: ${OS}"
        echo "Please install Tesseract OCR and Poppler manually"
        exit 1
        ;;
esac

# Verify installation
echo "\nVerifying Tesseract installation..."
if command -v tesseract &> /dev/null; then
    echo "Tesseract installation completed successfully!"
    tesseract --version | head -n 1
else
    echo "Tesseract installation failed or not found in PATH"
    exit 1
fi

echo "\nVerifying Poppler installation..."
if command -v pdftoppm &> /dev/null; then
    echo "Poppler utilities installed successfully!"
    pdftoppm -v 2>&1 | head -n 1
else
    echo "Poppler utilities not found in PATH"
    exit 1
fi
