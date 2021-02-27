!pip install pytest ipython_pytest
import ipython_pytest
%load_ext ipython_pytest

%%pytest

def canSubstract():
    calculator = Calculator
    result = calculator.substract(5, 2)
    assert result == 3
