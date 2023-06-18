#02/06/2023
#CS50P Week 6

import sys
import csv

if len(sys.argv) != 3:
    sys.exit("Incorrect number of command-line arguments")
if not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
    sys.exit("Not a csv file")

rows = []
try:
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            last, first = row["name"].strip('"').split(", ")
            rows.append({"first": first, "last": last, "house": row["house"]})
except FileNotFoundError:
    sys.exit("File not found")

try:
    with open(sys.argv[2], "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for row in rows:
            writer.writerow({"first": row["first"], "last": row["last"], "house": row["house"]})
except FileNotFoundError:
    sys.exit("File not found")
