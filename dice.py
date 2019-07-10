import random


class Die:
    def __init__(self, sides=2, value=0):
        if not sides >= 2 or not isinstance(sides, int):
            raise ValueError("Sides should be a whole number greater than 2")
        self.value = value or random.choice(1, sides)
        if not isinstance(value, int):
            raise ValueError("Values need to be a whole number")


class D6(Die):
    def __init__(self, value):
        super().__init__(sides=6, value=value)
