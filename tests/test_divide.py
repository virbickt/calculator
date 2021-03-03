import pytest


def test_divide():
    calculator = Calculator()
    calculator.add(6)
    result = calculator.divide(3)
    assert result == 2
    
def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        calculator = Calculator()
        calculator.divide(0)
