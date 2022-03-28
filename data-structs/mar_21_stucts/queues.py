# creating the node class

# a class for nodes which make up the elements in queues
class Node:
    # initialising the class, getting data for it
    def __init__(self, data):
        self.data = data
        # setting the item before the node to nothing
        self.previous_item = None
        # setting the item after the node to nothing
        self.next_item = None

# creating the actual queue class itself


class Queue:
    # initialising the queue with the option to have items which pre-load the queue with values
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

    def enqueue(self, item):
        self.head.next_item = item
        item.previous_item = self.head
        self.head.previous_item = self.head.previous_item.previous_item
        self.head = item
        print(self.head.data)
        item.next_item = None

    def dequeue(self):
        self.tail = self.tail.next_item
        self.tail.previous_item = None
        del self.tail

    def iterate(self):
        current_item = self.head
        while True:
            print(current_item.data)
            if current_item.previous_item != None:
                current_item = current_item.previous_item

            else:
                break

    def peek_all(self):
        arr = []
        current_item = self.head
        print(self.head.data)
        while True:
            if current_item.previous_item != None:
                arr.append(current_item.data)
                current_item = current_item.previous_item

            else:
                break

        return arr


my_queue = Queue([1, 3, 5, 6, 8, 9, 10, 2, 3, 4, 5, 9])

print(my_queue.peek_all())
my_queue.dequeue()
my_queue.enqueue(Node(8))
print(my_queue.peek_all())
