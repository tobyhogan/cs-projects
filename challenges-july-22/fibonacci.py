# the fibonacci sequence 
from time import sleep

def fib(limit):
    sequence = []
    x = 0
    y = 1
    z = 0
    for i in range(limit):
        z = x + y
        print(f"Number {i + 1}: {z}")
        x = y
        y = z

fib(int(input("Enter the number of digits you want to generate for: ")))