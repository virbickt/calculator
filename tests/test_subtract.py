import pytest


def test_subtracat():
    calculator = Calculator()
    calculator.add(5)
    result = calculator.substract(2)
    assert result == 3
