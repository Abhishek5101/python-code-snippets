import random


class Die:
    def __init__(self, sides=2, value=0):
        if not sides >= 2 or not isinstance(sides, int):
            raise ValueError("Sides should be a whole number greater than 2")
        self.value = value or random.randint(1, sides)
        if not isinstance(value, int):
            raise ValueError("Values need to be a whole number")

    def __int__(self):
        return self.value

    def __eq__(self, other):
        return int(self) == other

    def __ne__(self, other):
        return not int(self) == other

    def __gt__(self, other):
        return int(self) > other

    def __lt__(self, other):
        return int(self) < other

    def __ge__(self, other):
        return int(self) > other or int(self) == other

    def __le__(self, other):
        return int(self) <= other or int(self) == other

    def __add__(self, other):
        return int(self) + other

    def __radd__(self, other):
        return int(self) + other

class D6(Die):
    def __init__(self, value=0):
        super().__init__(sides=6, value=value)


d6 = D6()
print(int(d6))
