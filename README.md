# Python Example PEP

A modern Python project example following PEP 517/518/621 standards.

## Features

- ✅ Follows PEP 517/518/621 standards
- ✅ Uses `pyproject.toml` to manage project metadata and build configuration
- ✅ Uses `python -m build` for building (no dependency on setup.py)
- ✅ Uses `twine` to publish to private PyPI
- ✅ Multi-module project structure (utils, validators, calculator, logger, example)
- ✅ Complete unit test coverage (coverage requirement ≥80%)
- ✅ Includes GitHub Actions and GitLab CI configuration

## Project Structure

```
python-example-pep/
├── src/
│   └── example_pep/            # Main package
│       ├── __init__.py
│       ├── example/             # Example module (separate directory)
│       │   ├── __init__.py
│       │   └── example.py
│       ├── utils/               # Utility functions module (separate directory)
│       │   ├── __init__.py
│       │   └── utils.py
│       ├── validators/           # Data validation module (separate directory)
│       │   ├── __init__.py
│       │   └── validators.py
│       ├── calculator/           # Calculator module (separate directory)
│       │   ├── __init__.py
│       │   └── calculator.py
│       └── logger/               # Logging module (separate directory)
│           ├── __init__.py
│           └── logger.py
├── tests/                       # Test directory
│   ├── __init__.py
│   ├── test_example.py
│   ├── test_utils.py
│   ├── test_validators.py
│   ├── test_calculator.py
│   └── test_logger.py
├── .github/
│   └── workflows/
│       └── ci.yml              # GitHub Actions CI/CD
├── .gitlab-ci.yml              # GitLab CI/CD configuration
├── pyproject.toml              # PEP 621 project metadata and build configuration
├── README.md
├── USAGE.md                    # Usage examples documentation
├── .gitignore
├── .pypirc.example             # PyPI configuration example
├── Makefile                    # Convenient commands
└── verify_build.py             # Build verification script
```

## Module Description

### example - Example Module
Provides basic example functions including greetings and simple calculations.

### utils - Utility Functions Module
Provides utility functions for file path processing, directory management, etc.

### validators - Data Validation Module
Provides validation functions for email, phone number, URL, string length, numeric range, etc.

### calculator - Calculator Module
Provides a complete calculator class supporting addition, subtraction, multiplication, division, power operations, and calculation history.

### logger - Logging Module
Provides flexible logging functionality supporting console and file output with configurable log levels.

## Installation

### Install from Source

```bash
# Clone repository
git clone https://github.com/yourusername/python-example-pep.git
cd python-example-pep

# Install development dependencies
pip install -e ".[dev]"
```

## Development

### Run Tests

```bash
# Run all tests
pytest

# Run tests with coverage display
pytest --cov=src --cov-report=term-missing

# Generate HTML coverage report
pytest --cov=src --cov-report=html
# Then open htmlcov/index.html in browser
```

### Test Coverage

The project requires test coverage ≥80%. Coverage is automatically checked when running tests:

```bash
pytest
```

If coverage is below 80%, tests will fail. View detailed coverage reports:

```bash
# Terminal report
pytest --cov=src --cov-report=term-missing

# HTML report
pytest --cov=src --cov-report=html
open htmlcov/index.html  # macOS
xdg-open htmlcov/index.html  # Linux
start htmlcov/index.html  # Windows
```

### Code Formatting

```bash
black src tests
```

### Code Linting

```bash
ruff check src tests
mypy src
```

## Build

Use PEP 517 compatible build tools (**no setup.py**):

```bash
# Install build tool
pip install build

# Build distribution package (PEP 517 compliant)
python -m build
```

After building, the following will be generated in the `dist/` directory:
- `*.whl` (wheel file)
- `*.tar.gz` (source distribution package)

### Verify Build

Run verification script to ensure everything is working:

```bash
python verify_build.py
```

Or use Makefile:

```bash
make build
```

## Publish to Private PyPI

Use `twine` to upload to private PyPI (metadata from PEP 621 `pyproject.toml`):

```bash
# Install twine
pip install twine

# Method 1: Directly specify repository URL
twine upload --repository-url https://your-private-pypi.com/simple/ dist/*
```

### Configure Private PyPI

Method 2: Configure `~/.pypirc` file (copy `.pypirc.example` and modify):

```ini
[distutils]
index-servers =
    private

[private]
repository = https://your-private-pypi.com/simple/
username = your_username
password = your_password
```

