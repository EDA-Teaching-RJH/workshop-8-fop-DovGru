import csv

with open("contacts.csv") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(f"{row['name']} -> {row['email']}")