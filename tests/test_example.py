"""Tests for example module."""

import pytest
from python_example_pep import example


def test_hello_default():
    """Test default behavior of hello function."""
    assert example.hello() == "Hello, World!"


def test_hello_with_name():
    """Test hello function with parameter."""
    assert example.hello("Python") == "Hello, Python!"


def test_add():
    """Test add function."""
    assert example.add(2, 3) == 5
    assert example.add(-1, 1) == 0
    assert example.add(0, 0) == 0

