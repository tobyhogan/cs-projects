# an example where a binary tree could be used is in a family (i.e. where each family member has 2 children)

class Node:
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.right = None
        self.left = None


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
                if self.pointer.name >= item.name:
                    if self.pointer.right == None:
                        self.pointer.right = item
                        break

                    else:
                        self.pointer = self.pointer.right

                elif item.name > self.pointer.name:
                    if self.pointer.left == None:
                        self.pointer.left = item
                        break

                    else:
                        self.pointer = self.pointer.left

    def display_tree(self):
        currents = [self.root]

        while True:
            updated = False
            print([i.name for i in currents])

            for i in currents:
                if i.left != None:
                    currents.append(i.left)
                    updated = True

                if i.right != None:
                    currents.append(i.right)
                    updated = True

            print(updated)

            if updated == False:
                break


my_tree = BinaryTree()
my_tree.add_item(Node("Jaketh"))
my_tree.add_item(Node("Toby"))
my_tree.display_tree()
