import csv

profit_dict = {}
top_profit = 0

with open("Sales Records.csv", "r") as old_csv:
    reader = csv.reader(old_csv)
    total = 0
    for row in reader:
        item = row[2]
        profit = row[13]
        if "Total Profit" == row[13]:
            continue

        try:
            profit_dict[item] += float(profit)
        except KeyError:
            profit_dict[item] = float(profit)

        if profit_dict[item] > top_profit:
            top_profit = profit_dict[item]

    for key, value in profit_dict.items():
        if value == top_profit:
            print(key)

print(total)
