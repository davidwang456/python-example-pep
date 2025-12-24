.PHONY: help install install-dev test test-cov lint format clean build upload

help:
	@echo "Available commands:"
	@echo "  make install       - Install project"
	@echo "  make install-dev   - Install development dependencies"
	@echo "  make test          - Run tests"
	@echo "  make test-cov      - Run tests with coverage report"
	@echo "  make lint          - Code linting"
	@echo "  make format        - Code formatting"
	@echo "  make clean         - Clean build files"
	@echo "  make build         - Build distribution package"
	@echo "  make upload        - Upload to private PyPI"

install:
	pip install -e .

install-dev:
	pip install -e ".[dev]"

test:
	pytest

test-cov:
	pytest --cov=src --cov-report=term-missing --cov-report=html --cov-report=xml

lint:
	ruff check src tests
	mypy src
	black --check src tests

format:
	black src tests
	ruff check --fix src tests

clean:
	rm -rf build dist *.egg-info .pytest_cache .coverage htmlcov coverage.xml .cache

build:
	python -m build

upload:
	twine upload --repository private dist/*
