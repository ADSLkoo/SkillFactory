import pytest
from calculator import Calculator

class TestCalculator:
    def setup_method(self):
        self.calc = Calculator()

    def test_multiply(self):
        result = self.calc.multiply(2, 3)
        assert result == 6

    def test_division(self):
        result = self.calc.division(10, 2)
        assert result == 5.0

    def test_subtraction(self):
        result = self.calc.subtraction(5, 3)
        assert result == 2

    def test_adding(self):
        result = self.calc.adding(4, 6)
        assert result == 10