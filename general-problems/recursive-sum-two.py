def sum_even(n):
    if n != 0:
        return n + sum_even(n - 2)

    else:
        return 0


print(sum_even(10))
