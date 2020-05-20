from random import randint

class Die:
    """Represents a single die"""

    def __init__(self, num_sides=6):
        """Six sided"""
        self.num_sides = num_sides

    def roll (self):
        """Random value between 1 and number of sides"""
        return randint(1,self.num_sides)
