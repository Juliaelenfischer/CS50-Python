import sys
import requests

def get_bitcoin_price():
    try:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        response.raise_for_status()  # Raise an exception for bad status codes
        bitcoin_data = response.json()
        bitcoin_price = bitcoin_data['bpi']['USD']['rate_float']
        return bitcoin_price
    except requests.RequestException as e:
        print("Error fetching Bitcoin price:", e)
        sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print("Missing command-line argument")
        sys.exit(1)

    try:
        bitcoins = float(sys.argv[1])
    except ValueError:
        print("Command-line argument is not a number")
        sys.exit(1)

    bitcoin_price = get_bitcoin_price()
    total_cost = bitcoins * bitcoin_price
    print(f"Total cost of {bitcoins:,.4f} Bitcoins: ${total_cost:,.4f}")

if __name__ == "__main__":
    main()
