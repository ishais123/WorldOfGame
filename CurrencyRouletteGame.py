import requests
from random import randint


def get_guess_from_user():
    print("\n----------------\n")
    print("Hello and welcome to CurrencyRouletteGame")
    user_guess = input ("Please guess a number: ")
    return user_guess


def get_money_interval(difficulty):
    random = randint(1, 100)
    # print(f"the random is{random}")
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data = payload)
    to_json = response.json()
    rate = to_json.get("rates").get("ILS")
    # print(f"the rate is{rate}")
    interval = (random/rate - float(5 - difficulty), random/rate + float(5 - difficulty))
    return interval


def play(difficulty):
    user_guess = get_guess_from_user()
    interval = get_money_interval(difficulty)
    # print(f"the min is {interval[0]}")
    # print(f"the max is {interval[1]}")
    if interval[1] >= float(user_guess) >= interval[0]:
        return True
    else:
        end_message = f"Sorry but your number was {user_guess}" \
                      f" and the to won the game you had to choose number between {interval[0]} to {interval[1]}"
        print("\n----------------\n")
        print(end_message)
        return False
