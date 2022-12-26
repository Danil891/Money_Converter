import requests
import sys
import random
from dateutil.parser import parse


def rates_api(src):
    url = f"https://open.er-api.com/v6/latest/{src}"

    data = requests.get(url).json()
    if data["result"] == "success":
        last = parse(data["time_last_update_utc"])
        exchange_rates = data["rates"]
        # print(data)  # print all json
    return last, exchange_rates


def convert(src, dst, amount):
    last, exchange_rates = rates_api(src)
    return last, exchange_rates[dst] * amount


def convert_TRYtoRub(amount):
    source_currency = "TRY"
    destination_currency = "RUB"
    last, exchange_rate = convert(source_currency, destination_currency, amount)
    print("Last updated datetime:", last)
    print(f"{amount} {source_currency} = {exchange_rate} {destination_currency}")
    return f"{amount} {source_currency} = {exchange_rate} {destination_currency}"


def convert_RubtoTry(amount):
    source_currency = "RUB"
    destination_currency = "TRY"
    last, exchange_rate = convert(source_currency, destination_currency, amount)
    print("Last updated datetime:", last)
    print(f"{amount} {source_currency} = {exchange_rate} {destination_currency}")
    return f"{amount} {source_currency} = {exchange_rate} {destination_currency}"


def random_money():
    currencies = ["USD", "EUR", "AUD", "CAD", "BYN", "KZT", "UAH", "GBP", "CZK", "CHF", "JPY", "MGA", "AFN", "ZAR",
                  "XOF", "SCR", "RWF", "RUB", "TRY", "ANG", "BHD", "CAD", "DZD", "GTQ", "HNL", "KGS", "LRD", "MVR",
                  "NZD", "PHP", "RSD", "SGD", "SZL"]
    rand = random.randint(0, 32)
    rand1 = random.randint(0, 32)
    amount = random.randint(0, 1000000)
    last, exchange_rate = convert(currencies.pop(rand1), currencies.pop(rand), amount)
    print(f"{amount} {currencies.pop(rand1)} = {exchange_rate} {currencies.pop(rand)}")
    print(exchange_rate, currencies.pop(rand1), currencies.pop(rand))
    return currencies.pop(rand1), currencies.pop(rand), rand, rand1, amount


if __name__ == "__main__":
    notDigit = False
    no_arg = False
    if len(sys.argv) != 2:
        no_arg = True
    else:
        for char in sys.argv[1]:
            if not (char.isdigit() or char == '.'):
                notDigit = True

    if notDigit or no_arg:
        print("Validation error, run random")
        random_money()
    else:
        amount = float(sys.argv[1])
        convert_TRYtoRub(amount)
        convert_RubtoTry(amount)
