complete_nums = [i for i in range(10, 21)]
incomplete_nums = [10, 12, 13, 14, 15, 16, 17, 18, 19, 20]

for num in complete_nums:
    if not(num in incomplete_nums):
        print(f"{num} is missing!")
