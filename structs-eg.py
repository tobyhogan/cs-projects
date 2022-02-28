import random

sales = [random.randint(0, 5) for i in range(5)]

while True:
    year = int(input("Enter a year between 1 and 5: "))
    if year - 1 == 0:
        sales[0] = int(input(f"Enter a new value for year 1: "))

    else:
        print(year - 1)
