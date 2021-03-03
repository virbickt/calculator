import pytest


def test_sum():
    calculator = Calculator()
    result = calculator.add(2)
    assert result == 2
