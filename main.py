import requests
import json

API_KEY = "41134A54-15EA-4727-AF95-0D8434382EEE"
symbol = "KRAKEN_SPOT_BTC_USD"
url = f"https://rest.coinapi.io/v1/orderbooks/current?filter_symbol_id={symbol}&apikey={API_KEY}"

response = requests.get(url)

if response.status_code == 200:
    # The request was successful
    data = response.json()
    
    # Save the data to a file
    with open("order-books-kraken-spot-btc-usd.json", "w") as file:
        json.dump(data, file, indent=4)
    print("Data saved to order-books-kraken-spot-btc-usd.json")
else:
    # Handle error cases
    print(f"Error: Status code {response.status_code}")
    print(response.text)
