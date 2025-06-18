.PHONY: help setup install install-dev test test-cov lint format clean build run docker-build docker-run publish

# Default target
help:
	@echo "Available commands:"
	@echo "  setup       - Set up development environment (Python venv + dependencies)"
	@echo "  install     - Install production dependencies"
	@echo "  install-dev - Install development dependencies"
	@echo "  test        - Run tests"
	@echo "  test-cov    - Run tests with coverage"
	@echo "  lint        - Run linting checks"
	@echo "  format      - Format code"
	@echo "  clean       - Clean temporary files"
	@echo "  build       - Build the application"
	@echo "  run         - Run the application locally"
	@echo "  docker-build - Build Docker image"
	@echo "  docker-run  - Run Docker container"

# Setup and Installation
setup:
	@echo "Setting up development environment..."
	chmod +x scripts/setup_environment.sh
	./scripts/setup_environment.sh

# Installation
install: venv
	@echo "Installing production dependencies..."
	. venv/bin/activate && pip install -r requirements.txt

install-dev: venv
	@echo "Installing development dependencies..."
	. venv/bin/activate && \
	pip install -r requirements.txt -r requirements-dev.txt && \
	pre-commit install

venv:
	@if [ ! -d "venv" ]; then \
		echo "Virtual environment not found. Running setup..."; \
		$(MAKE) setup; \
	fi

# Check if Tesseract is installed
tesseract-check:
	@if ! command -v tesseract &> /dev/null; then \
		echo "Tesseract is not installed. Installing..."; \
		chmod +x scripts/install_tesseract.sh; \
		./scripts/install_tesseract.sh; \
	fi

# Testing
test:
	pytest tests/ -v

test-cov:
	pytest tests/ -v --cov=src --cov-report=html --cov-report=term

# Code quality
lint:
	flake8 src/ tests/
	mypy src/
	black --check src/ tests/
	isort --check-only src/ tests/

format:
	black src/ tests/
	isort src/ tests/

# Cleanup
clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	rm -rf build/ dist/ htmlcov/ .coverage .pytest_cache/

# Local development
build:
	poetry version patch
	poetry build

publish: build
	@echo "Publishing package to PyPI..."
	poetry publish

run:
	python -m uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload


# Docker commands
docker-build:
	docker build -t european-invoice-ocr .

docker-run:
	docker-compose up -d

docker-dev:
	docker-compose -f docker-compose.dev.yml up

docker-stop:
	docker-compose down

# Setup environment
setup:
	chmod +x scripts/setup.sh
	./scripts/setup.sh

# Download models
download-models:
	python scripts/download_models.py

# Validate installation
validate:
	python scripts/validate_installation.py

# Run benchmarks
benchmark:
	python scripts/benchmark.py