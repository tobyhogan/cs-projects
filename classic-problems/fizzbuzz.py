def attempt_one():
    for i in range(1, 101):
        conditions = ""
        if i % 2 == 0:
            conditions += "fizz"

        if i % 3 == 0:
            conditions += "buzz"

        print(i, conditions)


def attempt_two():
    [print(i, ("fizz" * (i % 2 == 0)) + ("buzz" * (i % 3 == 0)))
     for i in range(101)]


attempt_two()
