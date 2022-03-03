# This is the unsorted data set that will be sorted
data = [81, 2, 99, 22, 33, 45, 55, 29]

# creates a list variable that will contain the sorted items
sorted_data = [0]

for i in data[0:-1]:
    for e, j in enumerate(sorted_data):
        if i > j:
            sorted_data.insert((e + 1), i)
            print(sorted_data)

print(sorted_data)
    



