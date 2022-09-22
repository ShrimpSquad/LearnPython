from dice import Dice

class Player:
    def __init__(self,name,counter) -> None:
        self.name = name
        self.counter = counter
        self.die = Dice() # Give a player their own die for play