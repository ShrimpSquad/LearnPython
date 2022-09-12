import random
from data import deck

class Player():
    def __init__(self, name: str) -> None:
        self.cards = [random.choice(list(deck.values())), random.choice(list(deck.values()))]
        self.name = name

    def hit(self):
        total = sum(self.cards)
        new_card = random.choice(list(deck.values()))
        self.cards.append(new_card)
        print(f"Your new card is worth {new_card} points, for a total of {sum(self.cards)}")

    def bust_check(self) -> str:
        total = sum(self.cards)
        if total < 22 and 11 in self.cards:
            total -= 10
            print("It's bussin'")
        
        elif total > 21:
            print(f"{self.name} says: Oh fuck, I busted!")
            return False
        
        else:
            print("It do be bussin' doe")

    def compare_cards(self, player_cards: list, player_name: str) -> bool:
        if sum(self.cards) >= sum(player_cards) and sum(self.cards) <= 21:
            print(f"dealer cards:{self.cards}, for a total of {sum(self.cards)}")
            print(f"player cards:{player_cards}, for a total of {sum(player_cards)}")
            print("Dealer wins")
        elif sum(self.cards) < sum(player_cards) and sum(player_cards) <=21:
            print(f"dealer cards:{self.cards}, for a total of {sum(self.cards)}")
            print(f"player cards:{player_cards}, for a total of {sum(player_cards)}")
            print(f"{player_name} wins!")
        elif (sum(self.cards) < sum(player_cards)) and sum(player_cards) > 21:
            print(f"dealer cards:{self.cards}, for a total of {sum(self.cards)}")
            print(f"player cards:{player_cards}, for a total of {sum(player_cards)}")
            print(f"{player_name} busts! Dealer wins!")
        else:
            print(f"dealer cards:{self.cards}, for a total of {sum(self.cards)}")
            print(f"player cards:{player_cards}, for a total of {sum(player_cards)}")
            print(f"Dealer busts! {player_name} wins!")


    def hit_again(self):
        keep_asking = True
        while keep_asking:
            hit_again = input("Hit again? Y or N ").lower()
            if hit_again == "y":
                return True
            elif hit_again == "n":
                return False
            else:
                print("I didn't get that, try again")
                continue