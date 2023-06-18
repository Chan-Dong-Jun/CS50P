#02/06/2023
#CS50P Week 6

import sys
import csv
from tabulate import tabulate

if len(sys.argv) != 2:
    sys.exit("Incorrect number of command-line arguments")
if not sys.argv[1].endswith(".csv"):
    sys.exit("Not a csv file")

pizza= []
col_names = {}
try:
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for field in reader.fieldnames:
            col_names[field] = field
        for row in reader:
            pizza.append({reader.fieldnames[0]: row[reader.fieldnames[0]], "Small": row["Small"], "Large": row["Large"]})
except FileNotFoundError:
    sys.exit("File not found")
print(tabulate(pizza, col_names, tablefmt="grid"))