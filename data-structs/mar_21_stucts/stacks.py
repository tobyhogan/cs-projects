# NOTE: NOT DONE

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


# how stack will be stored in memory: [Bottom -> ... -> ... -> ... -> Top]

class Stack:
    def __init__(self, items: list = None):
        self.limit = 1024

        if items == None:
            self.top = None
            self.bottom = None

        elif items != None:
            for e, i in enumerate(items):
                items[e] = Node(i)

            for e, i in enumerate(items):
                if e != 0:
                    i.prev = items[e - 1]

                if e != items.index(items[-1]):
                    i.next = items[e + 1]

        self.top = items[-1]
        self.bottom = items[0]

    def iterate(self):
        current_item = self.bottom

        while True:
            if current_item == None:
                break

            print(current_item.data)
            current_item = current_item.next

    def display(self):
        arr = []
        current_item = self.bottom

        while True:
            if current_item == None:
                break

            arr.append(current_item.data)
            current_item = current_item.next

        return arr

    def check_underflow(self):
        if self.top == None and self.bottom == None:
            return True

        else:
            return False

    def check_overflow(self):
        if len(self.display()) == self.limit:
            return True

        else:
            return False

    def pop_item(self):
        self.top.prev.next = None
        self.top = self.top.prev

    def push_item(self, item):
        if type(item) == Node:
            self.top.next = item
            item.next = None
            item.prev = self.top
            self.top = item

        else:
            raise Exception("Input must be type <Node>")


my_stack = Stack([83, 34, 53, 12, 2, 9, 21, 32, 93, 24])
print(my_stack.display())
my_stack.push_item(Node(9))
print(my_stack.display())
