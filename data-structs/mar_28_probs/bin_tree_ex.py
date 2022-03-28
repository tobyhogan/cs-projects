import time

# an example where a binary tree could be used is in a family (i.e. where each family member has 2 children)

#


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
        # if the item to be added is the first item, make it the root
        if self.root == None:
            self.root = item

        # if the item to be added is not the first item, make the root the pointer
        else:
            self.pointer = self.root

            # go through each node that decends off of the root node until a space is found
            while True:
                # if the current location of the pointer's name is higher in the alphabet than the name of the item then try to make it go to the right
                if self.pointer.name >= item.name:
                    # if the right has nothign on it, then make the node that location(on the right)

                    print(item.name, "Going right")

                    if self.pointer.right == None:
                        self.pointer.right = item
                        print(item.name, "Placed")
                        break

                    else:
                        # if the item on the right does hold something, then make the pointer equal to it and redo the loop
                        self.pointer = self.pointer.right

                # if the items name is higher in the alphabet than the current node then try and make it go to the left
                elif item.name > self.pointer.name:
                    print(item.name, "Going left")

                    # if the item on the left is empty then make it hold the item
                    if self.pointer.left == None:
                        self.pointer.left = item
                        print(item.name, "Placed")
                        break

                    else:
                        # if the item on the left is already holding something, then set the pointer to the item and redo the loop
                        self.pointer = self.pointer.left

    def display_as_tree(self):
        nodes = [(0, self.root)]

        if nodes[0][1].left != None:
            nodes.append((1, nodes[0][1].left))

        if nodes[0][1].right != None:
            nodes.append((1, nodes[0][1].right))

        level = 1

        while True:
            updated = False
            print("Level in while loop", level)

            for i in nodes:
                if not(i in nodes):
                    if i.left != None:
                        nodes.append((level, i.left))
                        updated = True

                    if i.right != None:
                        nodes.append((level, i.right))
                        updated = True

            level += 1

            if updated == False:
                break

        print(nodes)

        for i in range(level):
            print("Level", i)
            print([item[1].name for item in nodes if item[0] == i])

    def display_as_list(self):
        self.ponter = root


my_tree = BinaryTree()

my_tree.add_item(Node("Jaketh"))
my_tree.add_item(Node("Toby"))
my_tree.add_item(Node("Joby"))

my_tree.display_as_tree()
