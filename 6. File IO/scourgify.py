import sys
import csv

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif (len(sys.argv)) < 3:
    sys.exit("Too few command-line arguments")
else:
    try:
        students = []
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            students = [
                {
                    "first": row["name"].split(",")[1].strip(' "'),
                    "last": row["name"].split(",")[0].strip(' "'),
                    "house": row["house"]
                }
                for row in reader
            ]
        with open(sys.argv[2], "w", newline="") as file:
            fieldnames = ["first", "last", "house"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(students)
    except ValueError:
        sys.exit(f"Could not read {sys.argv[1]}")