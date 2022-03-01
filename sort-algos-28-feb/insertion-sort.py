# This is the unsorted data set that will be sorted
data = [81, 2, 99, 22, 33, 45, 55, 29]
sorted_data = [None for i in data]

for e, i in enumerate(range(len(data), 0, -1)):
    if i > sorted_data[e]:
        sorted_data.append(i)


print(sorted_data)
