"""示例模块，展示项目的基本功能。"""


def hello(name: str = "World") -> str:
    """
    返回一个问候语。

    Args:
        name: 要问候的名字，默认为 "World"

    Returns:
        问候语字符串

    Examples:
        >>> hello()
        'Hello, World!'
        >>> hello("Python")
        'Hello, Python!'
    """
    return f"Hello, {name}!"


def add(a: int, b: int) -> int:
    """
    两个整数相加。

    Args:
        a: 第一个整数
        b: 第二个整数

    Returns:
        两个整数的和

    Examples:
        >>> add(2, 3)
        5
    """
    return a + b

