from random import randint


def generate_number(difficulty):
    secret_number = randint(1, diffi:wqculty)
    return int(secret_number)


def get_guess_from_user(difficulty):
    user_guess = input("Please enter a number between 1 to {}: \n".format(difficulty))
    return int(user_guess)


def compare_results(secret, guess):
    compare = secret == guess
    return compare


def play(difficulty):
    secret = generate_number(difficulty)
    guess = get_guess_from_user(difficulty)
    if compare_results(secret, guess):
        print("you and the pc choose the number {} so, You won the game !!!".format(secret))
    else:
        print("the pc generated the number {} and you choose {} so, you lose :(".format(secret, guess))

