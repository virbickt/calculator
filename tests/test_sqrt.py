import pytest


def test_sqrt():
    calculator = Calculator()
    calculator.add(4)
    result = calculator.sqrt()
    assert result == 2
