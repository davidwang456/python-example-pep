# Usage Examples

This document demonstrates how to use the various modules of the project.

> **Note**: This project uses a multi-directory module structure, with each module in a separate directory.

## Example Module (example)

```python
from python_example_pep import example

# Greeting
print(example.hello())  # Hello, World!
print(example.hello("Python"))  # Hello, Python!

# Simple calculation
result = example.add(2, 3)
print(result)  # 5
```

## Utility Functions Module (utils)

```python
from python_example_pep import utils
from pathlib import Path

# Ensure directory exists
dir_path = utils.ensure_dir("./logs/app")
print(dir_path)  # Path object

# Get file size
try:
    size = utils.get_file_size("README.md")
    print(f"File size: {size} bytes")
except FileNotFoundError:
    print("File not found")

# Split path
parts = utils.split_path("/usr/local/bin")
print(parts)  # ['usr', 'local', 'bin']

# Normalize path
normalized = utils.normalize_path("./src")
print(normalized)  # Absolute path

# Join paths
joined = utils.join_paths("usr", "local", "bin")
print(joined)  # 'usr/local/bin'
```

## Data Validation Module (validators)

```python
from python_example_pep import validators

# Validate email
if validators.validate_email("user@example.com"):
    print("Email format is correct")

# Validate phone number
if validators.validate_phone("13800138000"):
    print("Phone number format is correct")

# Validate URL
if validators.validate_url("https://www.example.com"):
    print("URL format is correct")

# Validate string length
if validators.validate_length("hello", min_length=3, max_length=10):
    print("Length meets requirements")

# Validate numeric range
if validators.validate_range(5.0, 0.0, 10.0):
    print("Value is within range")
```

## Calculator Module (calculator)

```python
from python_example_pep import calculator

# Use calculator class
calc = calculator.Calculator()

# Basic operations
result1 = calc.add(2, 3)  # 5
result2 = calc.subtract(5, 3)  # 2
result3 = calc.multiply(2, 3)  # 6
result4 = calc.divide(6, 2)  # 3.0
result5 = calc.power(2, 3)  # 8

# View calculation history
history = calc.get_history()
for entry in history:
    print(entry)

# Clear history
calc.clear_history()

# Use utility functions
numbers = [1, 2, 3, 4, 5]
total = calculator.calculate_sum(numbers)  # 15
average = calculator.calculate_average(numbers)  # 3.0
```

## Logging Module (logger)

```python
from python_example_pep import logger

# Create logger
log = logger.Logger("my_app", level=logger.LogLevel.INFO)

# Log different levels
log.debug("This is debug information")
log.info("This is info")
log.warning("This is a warning")
log.error("This is an error")
log.critical("This is a critical error")

# Change log level
log.set_level(logger.LogLevel.DEBUG)

# Use file logging
file_logger = logger.Logger(
    "file_app",
    level=logger.LogLevel.INFO,
    log_file="./logs/app.log"
)
file_logger.info("This log will be written to file")

# Use convenience function
app_logger = logger.get_logger("app", level=logger.LogLevel.DEBUG)
app_logger.info("Application started")
```

## Complete Example

```python
from python_example_pep import calculator, logger, validators

# Create logger
log = logger.get_logger("calculator_app")

# Validate input
user_email = "user@example.com"
if not validators.validate_email(user_email):
    log.error(f"Invalid email: {user_email}")
    exit(1)

log.info(f"User email validated: {user_email}")

# Use calculator
calc = calculator.Calculator()
try:
    result = calc.divide(10, 2)
    log.info(f"Calculation result: {result}")
except ZeroDivisionError:
    log.error("Divisor cannot be 0")

# Display calculation history
log.info("Calculation history:")
for entry in calc.get_history():
    log.info(f"  {entry}")
```
