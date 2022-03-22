class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


# how stack will be stored in memory: [... -> ... -> ... -> Head]

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
                    i.previous = items[e - 1]

                if e != items.index(items[-1]):
                    i.next = items[e + 1]

        self.top = items[-1]
        self.bottom = items[0]

    def iterate(self):
        current_item = self.bottom

        while True:
            if current_item.next == None:
                break

            print(current_item.data)
            current_item = current_item.next

    def check_underflow(self):
        if self.top == None and self.bottom == None:
            return True

        else:
            return False

    def check_overflow(self):
        if


my_stack = Stack([83, 34, 53, 12, 2, 9, 21, 32, 93, 32])
my_stack.iterate()

print(my_stack.top.data)
print(my_stack.bottom.data)
