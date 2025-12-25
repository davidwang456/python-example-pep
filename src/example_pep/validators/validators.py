"""Data validation module."""

import re
from typing import Optional


class ValidationError(Exception):
    """Validation error exception."""

    pass


def validate_email(email: str) -> bool:
    """
    Validate email address format.

    Args:
        email: Email address

    Returns:
        True if format is correct, False otherwise

    Examples:
        >>> validate_email("test@example.com")
        True
        >>> validate_email("invalid-email")
        False
    """
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))


def validate_phone(phone: str) -> bool:
    """
    Validate phone number format (supports 11-digit Chinese mobile numbers).

    Args:
        phone: Phone number

    Returns:
        True if format is correct, False otherwise

    Examples:
        >>> validate_phone("13800138000")
        True
        >>> validate_phone("123456")
        False
    """
    pattern = r"^1[3-9]\d{9}$"
    return bool(re.match(pattern, phone))


def validate_url(url: str) -> bool:
    """
    Validate URL format.

    Args:
        url: URL address

    Returns:
        True if format is correct, False otherwise

    Examples:
        >>> validate_url("https://www.example.com")
        True
        >>> validate_url("not-a-url")
        False
    """
    pattern = r"^https?://[^\s/$.?#].[^\s]*$"
    return bool(re.match(pattern, url))


def validate_length(text: str, min_length: int = 0, max_length: Optional[int] = None) -> bool:
    """
    Validate string length.

    Args:
        text: String to validate
        min_length: Minimum length
        max_length: Maximum length (None means no limit)

    Returns:
        True if length meets requirements, False otherwise

    Raises:
        ValueError: If min_length < 0 or max_length < min_length

    Examples:
        >>> validate_length("hello", min_length=3, max_length=10)
        True
        >>> validate_length("hi", min_length=3)
        False
    """
    if min_length < 0:
        raise ValueError("min_length cannot be less than 0")
    if max_length is not None and max_length < min_length:
        raise ValueError("max_length cannot be less than min_length")

    length = len(text)
    if length < min_length:
        return False
    if max_length is not None and length > max_length:
        return False
    return True


def validate_range(value: float, min_value: float, max_value: float) -> bool:
    """
    Validate if value is within specified range.

    Args:
        value: Value to validate
        min_value: Minimum value
        max_value: Maximum value

    Returns:
        True if value is within range, False otherwise

    Raises:
        ValueError: If min_value > max_value

    Examples:
        >>> validate_range(5.0, 0.0, 10.0)
        True
        >>> validate_range(15.0, 0.0, 10.0)
        False
    """
    if min_value > max_value:
        raise ValueError("min_value cannot be greater than max_value")
    return min_value <= value <= max_value

