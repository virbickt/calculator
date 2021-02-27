!pip install pytest ipython_pytest
import ipython_pytest
%load_ext ipython_pytest

%%pytest

def canAdd():
    calculator = Calculator
    result = calculator.add(1, 2)
    assert result == 3
