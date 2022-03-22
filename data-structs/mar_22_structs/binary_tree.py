class Node:
    def __init__(self, data, adj_nodes):
        self.data = data
        self.adj_nodes = adj_nodes


# tree format: {"A": ["B", "C"], "B": ["D", "E"]}


class BinaryTree:
    def __init__(self, tree: dict = None):
        if dict == None:
            self.root = None
            self.pointer = None

        elif dict != None:
            pass
