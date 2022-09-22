from dicegame import DiceGame
game_on = True
while game_on:
    game = DiceGame() # Create a game instance
    game.start_game() # Begin game
    game_over = False
    while not game_over: # Loop rounds until a winner has been decided
        game.start_round()
        if game.check_winner():
            game_over = True
    print("Game over! Thank you for playing!") # Game ended, say goodbye
    exit()