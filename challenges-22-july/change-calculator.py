# line_break = "=========================="

# print(line_break)
# money = float(input("Please enter the amount of money you want to convert: "))
# print(line_break)


money = 650.25
total_pence = money * 100

pounds = total_pence // 100
pence = total_pence - (pounds * 100)

pound_denoms = [1, 2, 5, 10, 50]
pence_denoms = [1, 2, 5, 10, 20, 50]

usable_pounds = []
usable_pence = []

for denom in pound_denoms:
    if (pounds - denom) > 0:
        usable_pounds.append([denom, (pounds // denom)])

pound_combinations = []


# for denom in pence_denoms:
#     if pence % denom == 0:
#         usable_pence.append([denom, (pence / denom)])


print(usable_pounds)
