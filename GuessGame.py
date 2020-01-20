from random import randint


def generate_number(difficulty):
    secret_number = randint(1, difficulty)
    return int(secret_number)


def get_guess_from_user(difficulty):
    print("\n----------------\n")
    print("Hello and welcome to GuessGame")
    user_guess = input("Please enter a number between 1 to {}: \n".format(difficulty))
    if user_guess not in range (1, difficulty):
        raise ValueError
    return int(user_guess)


def compare_results(secret, guess):
    compare = secret == guess
    return compare


def play(difficulty):
    try:
        secret = generate_number(difficulty)
        guess = get_guess_from_user(difficulty)
        if compare_results(secret, guess):
            print(f"you and the pc choose the number {secret} so, You won the game !!!")
        else:
            print(f"the pc generated the number {secret} and you choose {guess} so, you lose :(")
    except ValueError:
        raise ValueError
