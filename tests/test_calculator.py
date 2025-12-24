"""Tests for calculator module."""

import pytest

from python_example_pep import calculator


class TestCalculator:
    """Tests for Calculator class."""

    def setup_method(self):
        """Setup before each test method."""
        self.calc = calculator.Calculator()

    def test_add(self):
        """Test addition."""
        assert self.calc.add(2, 3) == 5
        assert self.calc.add(-1, 1) == 0
        assert self.calc.add(0, 0) == 0
        assert self.calc.add(2.5, 3.5) == 6.0

    def test_subtract(self):
        """Test subtraction."""
        assert self.calc.subtract(5, 3) == 2
        assert self.calc.subtract(0, 5) == -5
        assert self.calc.subtract(10.5, 3.5) == 7.0

    def test_multiply(self):
        """Test multiplication."""
        assert self.calc.multiply(2, 3) == 6
        assert self.calc.multiply(0, 5) == 0
        assert self.calc.multiply(-2, 3) == -6
        assert self.calc.multiply(2.5, 2) == 5.0

    def test_divide(self):
        """Test division."""
        assert self.calc.divide(6, 2) == 3.0
        assert self.calc.divide(5, 2) == 2.5
        assert self.calc.divide(-6, 2) == -3.0

    def test_divide_by_zero(self):
        """Test division by zero."""
        with pytest.raises(ZeroDivisionError):
            self.calc.divide(5, 0)

    def test_power(self):
        """Test power operation."""
        assert self.calc.power(2, 3) == 8
        assert self.calc.power(5, 0) == 1
        assert self.calc.power(2, -1) == 0.5

    def test_history(self):
        """Test calculation history."""
        self.calc.add(1, 2)
        self.calc.subtract(5, 3)
        history = self.calc.get_history()
        assert len(history) == 2
        assert "1 + 2 = 3" in history
        assert "5 - 3 = 2" in history

    def test_clear_history(self):
        """Test clearing history."""
        self.calc.add(1, 2)
        self.calc.clear_history()
        assert len(self.calc.get_history()) == 0

    def test_history_is_copy(self):
        """Test that history is a copy."""
        self.calc.add(1, 2)
        history1 = self.calc.get_history()
        self.calc.add(3, 4)
        history2 = self.calc.get_history()
        assert len(history1) == 1
        assert len(history2) == 2


class TestCalculateSum:
    """Tests for calculate_sum function."""

    def test_sum_integers(self):
        """Test summing integer list."""
        assert calculator.calculate_sum([1, 2, 3, 4]) == 10

    def test_sum_floats(self):
        """Test summing float list."""
        assert calculator.calculate_sum([1.5, 2.5, 3.0]) == 7.0

    def test_sum_mixed(self):
        """Test summing mixed type list."""
        assert calculator.calculate_sum([1, 2.5, 3]) == 6.5

    def test_sum_empty(self):
        """Test summing empty list."""
        assert calculator.calculate_sum([]) == 0

    def test_sum_single(self):
        """Test summing single element list."""
        assert calculator.calculate_sum([5]) == 5


class TestCalculateAverage:
    """Tests for calculate_average function."""

    def test_average_integers(self):
        """Test averaging integer list."""
        assert calculator.calculate_average([1, 2, 3, 4]) == 2.5

    def test_average_floats(self):
        """Test averaging float list."""
        assert calculator.calculate_average([1.0, 2.0, 3.0]) == 2.0

    def test_average_single(self):
        """Test averaging single element list."""
        assert calculator.calculate_average([5]) == 5.0

    def test_average_empty(self):
        """Test averaging empty list."""
        with pytest.raises(ValueError):
            calculator.calculate_average([])
