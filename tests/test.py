import pytest
from app.calc import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_sum_ok(self):
        assert self.calc.sum(self, 1, 1) == 2

    def test_sum_fail(self):
        assert self.calc.sum(self, 1, 1) == 3

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self, 1, 0)

    def test_multiply(self):
        assert self.calc.multiply(self, 2, 3) == 6

    def test_division(self):
        assert self.calc.division(self,10, 5) == 2

    def test_subtraction(self):
        assert self.calc.subtraction(self, 5, 2) == 3

    def test_power(self):
        assert self.calc.power(self, 5, 2) == 25

    def teardown(self):
        print("The End")
