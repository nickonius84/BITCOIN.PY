import sys
import requests

if len(sys.argv) != 2:
    sys.exit("Invalid command line argument ")

try:
    bitcoin = float(sys.argv[1])

except ValueError:
    sys.exit("Invalid command line argumente ")

try:
    info = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    data = info.json()
    price = data["bpi"]["USD"]["rate_float"]
except requests.RequestException:
    sys.exit("Error: Could not get the Bitcoin price")

total_cost = bitcoin * price

print(f"${total_cost:,.4f}")


