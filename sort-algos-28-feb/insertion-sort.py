# This is the unsorted data set that will be sorted
data = [81, 2, 99, 22, 33, 45, 55, 29]


def lazy_insertion(data):
    # creates a list variable that will contain the sorted items
    sorted_data = []
    for i in range(len(data)):
        sorted_data.append(min(data))
        data.remove(min(data))

    return sorted_data


def hard_insertion(data):
    # creates a list variable that will contain the sorted items
    sorted_data = [0]
    for i in data:
        for e, j in enumerate(sorted_data):
            if len(sorted_data) <= (e + 1):
                if (i > j):
                    sorted_data.insert(e + 1, i)

            elif (i > j) and (i < sorted_data[e + 1]):
                sorted_data.insert(e + 1, i)

    sorted_data.remove(0)
    print(sorted_data)
    return sorted_data


print(hard_insertion(data))
