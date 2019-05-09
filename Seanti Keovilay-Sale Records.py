import csv

with open("Sales Records.csv", "r") as old_csv:
    reader = csv.reader(old_csv)
    for row in reader:
        item = row[2]
        profit = row[13]
        if "fruits" == item:
            profit_list = sum(profit)
        print(profit_list)
