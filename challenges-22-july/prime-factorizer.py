num = int(input("Enter a number that you want to check is prime: "))
# primes cannot have factors greater than themselves
# primes only have two factors, themselves and 1

factors = []

for i in range(1, num + 1):
    if (num % i == 0) and (num != 2):
        factors.append(i)

if len(factors) == 2:
    print(f"{num} is prime!")

else:
    print(f"{num} is not prime.")