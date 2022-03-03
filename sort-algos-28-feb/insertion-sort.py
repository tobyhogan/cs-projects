# This is the unsorted data set that will be sorted
data = [81, 2, 99, 22, 33, 45, 55, 29]
<<<<<<< HEAD

# creates a list variable that will contain the sorted items
sorted_data = [0]

for i in data[0:-1]:
    for e, j in enumerate(sorted_data):
        if i > j:
            sorted_data.insert((e + 1), i)
            print(sorted_data)

print(sorted_data)
    



=======
sorted_data = [None for i in data]

for e, i in enumerate(range(len(data), 0, -1)):
    if i > sorted_data[e]:
        sorted_data.append(i)


print(sorted_data)
>>>>>>> bc4daa0ed3a53cc35766df0312d3e40df39e20b2
