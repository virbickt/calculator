class Calculator:
    def __init__(self, state: float = 0):
        self.__state = state

    @property
    def state(self) -> float:
        return self.__state
