# a dict for mock currencies EUR: 4.75
import argparse
import requests


CURRENCIES = {
    'EUR': 4.75,
    'USD': 4.80,
    'CAD': 3.50
}

def parser():
    parser = argparse.ArgumentParser(description='Exchange the currencies')

    parser.add_argument('amount', type=int,
                        help='an integer for the currency')
    parser.add_argument('currency', type=str, 
        choices=CURRENCIES.keys(), help='currency type')


    args = parser.parse_args()

    return args

args = parser()

def fetch_currency_rate(currency: str) -> float:
    r = requests.get('http://api.nbp.pl/api/exchangerates/tables/A/')

    rates = r.json()[0]["rates"]

    for i in rates:
        if i["code"] == currency:
            return i["mid"]

def convert(value: float, currency: str) -> float:
    exchange_rate = fetch_currency_rate(currency)
    return value * exchange_rate
    # return exchange_rate * value



input = (args.amount, args.currency)
output = convert(value=input[0], currency=input[1])
print(f"{output} PLN")



