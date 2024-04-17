import json
import matplotlib.pyplot as plt

# Function to read order book data from a JSON
def read_order_book_data(file_path):
    with open(file_path, 'r') as file:
        order_book_data = json.load(file)
    return order_book_data

file_path = 'order-books-kraken-spot-btc-usd.json'

# Read order book data from the file we've obtained in the previous step
order_book_data = read_order_book_data(file_path)

# Function to visualize order book depth chart
def visualize_order_book_depth(order_book_data):
    bids = order_book_data["bids"]
    asks = order_book_data["asks"]
    
    bid_prices = [entry["price"] for entry in bids]
    bid_sizes = [entry["size"] for entry in bids]
    
    ask_prices = [entry["price"] for entry in asks]
    ask_sizes = [entry["size"] for entry in asks]
    
    plt.figure(figsize=(10, 6))
    plt.plot(bid_prices, bid_sizes, label="Bids (buyers)", color="green")
    plt.plot(ask_prices, ask_sizes, label="Asks (sellers)", color="red")
    plt.xlabel("Price")
    plt.ylabel("Size")
    plt.title("Order Book Depth")
    plt.legend()
    plt.savefig("order-book-depth.png")  # Save the figure as an image file
    plt.show()

# Visualize the order book depth
visualize_order_book_depth(order_book_data)
