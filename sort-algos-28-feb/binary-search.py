# takes an ordered data set as the data to actually be searched
data = [1, 3, 8, 12, 19, 36, 43, 46, 51, 68, 71, 73, 75, 81, 96, 99, 100]

recs = 0

# here I define the function for the search, it takes in two parameters - data to search through and the item it's looking for


def binary_search(data, item):
    global recs

    if len(data) > 0:
        mid = data[len(data) // 2]
    else:
        return None

    if item < mid:
        recs += 1
        binary_search(data[0: mid], item)

    elif item > mid:
        recs += 1
        binary_search(data[mid:], item)

    elif item == mid:
        print(f"Found item after {recs} recursions!")


binary_search(data, 73)
