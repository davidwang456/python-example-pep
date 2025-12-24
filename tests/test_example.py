"""示例模块的测试。"""

import pytest
from python_example_pep import example


def test_hello_default():
    """测试 hello 函数的默认行为。"""
    assert example.hello() == "Hello, World!"


def test_hello_with_name():
    """测试 hello 函数带参数的情况。"""
    assert example.hello("Python") == "Hello, Python!"


def test_add():
    """测试 add 函数。"""
    assert example.add(2, 3) == 5
    assert example.add(-1, 1) == 0
    assert example.add(0, 0) == 0

