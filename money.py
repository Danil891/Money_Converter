import requests
import sys
from dateutil.parser import parse


def rates_api(src):
    url = f"https://open.er-api.com/v6/latest/{src}"

    data = requests.get(url).json()
    if data["result"] == "success":
        last = parse(data["time_last_update_utc"])
        exchange_rates = data["rates"]
        print(data)  # print all json
    return last, exchange_rates


def convert(src, dst, amount):
    last, exchange_rates = rates_api(src)
    return last, exchange_rates[dst] * amount


if __name__ == "__main__":
    source_currency = sys.argv[1]
    destination_currency = sys.argv[2]
    amount = float(sys.argv[3])
    last, exchange_rate = convert(source_currency, destination_currency, amount)
    print("Last updated datetime:", last)
    print(f"{amount} {source_currency} = {exchange_rate} {destination_currency}")
