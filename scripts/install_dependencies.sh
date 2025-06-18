#!/bin/bash

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Detect the operating system
OS="$(uname -s)"

install_linux() {
    echo -e "${GREEN}Installing dependencies for Linux...${NC}"
    
    # Update package list
    sudo apt-get update
    
    # Install Tesseract and language packs
    echo -e "\n${YELLOW}Installing Tesseract OCR...${NC}"
    sudo apt-get install -y tesseract-ocr tesseract-ocr-pol tesseract-ocr-deu tesseract-ocr-eng
    sudo apt-get install -y libtesseract-dev libleptonica-dev
    
    # Install Poppler
    echo -e "\n${YELLOW}Installing Poppler...${NC}"
    sudo apt-get install -y poppler-utils
    
    # Install other system dependencies
    echo -e "\n${YELLOW}Installing other dependencies...${NC}"
    sudo apt-get install -y python3-dev python3-pip python3-venv
}

install_macos() {
    echo -e "${GREEN}Installing dependencies for macOS...${NC}"
    
    # Check if Homebrew is installed
    if ! command -v brew &> /dev/null; then
        echo -e "${YELLOW}Installing Homebrew...${NC}"
        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    fi
    
    # Install Tesseract
    echo -e "\n${YELLOW}Installing Tesseract OCR...${NC}"
    brew install tesseract tesseract-lang
    
    # Install Poppler
    echo -e "\n${YELLOW}Installing Poppler...${NC}"
    brew install poppler
}

# Main installation
case "${OS}" in
    Linux*)
        install_linux
        ;;
    Darwin*)
        install_macos
        ;;
    *)
        echo -e "${YELLOW}Unsupported operating system: ${OS}${NC}"
        echo "Please install dependencies manually."
        exit 1
        ;;
esac

echo -e "\n${GREEN}✅ All system dependencies have been installed successfully!${NC}"
