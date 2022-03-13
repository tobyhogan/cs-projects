"""
Structure of linked list

[Head] -> ... -> ... -> ... -> [Tail]

<- Next item
Previous item ->


"""


class Node:
    def __init__(self, data):
        self.data = data
        self.previous_item = None
        self.next_item = None


class LinkedList:
    def __init__(self, items: list = None):
        self.head = None
        self.tail = None

        if items:
            items = [Node(i) for i in items]

            for e, i in enumerate(items):
                if e < items.index(items[-1]):
                    i.previous_item = items[e + 1]

                else:
                    i.previous_item = None

                if e != 0:
                    i.next_item = items[e - 1]

            self.head = items[0]
            self.tail = items[-1]

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
