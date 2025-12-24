"""数据验证模块。"""

import re
from typing import Optional


class ValidationError(Exception):
    """验证错误异常。"""

    pass


def validate_email(email: str) -> bool:
    """
    验证邮箱地址格式。

    Args:
        email: 邮箱地址

    Returns:
        如果格式正确返回 True，否则返回 False

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
    验证手机号码格式（支持中国大陆11位手机号）。

    Args:
        phone: 手机号码

    Returns:
        如果格式正确返回 True，否则返回 False

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
    验证 URL 格式。

    Args:
        url: URL 地址

    Returns:
        如果格式正确返回 True，否则返回 False

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
    验证字符串长度。

    Args:
        text: 要验证的字符串
        min_length: 最小长度
        max_length: 最大长度（None 表示无限制）

    Returns:
        如果长度符合要求返回 True，否则返回 False

    Raises:
        ValueError: 如果 min_length < 0 或 max_length < min_length

    Examples:
        >>> validate_length("hello", min_length=3, max_length=10)
        True
        >>> validate_length("hi", min_length=3)
        False
    """
    if min_length < 0:
        raise ValueError("min_length 不能小于 0")
    if max_length is not None and max_length < min_length:
        raise ValueError("max_length 不能小于 min_length")

    length = len(text)
    if length < min_length:
        return False
    if max_length is not None and length > max_length:
        return False
    return True


def validate_range(value: float, min_value: float, max_value: float) -> bool:
    """
    验证数值是否在指定范围内。

    Args:
        value: 要验证的数值
        min_value: 最小值
        max_value: 最大值

    Returns:
        如果值在范围内返回 True，否则返回 False

    Raises:
        ValueError: 如果 min_value > max_value

    Examples:
        >>> validate_range(5.0, 0.0, 10.0)
        True
        >>> validate_range(15.0, 0.0, 10.0)
        False
    """
    if min_value > max_value:
        raise ValueError("min_value 不能大于 max_value")
    return min_value <= value <= max_value

