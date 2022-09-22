import random

class Die:

    def __init__(self):
        self.roll = [1, 2, 3, 4, 5, 6]


class Player:

    def __init__(self,name,die):
        self.name = name
        self.lives = 10
        self.die = die


class Brain:

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def start(self):
        print("===============================\nWelcome to Roll Dice game thing\n===============================")

    def round(self):
        print("------New Round------")

    def gameplay(self):
        
        player1_roll = random.choice(player1.die.roll)
        player2_roll = random.choice(player2.die.roll)
        if player1_roll == player2_roll:
            print("it's a tie")
        elif player1_roll > player2_roll:
            player2.lives -= 1
            print("Player 1 Wins")
        elif player1_roll < player2_roll:
            player1.lives -= 1
            print("Player 2 Wins")


die = Die()
die2 = Die()
player1 = Player("Rico", die)
player2 = Player("Computer", die2)
brain = Brain(player1, player2)


next_round = ""
brain.start()
still_on = True

while still_on == True:

    if next_round != "s":

        brain.round()
        next_round = input("Any key for next round or s to finsh: ")
        brain.gameplay()
        print(f"Player 1 lives: {brain.player1.lives}")
        print(f"Player 2 lives: {brain.player2.lives}")

        if brain.player1.lives == 0:
            print("game over player 2 wins")
            still_on = False
        elif brain.player2.lives == 0:
            print("game over player 2 wins")
            still_on = False
    else:
        still_on = False