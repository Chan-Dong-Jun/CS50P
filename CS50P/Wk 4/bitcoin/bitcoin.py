# Saturday, 27/05/2023
# CS50P Week 4

import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
try:
    float(sys.argv[1])
except:
    sys.exit("Command-line argument is not a number")

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
    per_unit_price = response["bpi"]["USD"]["rate_float"]
    print(f"${float(sys.argv[1])*per_unit_price:,.4f}")

except requests.RequestException:
    sys.exit("Error retrieving price")
