import random

class Dice:
    def __init__(self, sides = ["1","2","3","5","6"]) -> None:
        self.sides = sides
        
    # Rolls dice and returns value of side
    def roll(self):
        return random.choice(self.sides)