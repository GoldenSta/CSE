import csv

profit_dict = {}
top_profit = 0
region_dict = {}
region_profit = 0
unit_dict = {}
unit_profit = 0

with open("Sales Records.csv", "r") as old_csv:
    reader = csv.reader(old_csv)
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
            unit_dict[item] += float(unit)
        except KeyError:
            profit_dict[item] = float(profit)
            region_dict[region] = float(profit)
            unit_dict[item] = float(unit)

        if profit_dict[item] > top_profit:
            top_profit = profit_dict[item]

        if region_dict[region] > region_profit:
            region_profit = region_dict[region]

    for key, value in profit_dict.items():
        if value == top_profit:
            print(key)

    for key, value in region_dict.items():
        if value == region_profit:
            print(key)

    for key, value in unit_dict.items():
        if profit_dict[key] / value > unit_profit:
            unit_profit = profit_dict[key] / value

    for key, value in unit_dict.items():
        if profit_dict[key] / value == unit_profit:
            print(key)
