from math import sqrt


class Calculator:

    def __init__(self, state: float = 0):
        if not isinstance(state, (int, float)):
            raise TypeError
        self._state = state

    @property
    def state(self) -> float:
        return self.__state

    def add(self, number: float) -> float:
        self.__state += number
        return self.__state

    def subtract(self, number: float) -> float:
        self.__state -= number
        return self.__state

    def multiply(self, number: float) -> float:
        self.__state *= number
        return self.__state

    def divide(self, number: float) -> float:
        if number == 0:
            raise ZeroDivisionError
        self.__state /= number
        return self.__state

    def sqrt(self) -> float:
        self.__state = sqrt(self.__state)
        return self.__state
