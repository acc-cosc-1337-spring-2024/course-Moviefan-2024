import random

class Die:
    def roll(self):
        self._roll_value = random.randint(1, 6)

    def get_rolled_value(self):
        return self._roll_value

    def __str__(self):
        return f"The rolled value is {self._roll_value}"

    # Private data member
    _roll_value = None
