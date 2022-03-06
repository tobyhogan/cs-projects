# This is the unsorted data set that will be sorted
data = [81, 2, 99, 22, 33, 45, 55, 29]


def lazy_insertion(data):
    # creates a list variable that will contain the sorted items
    sorted_data = []
    # this goes through each item in the data set
    for i in range(len(data)):
        # this finds the smallest item in the current iteration and adds it to the sorted data
        sorted_data.append(min(data))
        # this removes the item that was just added to the sorted data set, so it can't be added again
        data.remove(min(data))
    # produces the sorted data set as an output
    return sorted_data


def hard_insertion(data):
    # creates a list variable that will contain the sorted items and sets it to 0, so there is something for the program to work with
    sorted_data = [0]
    # goes through each item in the data set
    for i in data:
        # sub-iterates through each item in the sorted data set, also enumerating to give access to it's index
        for e, j in enumerate(sorted_data):
            # if the program is at the end of the list, only insert the element if the item before is smaller - no comparison to non-existant last element
            if len(sorted_data) <= (e + 1):
                # the comparision for insertion
                if (i > j):
                    # the actual insertion itself
                    sorted_data.insert(e + 1, i)

            # if there is more elements after the current one, do the comparision for the element after, as well as before
            elif (i > j) and (i < sorted_data[e + 1]):
                # inserting the element
                sorted_data.insert(e + 1, i)
    # removing the first element which wasn't actually needed, just used to get things started
    sorted_data.remove(0)
    # outputting the value from the function
    return sorted_data

# printing the value to the console to check it's correct
print(hard_insertion(data))
