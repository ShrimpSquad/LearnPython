# Create a game of blackjack using Object Oriented Programming
import random
from classes import Player

def blackjack():
    dealer = Player("Dealer")
    player1 = Player(input("What is your name? "))
    hitting = True
    print(f"Dealer's first card is {dealer.cards[0]}")
    hit_again = input("Would you like to hit? Y or N ").lower()
    while hitting:
        if hit_again == "y":
            player1.hit()
            if player1.bust_check() == False:
                hitting = False
                break
            if player1.hit_again() == False:
                hitting = False
                break
        elif hit_again == "n":
            hitting = False
        else:
            print("I didn't get that. Try again.")
    dealer.compare_cards(player1.cards, player1.name)
    play_check = True
    while play_check:
        play_again = input("Play again? Y or N ").lower()
        if play_again == "y":
            blackjack()
        elif play_again == "n":
            print("Goodbye!"), exit()
        else:
            print("I didn't quite get that...")
            continue
blackjack()