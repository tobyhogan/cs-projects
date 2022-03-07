data = [1, 8, 1, 2, 9, 7, 6, 3, 5]


def linear_search(item, data):
    for e, i in enumerate(data):
        if i == item:
            print(f"Found at index [{e}]")


linear_search(5, data)
