import csv


def load(path):
    rows = []
    with open(path) as f:
        reader = csv.reader(f)
        for line in reader:
            rows.append(line)
    return rows[1:]


def find_restock(rows, threshold=10, flagged=[]):
    result = {}
    for row in rows:
        name = row[0]
        qty = int(row[1])
        per_day = float(row[2])
        if qty < threshold:
            days_left = qty / per_day
            result[name] = round(days_left)
            flagged.append(name)
    return result, flagged


def report(data):
    total = 0
    for name in data:
        total += data[name]
    avg = total / len(data)
    print("Items needing restock: " + str(len(data)))
    print("Average days of stock remaining: " + str(avg))
    for name in data:
        print("  " + name + ": " + str(data[name]) + " days")


rows = load("inventory.csv")
urgent, seen = find_restock(rows)
report(urgent)
