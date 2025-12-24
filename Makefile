.PHONY: help install install-dev test test-cov lint format clean build upload

help:
	@echo "可用的命令:"
	@echo "  make install       - 安装项目"
	@echo "  make install-dev   - 安装开发依赖"
	@echo "  make test          - 运行测试"
	@echo "  make test-cov      - 运行测试并生成覆盖率报告"
	@echo "  make lint          - 代码检查"
	@echo "  make format        - 代码格式化"
	@echo "  make clean         - 清理构建文件"
	@echo "  make build         - 构建分发包"
	@echo "  make upload        - 上传到 PyPI 私库"

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

