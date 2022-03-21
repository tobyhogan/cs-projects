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

    #
    def append(self, item):
        self.tail.previous_item = item
        item.next_item = self.tail
        item.previous_item = None
        self.tail = item

    def iterate(self):
        current_item = self.head
        while True:
            print(current_item.data)
            if current_item.previous_item != None:
                current_item = current_item.previous_item

            else:
                break

    def display(self):
        arr = []
        current_item = self.head
        while True:
            arr.append(current_item.data)
            if current_item.previous_item != None:
                current_item = current_item.previous_item
            else:
                break

        return arr


linked_list = LinkedList([1, 3, 5, 6, 8, 9, 10, 2, 3, 4, 5, 6])

print(linked_list.display())

linked_list.append(Node(8))

print(linked_list.display())
