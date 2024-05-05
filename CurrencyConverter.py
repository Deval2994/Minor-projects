""""
Author: Deval Patel
Description: This project showcases the integration of an API key in Python to fetch real-time currency exchange rates,
demonstrating proficiency in handling external APIs and parsing JSON responses.
"""

import requests

API_KEY = 'fca_live_Ydgt9F6TZ61JRo8gW9dbEYc09vUHbgggEVoZaCoD'
BASE_URL = f'https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}'

CURRENCIES = ["USD", "EUR", "JPY", "GBP", "AUD", "CAD", "CHF", "CNY", "INR", "SEK"]


# Function to fetch currency conversion rates
def convertCurrency(base):
    currencies = ",".join(CURRENCIES)
    URL = f'{BASE_URL}&base_currency={base}&currencies={currencies}'
    try:
        response = requests.get(URL)
        data = response.json()
        return data["data"]
    except Exception as e:
        print("An error occurred: ", e)


if __name__ == "__main__":
    while True:
        baseCurrency = input("Enter Base Currency (e for exit): ").upper()
        if baseCurrency == "E":
            break
        elif baseCurrency not in CURRENCIES:
            print("Enter a valid Currency...")
            continue
        data = convertCurrency(baseCurrency)
        del data[baseCurrency]  # Removing base currency from the data
        for currency, value in data.items():
            print(f"{currency}: {value}")
