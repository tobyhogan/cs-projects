# program converts denary numbers(with base 10) to hexidecimal numbers(with base 16)
# 130 in denary would be converted to 82 because 82 in hex is (8*16) + (2*1)

# hex conversion chart:

# 256 = 100
# 16 = 10
# 15 = 0F

from itertools import count
from time import sleep

den_num = int(input("Please enter a number in denary: "))
den_num_remaining = den_num
max_pos_occupied = 0
hex_num = ""

hex_digits = ["A", "B", "C", "D", "E", "F"]


for i in count():
    if (den_num // (16**i) == 0):
        max_pos_occupied = i - 1
        break

    
def den_to_hex(num):
    if num < 10:
        return str(num)
    
    elif num > 15:
        raise Exception("Number must not be greater than 15")
    
    return hex_digits[num - 10]


for i in range(max_pos_occupied, -1, -1):
    times_hex_into_den = den_num_remaining // (16**i)
    hex_num += den_to_hex(times_hex_into_den)
    den_num_remaining -= (times_hex_into_den*(16**i))

print(f"The resultant hex number is: {hex_num}")

