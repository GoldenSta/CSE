import csv

profit_dict = {}
top_profit = 0
region_dict = {}
region_profit = 0
unit_dict = {}
unit_profit = 0

with open("Sales Records.csv", "r") as old_csv:
    reader = csv.reader(old_csv)
    total = 0
    for row in reader:
        item = row[2]
        profit = row[13]
        region = row[0]
        unit = row[8]
        if "Total Profit" == row[13]:
            continue

        try:
            profit_dict[item] += float(profit)
            region_dict[region] += float(profit)
            unit_dict[unit] += float(profit)
        except KeyError:
            profit_dict[item] = float(profit)
            region_dict[region] = float(profit)
            unit_dict[unit] = float(profit)

        if profit_dict[item] > top_profit:
            top_profit = profit_dict[item]

        if region_dict[region] > region_profit:
            region_profit = region_dict[region]

        if unit_dict[unit] > unit_profit:
            unit_profit = unit_dict[unit]

    for key, value in profit_dict.items():
        if value == top_profit:
            print(key)

    for key, value in region_dict.items():
        if value == region_profit:
            print(key)

    for key, value in unit_dict.items():
        if value == unit_profit:
            print(key)

print(total)
