"""
Structure of linked list

[Head] -> ... -> ... -> ... -> [Tail]

<- Next item
Previous item ->


"""

# creates a class for nodes, this allows them to be accessed like objects and have many different properties


class Node:
    # initialisation/constructor funciton of the object gives it a value of data to hold
    def __init__(self, data):
        # sets the data that the object will hold equal to the value that the object was inintialised with
        self.data = data
        # sets the pointer of the previous item to None(when the object will be part of a linked list)
        self.previous_item = None
        # sets the pointer of the next item also to None - as a placeholder
        self.next_item = None

# creates the class linked list that will actually be the data structure and will be made up of nodes


class LinkedList:
    # the initialisation function of the class, allows a predefined set of values to be passed in, so the list does not have to be created completely manually
    def __init__(self, items: list = None):
        # sets the head equal to none, for now
        self.head = None
        # sets the tail equal to none, for now
        self.tail = None

        # checks if any items were passed in, and if they were to do something
        if items:
            # goes through the list of data turning each data point into a node that has that same data
            items = [Node(i) for i in items]

            # goes through all the items
            for e, i in enumerate(items):
                # if an items index is less than index of the first item - a.k.a. the item is not the first one, to set the previous item pointer to the item ahead of it in the list
                if e != 0:
                    i.previous_item = items[e + 1]

                # if the item is the first item, then don't give it a previous item(set it to None)
                else:
                    i.previous_item = None

                # if the items index is not 0 - it's not the last item, then set the next item to the item with index n - 1
                if e != items.index(items[-1]):
                    i.next_item = items[e - 1]

            # the head of the list is the first item
            self.head = items[0]
            # the tail of the list is the last item
            self.tail = items[-1]

    # a method to add an item to the end of the linked list
    def append(self, item):
        # the old tails new previous item is the appended item
        self.tail.previous_item = item
        # the next item of the new tail is the old tail
        item.next_item = self.tail
        # the previous item of the new tail is nothing(None)
        item.previous_item = None
        # the new tail is the item that was passed in
        self.tail = item

    # a function to go through each item and print out the value of the data that it holds
    def iterate(self):
        # starts iteration at the head
        current_item = self.head
        while True:
            # outputs the current item of data
            print(current_item.data)
            # if the current item has more items behind it then make the current item the previous item
            if current_item.previous_item != None:
                current_item = current_item.previous_item

            # if there are no more items behind the current item then stop looping
            else:
                break

    # a function to show all the data items in the array and display them as if it was a list
    def display(self):
        # creating the empty array to act as a list
        arr = []
        # setting the item to look at currently to the first item in the list
        current_item = self.head
        # creating a loop that goes through each item in the list sequentially and adds the data to a list
        while True:
            # actually adding the data to a list
            arr.append(current_item.data)
            # checking if the current item is not the last item
            if current_item.previous_item != None:
                # setting the curerent itme to the item behind it
                current_item = current_item.previous_item
            else:
                break

        # actually giving the array with all the data values addded as a result
        return arr

# testing the program:


linked_list = LinkedList([1, 3, 5, 6, 8, 9, 10, 2, 3, 4, 5, 6])

print(linked_list.display())

linked_list.append(Node(8))

print(linked_list.display())
