"""计算器模块的测试。"""

import pytest

from python_example_pep import calculator


class TestCalculator:
    """测试 Calculator 类。"""

    def setup_method(self):
        """每个测试方法前的设置。"""
        self.calc = calculator.Calculator()

    def test_add(self):
        """测试加法。"""
        assert self.calc.add(2, 3) == 5
        assert self.calc.add(-1, 1) == 0
        assert self.calc.add(0, 0) == 0
        assert self.calc.add(2.5, 3.5) == 6.0

    def test_subtract(self):
        """测试减法。"""
        assert self.calc.subtract(5, 3) == 2
        assert self.calc.subtract(0, 5) == -5
        assert self.calc.subtract(10.5, 3.5) == 7.0

    def test_multiply(self):
        """测试乘法。"""
        assert self.calc.multiply(2, 3) == 6
        assert self.calc.multiply(0, 5) == 0
        assert self.calc.multiply(-2, 3) == -6
        assert self.calc.multiply(2.5, 2) == 5.0

    def test_divide(self):
        """测试除法。"""
        assert self.calc.divide(6, 2) == 3.0
        assert self.calc.divide(5, 2) == 2.5
        assert self.calc.divide(-6, 2) == -3.0

    def test_divide_by_zero(self):
        """测试除以零。"""
        with pytest.raises(ZeroDivisionError):
            self.calc.divide(5, 0)

    def test_power(self):
        """测试幂运算。"""
        assert self.calc.power(2, 3) == 8
        assert self.calc.power(5, 0) == 1
        assert self.calc.power(2, -1) == 0.5

    def test_history(self):
        """测试计算历史。"""
        self.calc.add(1, 2)
        self.calc.subtract(5, 3)
        history = self.calc.get_history()
        assert len(history) == 2
        assert "1 + 2 = 3" in history
        assert "5 - 3 = 2" in history

    def test_clear_history(self):
        """测试清空历史。"""
        self.calc.add(1, 2)
        self.calc.clear_history()
        assert len(self.calc.get_history()) == 0

    def test_history_is_copy(self):
        """测试历史记录是副本。"""
        self.calc.add(1, 2)
        history1 = self.calc.get_history()
        self.calc.add(3, 4)
        history2 = self.calc.get_history()
        assert len(history1) == 1
        assert len(history2) == 2


class TestCalculateSum:
    """测试 calculate_sum 函数。"""

    def test_sum_integers(self):
        """测试整数列表求和。"""
        assert calculator.calculate_sum([1, 2, 3, 4]) == 10

    def test_sum_floats(self):
        """测试浮点数列表求和。"""
        assert calculator.calculate_sum([1.5, 2.5, 3.0]) == 7.0

    def test_sum_mixed(self):
        """测试混合类型列表求和。"""
        assert calculator.calculate_sum([1, 2.5, 3]) == 6.5

    def test_sum_empty(self):
        """测试空列表求和。"""
        assert calculator.calculate_sum([]) == 0

    def test_sum_single(self):
        """测试单个元素列表求和。"""
        assert calculator.calculate_sum([5]) == 5


class TestCalculateAverage:
    """测试 calculate_average 函数。"""

    def test_average_integers(self):
        """测试整数列表平均值。"""
        assert calculator.calculate_average([1, 2, 3, 4]) == 2.5

    def test_average_floats(self):
        """测试浮点数列表平均值。"""
        assert calculator.calculate_average([1.0, 2.0, 3.0]) == 2.0

    def test_average_single(self):
        """测试单个元素列表平均值。"""
        assert calculator.calculate_average([5]) == 5.0

    def test_average_empty(self):
        """测试空列表平均值。"""
        with pytest.raises(ValueError):
            calculator.calculate_average([])

