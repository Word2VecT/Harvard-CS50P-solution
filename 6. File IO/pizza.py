import sys
import csv
from tabulate import tabulate

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif (len(sys.argv)) == 1:
    sys.exit("Too few command-line arguments")
else:
    if (not sys.argv[1].endswith(".csv")):
        sys.exit("Not a CSV file")
    try:
        table = []
        headers = ["Regular Pizza" if sys.argv[1] == "regular.csv" else "Sicilian Pizza", "Small", "Large"]
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            table.extend([row[header] for header in headers] for row in reader)
        print(tabulate(table, headers, tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")