!pip install pytest ipython_pytest
import ipython_pytest
%load_ext ipython_pytest

%%pytest

def canMultiply():
    calculator = Calculator
    result = calculator.multiply(2, 3)
    assert result == 6
