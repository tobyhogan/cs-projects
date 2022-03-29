import time

# an example where a binary tree could be used is in a family (i.e. where each family member has 2 children)

ln_break = "============================================================================"


class Node:
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.right = None
        self.left = None
        self.depth = None


class BinaryTree:
    def __init__(self):
        self.root = None
        self.pointer = None

    # adds the item depending on the letters in its name
    def add_item(self, item):
        # if the item to be added is the first item, make it the root
        if self.root == None:
            self.root = item
            self.root.depth = 0

        # if the item to be added is not the first item, make the root the pointer
        else:
            self.pointer = self.root

            # go through each node that decends off of the root node until a space is found
            while True:
                # if the current location of the pointer's name is higher in the alphabet than the name of the item then try to make it go to the right
                if self.pointer.name <= item.name:
                    # if the right has nothing on it, then make the node that location(on the right)

                    if self.pointer.right == None:
                        # making the place to the right of the pointer equal to the item
                        self.pointer.right = item
                        # making the parent of the item, the pointer
                        item.parent = self.pointer
                        # making the depth of the item the depth of the parent add 1
                        item.depth = self.pointer.depth + 1

                        break

                    else:
                        # if the item on the right does hold something, then make the pointer equal to it and redo the loop
                        self.pointer = self.pointer.right

                # if the items name is higher in the alphabet than the current node then try and make it go to the left
                elif item.name < self.pointer.name:

                    # if the item on the left is empty then make it hold the item
                    if self.pointer.left == None:
                        # making the place to the left of the pointer equal the item
                        self.pointer.left = item
                        # making the parent of the item, the pointer
                        item.parent = self.pointer
                        # making the depth of the item the depth of the parent add 1
                        item.depth = self.pointer.depth + 1

                        break

                    else:
                        # if the item on the left is already holding something, then set the pointer to the item and redo the loop
                        self.pointer = self.pointer.left

    def display_as_tree(self):
        # making a list of nodes to contain all the other nodes, and the depth they're at
        nodes = [self.root]

        # checking if the root node has a left node, if it does: add it to the list at depth 1
        if self.root.left != None:
            nodes.append(self.root.left)

        # checking if the root node has a right node, if it does: add it to the list at depth 1
        if self.root.right != None:
            nodes.append(self.root.right)

        # setting the default depth to be 1, as we've just added two items at level 1
        depth = 1

        # starting an infinite loop to go through and explore each node to see if it has other nodes
        while True:
            # setting the value of the updated variable to false(a.k.a no new nodes have been added YET)
            updated = False

            # going through each of the nodes in the list and looking to see if they have children
            for i in nodes:
                # checking to see if the index of the item has the greatest current depth(just the depth)
                if i.depth == depth:
                    # if the left child of the node is not empty, add that node to the list
                    if i.left != None:
                        nodes.append(i.left)
                        updated = True

                    if i.right != None:
                        nodes.append(i.right)
                        updated = True

            depth += 1

            if updated == False:
                break

        print(ln_break)
        for i in range(depth):
            print("Depth", i)
            print([j.name for j in nodes if j.depth == i])

        print(ln_break)

    def display_as_list(self):
        # making a list of nodes to contain all the other nodes, and the depth they're at
        nodes = [self.root]

        # checking if the root node has a left node, if it does: add it to the list at depth 1
        if self.root.left != None:
            nodes.append(self.root.left)

        # checking if the root node has a right node, if it does: add it to the list at depth 1
        if self.root.right != None:
            nodes.append(self.root.right)

        # setting the default depth to be 1, as we've just added two items at level 1
        depth = 1

        # starting an infinite loop to go through and explore each node to see if it has other nodes
        while True:
            # setting the value of the updated variable to false(a.k.a no new nodes have been added YET)
            updated = False

            # going through each of the nodes in the list and looking to see if they have children
            for i in nodes:
                # checking to see if the index of the item has the greatest current depth(just the depth)
                if i.depth == depth:
                    # if the left child of the node is not empty, add that node to the list
                    if i.left != None:
                        nodes.append(i.left)
                        updated = True

                    if i.right != None:
                        nodes.append(i.right)
                        updated = True

            depth += 1

            if updated == False:
                break

        print(ln_break)
        print([i.name for i in nodes])
        print([i.depth for i in nodes])
        print(ln_break)


my_tree = BinaryTree()

my_tree.add_item(Node("Jaketh"))
my_tree.add_item(Node("Aaron"))
my_tree.add_item(Node("Adam"))
my_tree.add_item(Node("Toby"))
my_tree.add_item(Node("Jed"))
my_tree.add_item(Node("Help"))
my_tree.add_item(Node("Me"))
my_tree.add_item(Node("Please"))


my_tree.display_as_tree()
my_tree.display_as_list()
