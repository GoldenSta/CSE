import csv

with open("Sales Records.csv", "r") as old_csv:
    reader = csv.reader(old_csv)
    total = 0
    for row in reader:
        item = row[2]
        profit = row[13]
        if "Fruits" == item:
            total += float(profit)

print(total)
