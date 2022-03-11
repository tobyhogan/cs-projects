"""
How quick sort works:
- A pivot is chosen(I.e. mean of three):
    - The first, middle and last elements of the list are identified
    - The identified items are sorted properly and the middle one is estimated to be close to the middle of the list
- An item from the left is chosen, which is the first one that is larger than the pivot
- An item from the right is chosen, whichis the first on that is smaller than the pivot
- Switch these two items that have been selected
- Repeat the process until the item from left has a greater index than the item from the left
- Swap the item from the left with the pivot
- The two separate lists on either side of the pivot are isolated and have the process above perfomed on them recursively



A pivot is an item in the final sorted array that:
- Has a correct position
- All the items to the left are smaller
- All the items to the right are larger
"""

# this is the data set that will be used for the project
data = [3, 9, 2, 1, 8, 7, 6, 5, 9, 6, 2, 8]


def quick_sort(data):
    if len(data) < 3:
        print(f"Data that's less than 3: {data}")
        if data[1] > data[0]:
            data[0], data[1] = data[1], data[0]

        return data

    elif len(data) >= 3:
        print(f"Data that's greater than or equal to 3: {data}")

        # finds (using the mean of 3 method), the first, middle and last items in the data
        quartiles = [data[0], data[(len(data) // 2)], data[-1]]
        # sorts the items, so they are in order from highest to lowest
        quartiles.sort()
        # sets the pivot as the middle one of these values, after they've been sorted
        pivot = quartiles[1]
        # removes the pivot from the data set, so it can be compared properly without interference

        print(f"The length of the data is: {len(data)}")

        if len(data) == 3:
            print("returning quartiles for len 3 data")
            print(f"The sorted data is {quartiles}")
            return quartiles

        data.remove(pivot)

        while True:
            for e, i in enumerate(data):
                if i > pivot:
                    l_index = e
                    break

            for i in range(len(data) - 1, -1, -1):
                if data[i] < pivot:
                    r_index = i
                    break

            if l_index > r_index:
                break
            else:
                data[e], data[r_index] = data[r_index], data[e]

        data.insert(len(data) // 2, pivot)

        sorted = True
        for e, i in enumerate(data):
            try:
                if i > data[e + 1]:
                    sorted = False
            except:
                pass

        if sorted == True:
            print("ending")
            print(f"the sorted data is {data}")
            return data

        elif sorted == False:
            print(f"The sorted data is {data}")
            print("recursing")
            return quick_sort(data[0:data.index(pivot)]) + quick_sort(data[data.index(pivot) + 1:])


print(quick_sort(data))

# FIXME item recombination algorithm needs work
