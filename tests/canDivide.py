!pip install pytest ipython_pytest
import ipython_pytest
%load_ext ipython_pytest

%%pytest

def canDivide():
    calculator = Calculator
    result = calculator.divide(6, 3)
    assert result == 2
