import json

# Function to read order book data from a JSON
def read_order_book_data(file_path):
    with open(file_path, 'r') as file:
        order_book_data = json.load(file)
    return order_book_data

file_path = 'order-books-kraken-spot-btc-usd.json'

# Read order book data from the file we've obtained in the previous step
order_book_data = read_order_book_data(file_path)

# Function to calculate order imbalance
def calculate_order_imbalance(order_book_data):
    bids = sum(entry[0]["size"] for entry in order_book_data["bids"])
    asks = sum(entry[0]["size"] for entry in order_book_data["asks"])

    order_imbalance = (bids - asks) / (bids + asks)
    return order_imbalance

# Function to identify significant price levels
def identify_significant_price_levels(order_book_data, threshold=50):
    bids = order_book_data["bids"]
    asks = order_book_data["asks"]
    
    significant_bids = [entry for entry in bids if entry["size"] > threshold]
    significant_asks = [entry for entry in asks if entry["size"] > threshold]
    return significant_bids, significant_asks

# Function to calculate market spread
def calculate_market_spread(order_book_data):
    best_bid = order_book_data["bids"][0]["price"]
    best_ask = order_book_data["asks"][0]["price"]
    
    spread = best_ask - best_bid
    return spread

# Common metrics calculation
order_imbalance = calculate_order_imbalance(order_book_data)
significant_price_threshold = 20
significant_bids, significant_asks = identify_significant_price_levels(order_book_data, significant_price_threshold)
spread = calculate_market_spread(order_book_data)

print("******************************")
print("Order Imbalance:", order_imbalance)
print("***************************")
print("Significant Bids:", significant_bids)
print("***************************")
print("Significant Asks:", significant_asks)
print("***************************")
print("Market Spread:", spread)
print("***************************")
