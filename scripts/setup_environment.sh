#!/bin/bash

# Exit on error
set -e

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check if running as root
if [ "$EUID" -eq 0 ]; then
    echo -e "${YELLOW}Warning: It's not recommended to run this script as root.${NC}"
    read -p "Do you want to continue? [y/N] " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

# Check Python version
PYTHON_CMD="python3"
if ! command -v python3 &> /dev/null; then
    PYTHON_CMD="python"
    if ! command -v python &> /dev/null; then
        echo "Python is not installed. Please install Python 3.7 or higher and try again."
        exit 1
    fi
fi

# Create virtual environment
echo -e "${GREEN}Creating Python virtual environment...${NC}"
$PYTHON_CMD -m venv venv

# Activate virtual environment
echo -e "\n${GREEN}Activating virtual environment...${NC}"
source venv/bin/activate

# Upgrade pip
echo -e "\n${GREEN}Upgrading pip...${NC}"
pip install --upgrade pip

# Install Python dependencies
echo -e "\n${GREEN}Installing Python dependencies...${NC}"
pip install -r requirements.txt

# Install system dependencies
echo -e "\n${GREEN}Installing system dependencies (Tesseract and Poppler)...${NC}"
chmod +x scripts/install_tesseract.sh
./scripts/install_tesseract.sh

echo -e "\n${GREEN}✅ Setup completed successfully!${NC}"
echo -e "To activate the virtual environment, run: ${YELLOW}source venv/bin/activate${NC}"
echo -e "To deactivate the virtual environment when done, run: ${YELLOW}deactivate${NC}"
