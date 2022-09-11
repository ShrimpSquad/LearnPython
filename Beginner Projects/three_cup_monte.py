# Create a function that shuffles the ball in three cups

from random import shuffle

ball_location = ["___", "(O)", "___"]

def shuffle_cups(cups):
    shuffle(cups)
    return cups

def player_guess():
    guess = int(input("Which cup is the ball in? 1, 2, or 3? "))
    while guess not in (1, 2, 3):
        guess = int(input("I SAID CHOOSE 1, 2, or 3!!! TRY AGAIN!\nWhich cup? "))
    return guess

def guess_check(result, guess):
    if result[guess - 1] == "(O)":
        print("Correct! Well done")
    else:
        print("Wrong cup. Better luck next time")

# Game below
result = shuffle_cups(ball_location)
guess = player_guess()
guess_check(result, guess)