# This is the unsorted data set that will be sorted
data = [81, 2, 99, 22, 33, 45, 55, 29]

# This goes through each item in the data set, and also gets the index of the item
for e, i in enumerate(data):
    # This also goes through each data item, but is executed n(where n is the set length) for each item
    for f, j in enumerate(data):
        # This compares two items, and if one is smaller than the other, and the first is at a greater index, they're swapped
        if (i < j) and (e > f):
            # This code is the actual swapping of the data items
            data[e], data[f] = data[f], data[e]

# This prints out the sorted data set
print(data)