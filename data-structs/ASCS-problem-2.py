import itertools

"""
Binary to decimal: 

bin_num = "0"
dec_num = 0

for i in range(len(bin_num) - 1, -1, -1):
    dec_num += int(bin_num[i]) * (2**i)

print(dec_num)
"""

# Decimal to binary

dec_num = str(1090)

for e, i in enumerate(range(len(dec_num) - 1, -1, -1)):
    place_val = (10 ** i) * int(dec_num[e])
    print(f"Decimal value: {place_val}")

    for j in itertools.count(start=0):
        if 2 ** j > place_val:
            div = 2 ** j
            print(f"Greater divisor: {div}")
            break
        


    # print(10 ** i)

