import GuessGame
import MemoryGame
import CurrencyRouletteGame


def welcome(name):
    output = f"Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play"
    return output


def load_game():
    game_to_play = int(input("\nPlease Choose an game to play:\n"
                         "1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n"
                         "2. Guess Game - guess a number and see if you chose like the computer\n"
                         "3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n"))

    if game_to_play not in range(1, 4):
        raise ValueError
    difficulty = int(input("\nPlease choose game difficulty from 1 to 5: "))
    if difficulty not in range(1, 5):
        raise ValueError
    try:
        if game_to_play == 1:
            MemoryGame.play(difficulty)
        if game_to_play == 2:
            GuessGame.play(difficulty)
            if game_to_play == 3:
                if CurrencyRouletteGame.play(difficulty):
                    print("\n-------YOU WON THE GAME---------\n")
    except ValueError:
        raise ValueError

