import pytest


def test_reset():
    calculator = Calculator()
    calculator.add(2)
    calculator.reset()
    state = calculator.state()
    assert state == 0
