from math import sqrt


class Calculator:
    """
    The calculator is able to perform addition, subtraction,
     multiplication, division, square root and reset its memory.
    Consult the docstring of each method individually for more information.
    """

    def __init__(self, state: float = 0):
        """
        Calculator only accepts objects of type float or int as input; TypeError is raised otherwise
        """
        if not isinstance(state, (int, float)):
            raise TypeError
        self.__state = state

    @property
    def state(self) -> float:
        return self.__state

    def add(self, number: float) -> float:
        """
        Adds the input value to the initial state and returns the result.
        """
        self.__state += number
        return self.__state

    def subtract(self, number: float) -> float:
        """
        Subtracts the input value from the value stored in the memory state and returns the result.
        """
        self.__state -= number
        return self.__state

    def multiply(self, number: float) -> float:
        """Multiplies the input value by the value stored in the memory state and returns the result."""
        self.__state *= number
        return self.__state

    def divide(self, number: float) -> float:
        """
        Divides the value stored in the memory state by the input value.
        Note that the input value must not be equal to 0; ZeroDivisionError is raised otherwise
        """
        if number == 0:
            raise ZeroDivisionError
        self.__state /= number
        return self.__state

    def sqrt(self) -> float:
        """Takes the square root of the value stored in the memory state
        using math.sqrt and returns the result."""
        self.__state = sqrt(self.__state)
        return self.__state

    def reset(self):
        """Sets the value stored in the memory state to 0"""
        self.__state = 0
