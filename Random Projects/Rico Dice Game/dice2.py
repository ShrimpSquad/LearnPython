import random


class Dice:

    def __init__(self):
        self.sides = [1,2,3,4,5,6]
        
    def roll(self):
        return random.choice(self.sides)

class Player:

    def __init__(self,name,dice):
        self.name = name
        self.lives = 10
        self.dice = dice

    def minus(self):
        self.lives -= 1

    def roll_dice(self):
        return self.dice.roll()


dice = Dice()
player1 = Player("rico", dice)
player2 = Player("computer", dice)


print(player1.dice.roll())
print(player2.dice.roll())