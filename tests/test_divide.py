import pytest


def canDivide():
    calculator = Calculator()
    calculator.add(6)
    result = calculator.divide(3)
    assert result == 2
