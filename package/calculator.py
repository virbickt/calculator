from math import sqrt


class Calculator:

    def __init__(self, state: float = 0):
        if not isinstance(state, (int, float)):
            raise TypeError
        self._state = state

    @property
    def state(self) -> float:
        return self.__state
