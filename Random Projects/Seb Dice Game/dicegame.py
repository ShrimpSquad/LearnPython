# from player import Player
# from dice import Dice
from player import Player
from dice import Dice
import time # Add short delay between rounds for user experience
    
class DiceGame:
    def __init__(self) -> None:
        self.human = Player(input("What is your name? "), 10) # Only human player inputs their name
        self.human_die = Dice()
        self.computer = Player("Computer", 10)
        self.computer_die = Dice()

    # Starts the game with an introduction
    def start_game(self):
        print("🎲 Welcome to the dice game! 🎲")
        time.sleep(.5)
        
    # Starts a new round
    def start_round(self):
        print("\n------------ NEW ROUND ------------\n")
        print(f"The current score is {self.human.counter} for {self.human.name}, and {self.computer.counter} for {self.computer.name}\n")
        roll = input("\n🎲 Time to roll! Press enter to roll 🎲\n")
        
        # In case user wants to end game early
        if roll == "off":
            print("Game manually stopped. Goodbye!")
            exit()
        time.sleep(.25)

        human_roll = int(self.human.die.roll())
        computer_roll = int(self.human_die.roll())
        print(f"{self.human.name} rolled {human_roll}!\n{self.computer.name} rolled {computer_roll}!")

        # Outcome of roll comparison
        if human_roll < computer_roll:
            self.human.counter -= 1
            #self.computer.counter += 1
            print(f"{self.computer.name} rolled higher!")
            self.check_winner(human_roll,computer_roll)

        elif human_roll > computer_roll:
            #self.human.counter += 1
            self.computer.counter -= 1
            print(f"{self.human.name} rolled higher!")
            self.check_winner(human_roll,computer_roll)

        else:
            print("It's a draw... let's go again!")

    # At the end of each round, check if a winner has been decided
    def check_winner(self, *args):
        if self.human.counter == 0:
            print(f"{self.human.name} wins the game!")
            return True
        elif self.computer.counter == 0:
            print(f"{self.computer.name} wins the game!")
            return True
        else:
            pass