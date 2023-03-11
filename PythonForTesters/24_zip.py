cost = [45, 30, 70]
sales = [60, 35, 60]

# combines each same index from voth lists
match = zip(cost, sales)

# for x in match:
#     print(x)

for x, y in match:
    print("Profit:", (y-x))
