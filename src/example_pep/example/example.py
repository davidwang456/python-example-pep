"""Example module demonstrating basic project functionality."""


def hello(name: str = "World") -> str:
    """
    Return a greeting message.

    Args:
        name: Name to greet, defaults to "World"

    Returns:
        Greeting string

    Examples:
        >>> hello()
        'Hello, World!'
        >>> hello("Python")
        'Hello, Python!'
    """
    return f"Hello, {name}!"


def add(a: int, b: int) -> int:
    """
    Add two integers.

    Args:
        a: First integer
        b: Second integer

    Returns:
        Sum of the two integers

    Examples:
        >>> add(2, 3)
        5
    """
    return a + b

