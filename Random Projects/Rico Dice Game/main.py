import random

class Die:

    def __init__(self):
        self.sides = [1, 2, 3, 4, 5, 6]


class Player:

    def __init__(self, name, die):
        self.name = name
        self.lives = 10
        self.die = die


class Brain:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def roll(self):

        p1_roll  = random.choice(p1.die.sides)
        p2_roll = random.choice(p2.die.sides)

        if p1_roll == p2_roll:
            print(f"{p1.name} rolls: {p1_roll}\n{p2.name} rolls: {p2_roll}")
            print("!!! It's a tie !!!")
        elif p1_roll > p2_roll:
            print(f"{p1.name} rolls: {p1_roll}\n{p2.name} rolls: {p2_roll}")
            p2.lives -= 1
            print("!!! Player 1 rolls higher !!!")
        elif p1_roll < p2_roll:
            print(f"{p1.name} rolls: {p1_roll}\n{p2.name} rolls: {p2_roll}")
            p1.lives -= 1
            print("!!! Player 2 roll highers !!!")
    
    def view_lives(self):
        print(f"{p1.name} lives left: {p1.lives}\n{p2.name} lives left: {p2.lives}")

while True:
    while True:

        print("===============================\nWelcome to Roll Dice game thing\n===============================")
        p1_die, p2_die = Die(), Die()
        p1, p2 = Player(input("What is your name: "), p1_die), Player("Computer", p1_die)
        brain = Brain(p1, p2)
        input("Any letter to start: ")
        print("==========GAME BEGINS==========")

        brain.roll()
        brain.view_lives()
        next_round = input("Any letter for next round / r to restart: ")
        if next_round == "r":
            print("gameover")
            break

        while True:
            print("------------New Round------------")
            brain.roll()
            brain.view_lives()

            if p1.lives == 0:
                winner = p2.lives - p1.lives
                print(f"Game over! {p2.name} Win by {winner} lives")
                input("Press a key to restart")
                break
            elif p2.lives == 0:
                winner = p1.lives - p2.lives
                print(f"Game over! {p2.name} Win by {winner} lives")
                input("Press a key to restart")
                break
            else:
                pass

            next_round = input("Any letter for next round / r to restart: ")
            if next_round == "r":
                print("Gameover")
                break