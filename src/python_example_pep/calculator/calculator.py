"""计算器模块。"""

from typing import List, Union


class Calculator:
    """简单计算器类。"""

    def __init__(self):
        """初始化计算器。"""
        self.history: List[str] = []

    def add(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """
        加法运算。

        Args:
            a: 第一个数
            b: 第二个数

        Returns:
            两数之和

        Examples:
            >>> calc = Calculator()
            >>> calc.add(2, 3)
            5
        """
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result

    def subtract(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """
        减法运算。

        Args:
            a: 被减数
            b: 减数

        Returns:
            两数之差

        Examples:
            >>> calc = Calculator()
            >>> calc.subtract(5, 3)
            2
        """
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result

    def multiply(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """
        乘法运算。

        Args:
            a: 第一个数
            b: 第二个数

        Returns:
            两数之积

        Examples:
            >>> calc = Calculator()
            >>> calc.multiply(2, 3)
            6
        """
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result

    def divide(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """
        除法运算。

        Args:
            a: 被除数
            b: 除数

        Returns:
            两数之商

        Raises:
            ZeroDivisionError: 如果除数为 0

        Examples:
            >>> calc = Calculator()
            >>> calc.divide(6, 2)
            3.0
        """
        if b == 0:
            raise ZeroDivisionError("除数不能为 0")
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result

    def power(self, base: Union[int, float], exponent: Union[int, float]) -> Union[int, float]:
        """
        幂运算。

        Args:
            base: 底数
            exponent: 指数

        Returns:
            幂运算结果

        Examples:
            >>> calc = Calculator()
            >>> calc.power(2, 3)
            8
        """
        result = base ** exponent
        self.history.append(f"{base} ** {exponent} = {result}")
        return result

    def clear_history(self) -> None:
        """清空计算历史。"""
        self.history.clear()

    def get_history(self) -> List[str]:
        """
        获取计算历史。

        Returns:
            计算历史记录列表
        """
        return self.history.copy()


def calculate_sum(numbers: List[Union[int, float]]) -> Union[int, float]:
    """
    计算列表中所有数字的和。

    Args:
        numbers: 数字列表

    Returns:
        所有数字的和

    Examples:
        >>> calculate_sum([1, 2, 3, 4])
        10
    """
    return sum(numbers)


def calculate_average(numbers: List[Union[int, float]]) -> float:
    """
    计算列表中所有数字的平均值。

    Args:
        numbers: 数字列表

    Returns:
        平均值

    Raises:
        ValueError: 如果列表为空

    Examples:
        >>> calculate_average([1, 2, 3, 4])
        2.5
    """
    if not numbers:
        raise ValueError("列表不能为空")
    return sum(numbers) / len(numbers)

