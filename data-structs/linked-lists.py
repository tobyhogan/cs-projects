# This is code for a uni-directional linked list

class Node:
    def __init__(self, data=None, pos=None, test=None):
        self.data = data
        self.pos = pos
        self.next = None


class LinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def add_node(self, node):
        if self.head == None:
            self.head = node
            self.tail = node

        else:
            self.head.next = node
            self.head = node
