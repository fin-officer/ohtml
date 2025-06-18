.PHONY: help setup install install-dev test test-cov lint format clean build run docker-build docker-run publish

# Default target
help:
	@echo "Available commands:"
	@echo "  setup       - Set up development environment with Poetry"
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
	@echo "Setting up development environment with Poetry..."
	@if ! command -v poetry &> /dev/null; then \
		echo "Poetry not found. Installing..."; \
		curl -sSL https://install.python-poetry.org | python3 -; \
	fi
	poetry install
	@echo "Installing system dependencies..."
	chmod +x scripts/install_dependencies.sh
	./scripts/install_dependencies.sh

# Installation
install:
	@echo "Installing production dependencies with Poetry..."
	poetry install --without dev

install-dev:
	@echo "Installing development dependencies with Poetry..."
	poetry install
	poetry run pre-commit install

# Testing
test:
	poetry run pytest tests/ -v

test-cov:
	poetry run pytest tests/ -v --cov=src --cov-report=html --cov-report=term

# Code quality
lint:
	poetry run flake8 src/ tests/
	poetry run mypy src/
	poetry run black --check src/ tests/
	poetry run isort --check-only src/ tests/

format:
	poetry run black src/ tests/
	poetry run isort src/ tests/

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
	poetry run python -m uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload

# Docker commands
docker-build:
	docker build -t european-invoice-ocr .

docker-run:
	docker-compose up -d

docker-dev:
	docker-compose -f docker-compose.dev.yml up

docker-stop:
	docker-compose down

# Download models
download-models:
	poetry run python scripts/download_models.py

# Validate installation
validate:
	poetry run python scripts/validate_installation.py

# Run benchmarks
benchmark:
	poetry run python scripts/benchmark.py

# === TESTY INTEGRACYJNE USŁUG EKSTRAKCJI ===

test-gateway:
	poetry run python -m vhtml.main invoices/Invoice-30392B3C-0001.pdf --docker ../../ --extractor-service invoice --format mhtml -o output/examples/invoice_mhtml

test-adapter:
	poetry run python -m vhtml.main invoices/Invoice-30392B3C-0001.pdf --adapter invoice --adapter-port 8001

test-dockerfile:
	poetry run python -m vhtml.main invoices/Invoice-30392B3C-0001.pdf \
		--dockerfile ./services/01-invoice-extractor/Dockerfile \
		--adapter invoice --adapter-port 8001

# Batch test wszystkich adapterów (jeśli porty i pliki są dostępne)
test-adapter-all:
	poetry run python -m vhtml.main invoices/Invoice-30392B3C-0001.pdf --adapter invoice --adapter-port 8001
	poetry run python -m vhtml.main invoices/Receipt-2914-4703.pdf --adapter receipt --adapter-port 8002
	poetry run python -m vhtml.main invoices/Invoice-30392B3C-0002.pdf --adapter cv --adapter-port 8003
	poetry run python -m vhtml.main invoices/Invoice-34967F04-0002.pdf --adapter contract --adapter-port 8004
	poetry run python -m vhtml.main invoices/Adobe_Transaction_No_2878915736_20240920.pdf --adapter financial --adapter-port 8005