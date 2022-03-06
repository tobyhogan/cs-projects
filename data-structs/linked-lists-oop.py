# class Node:
#     def __init__(self, data: int):
#         self.data = data
#         self.next = None


# class LinkedList:
#     def __init__(self, data: list = None):
#         self.data = data
#         if self.data:
#             self.head = None

#         else:
#             self.head = data[1]

#     def insert_item(self, item, position):
#         self.data.insert(position, item)

#     def add_item(self, item):
#         self.data.append(item)

#     def display_list(self):
#         print(self.data)

#     def get_iterator(self):
#         return self.data

#     def del_item(self):


# my_list = LinkedList([1, 3, 2])
# my_list.add_item(2)
# my_list.insert_item(3, 3)
# my_list.display_list()
# for i in my_list.get_iterator():
#     print(i)


class Node:
    def __init__(self, data=None, pos=None, next=None):
        self.data = data
        self.pos = pos
        self.next = next


class LinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def add_node(self, node):
        if self.head == None:
            self.head = node
            self.tail = node

    def get_iter(self):
        while True:
            pass
