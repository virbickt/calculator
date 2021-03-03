import pytest


def test_subtract():
    calculator = Calculator()
    calculator.add(5)
    result = calculator.substract(2)
    assert result == 3
