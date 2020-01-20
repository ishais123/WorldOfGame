import requests


def get_money_interval(difficulty):
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data = payload)
    to_json = response.json()
    rate = to_json.get("rates").get("ILS")
    interval = (rate-float(5-difficulty), rate+float(5-difficulty))
    return interval
