# an example where a binary tree could be used is in a family (i.e. where each family member has 2 children)

class Node:
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.right_child = None
        self.left_child = None


class BinaryTree:
    def __init__(self):
        self.root = None
        self.pointer = None

    # adds the item depending on the letters in its name
    def add_item(self, item):
        if self.root == None:
            self.root = item

        else:
            self.pointer = self.root

            while True:
                for i in range(min(len(self.pointer.name), len(item.name)) + 1):
                    # print(self.pointer.name[i])

                    print(item.name[i], self.pointer.name[i])
                break


my_tree = BinaryTree()
my_tree.add_item(Node("Toby"))
my_tree.add_item(Node("Jaketh"))
