!pip install pytest ipython_pytest
import ipython_pytest
%load_ext ipython_pytest

%%pytest

def canSqrt():
    calculator = Calculator
    result = calculator.sqrt
    assert result == 2
