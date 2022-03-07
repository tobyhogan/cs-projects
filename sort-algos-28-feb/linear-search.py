# this is the data set that I will be using as an example to find an item in
data = [1, 8, 1, 2, 9, 7, 6, 3, 5]

# this is the function definition where I get the item and data parameter, item is what I want to find, data is what I want to look for it in
def linear_search(item, data):
    # iterates through data, also getting an index as it goes
    for e, i in enumerate(data):
        # checks if the current item is equal to the item the search is looking for
        if i == item:
            # if it does find the item, aka they match then it will announce it 
            print(f"Found at index [{e}]")
            # once the item is found, it will also stop the search as it no longer needs to continue
            break

# calling the function
linear_search(5, data)