Then use:

```bash
twine upload --repository private dist/*
```

Or use Makefile:

```bash
make upload
```

### Environment Variables

Method 3: Use environment variables (recommended for CI/CD):

```bash
export TWINE_USERNAME=your_username
export TWINE_PASSWORD=your_password
export TWINE_REPOSITORY_URL=https://your-private-pypi.com/simple/
twine upload dist/*
```

## CI/CD

### GitHub Actions

The project includes GitHub Actions workflow configuration (`.github/workflows/ci.yml`), supporting:
- Multi Python version testing (3.8-3.12)
- Multi OS testing (Ubuntu, Windows, macOS)
- Automatic distribution package building
- Automatic publishing to private PyPI (optional)

### GitLab CI

The project includes GitLab CI configuration (`.gitlab-ci.yml`), containing the following stages:

1. **Test Stage** (`test`)
   - Multi Python version testing (3.8-3.12)
   - Code coverage check (requirement ≥80%)
   - Code quality check (ruff, mypy, black)

2. **Build Stage** (`build`)
   - Use `python -m build` to build distribution package
   - Generate wheel and source distribution packages

3. **Deploy Stage** (`deploy`)
   - Manually triggered publishing to private PyPI
   - Use `twine upload` to upload

#### GitLab CI Environment Variables Configuration

Configure the following CI/CD variables in GitLab project settings:

**For pip configuration (used during dependency installation):**
- `PIP_CONFIG_FILE`: (File type variable) Pip configuration file
  - **Variable type**: **File** (must be File type, not Variable type)
  - **How it works**: 
    - GitLab creates a temporary file with the content you upload
    - Sets `PIP_CONFIG_FILE` environment variable to the temporary file path
    - CI pipeline automatically copies this file to `$CI_PROJECT_DIR/pip.conf`
    - Pip uses the copied `pip.conf` file during the build process
  - **File format**: Should contain pip configuration in INI format (see `pip.conf.example`)
  - **Example content**:
    ```ini
    [global]
    index-url = https://username:password@pypi.my-company.com/simple
    extra-index-url = https://pypi.org/simple
    trusted-host = pypi.my-company.com
    ```

**For publishing to PyPI:**
- `PYPI_REPOSITORY_URL`: Private PyPI URL (e.g., `https://your-private-pypi.com/simple/`)
- `PYPI_USERNAME`: PyPI username
- `PYPI_PASSWORD`: PyPI password or token

**Configuration steps:**
1. Go to GitLab Project → Settings → CI/CD → Variables
2. Click "Add variable"
3. Set `PIP_CONFIG_FILE` as:
   - **Key**: `PIP_CONFIG_FILE`
   - **Type**: **File** (important! Select File type, not Variable type)
   - **Value**: Paste your pip configuration content (see `pip.conf.example`)
   - **Protected**: ✓ (recommended)
   - **Masked**: ✗ (File type variables cannot be masked)
4. Save the variable

**Note:** 
- The CI pipeline will automatically copy the file to `$CI_PROJECT_DIR/pip.conf` during each build
- If `PIP_CONFIG_FILE` is not set, pip will use default configuration
- The configuration file format should match `pip.conf.example`

## License

MIT License

## References

- [PEP 517](https://peps.python.org/pep-0517/) - Build System Interface
- [PEP 518](https://peps.python.org/pep-0518/) - Specifying Build Dependencies
- [PEP 621](https://peps.python.org/pep-0621/) - Project Metadata Standard


### Local pip Configuration (Optional)

For local development, you can create a `pip.conf` file (see `pip.conf.example`):

```ini
[global]
# Set default index URL to private PyPI
index-url = https://username:password@pypi.my-company.com/simple

# (Optional but recommended) Set official PyPI as fallback
# This way, if a package (like requests) is not found in private PyPI,
# pip will automatically search in the official PyPI
extra-index-url = https://pypi.org/simple

# (Optional but recommended) Set trusted host for private PyPI to avoid SSL warnings
trusted-host = pypi.my-company.com
```

Place this file at:
- Linux/macOS: `~/.pip/pip.conf` or `/etc/pip.conf`
- Windows: `%APPDATA%\pip\pip.ini` or `%PROGRAMDATA%\pip\pip.ini`

**Note:** In GitLab CI, the pip configuration is automatically created from CI/CD variables, so you don't need to commit this file.
