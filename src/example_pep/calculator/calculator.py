"""Calculator module."""

from typing import List, Union


class Calculator:
    """Simple calculator class."""

    def __init__(self):
        """Initialize calculator."""
        self.history: List[str] = []

    def add(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """
        Addition operation.

        Args:
            a: First number
            b: Second number

        Returns:
            Sum of the two numbers

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
        Subtraction operation.

        Args:
            a: Minuend
            b: Subtrahend

        Returns:
            Difference of the two numbers

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
        Multiplication operation.

        Args:
            a: First number
            b: Second number

        Returns:
            Product of the two numbers

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
        Division operation.

        Args:
            a: Dividend
            b: Divisor

        Returns:
            Quotient of the two numbers

        Raises:
            ZeroDivisionError: If divisor is 0

        Examples:
            >>> calc = Calculator()
            >>> calc.divide(6, 2)
            3.0
        """
        if b == 0:
            raise ZeroDivisionError("Divisor cannot be 0")
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result

    def power(self, base: Union[int, float], exponent: Union[int, float]) -> Union[int, float]:
        """
        Power operation.

        Args:
            base: Base number
            exponent: Exponent

        Returns:
            Result of power operation

        Examples:
            >>> calc = Calculator()
            >>> calc.power(2, 3)
            8
        """
        result = base ** exponent
        self.history.append(f"{base} ** {exponent} = {result}")
        return result

    def clear_history(self) -> None:
        """Clear calculation history."""
        self.history.clear()

    def get_history(self) -> List[str]:
        """
        Get calculation history.

        Returns:
            List of calculation history records
        """
        return self.history.copy()


def calculate_sum(numbers: List[Union[int, float]]) -> Union[int, float]:
    """
    Calculate sum of all numbers in a list.

    Args:
        numbers: List of numbers

    Returns:
        Sum of all numbers

    Examples:
        >>> calculate_sum([1, 2, 3, 4])
        10
    """
    return sum(numbers)


def calculate_average(numbers: List[Union[int, float]]) -> float:
    """
    Calculate average of all numbers in a list.

    Args:
        numbers: List of numbers

    Returns:
        Average value

    Raises:
        ValueError: If list is empty

    Examples:
        >>> calculate_average([1, 2, 3, 4])
        2.5
    """
    if not numbers:
        raise ValueError("List cannot be empty")
    return sum(numbers) / len(numbers)

