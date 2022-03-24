# format: {"A": ["B", "C"], "B": ["A", "C"], "C": ["A", "B"]}

# NOTE: UNFINISHED
# TODO: make directed

class Node:
    def __init__(self, data, adj_nodes: list = []):
        self.data = data
        self.adj_nodes = adj_nodes


class DirectedGraph:
    def __init__(self, items: dict = {}):
        self.root = None
        self.pointer = None
        self.members = []

        # if there is a list inputted to build a graph off, then go through each item and build it up
        if items != None:
            # the root item should be the item at the start of the dictionary given
            self.root = list(items.keys())[0]
            # the pointer(the item that's currently being looked at should start as the root)
            self.pointer = self.root

            # go through each node in the list and unpack it's value and the nodes that it's connected to(key)
            for key, value in items.items():
                self.pointer = Node(key)

                # goes through each of the adjacent nodes listed from the input
                for i in value:
                    found_node = False
                    # goes through each of the nodes(and their indicies) that are already registered with the list
                    for e, j in enumerate(self.members):
                        # if the value has aleready been made with a node, then add the node to the current nodes adjacent list
                        if j.data == i:
                            # adding the node to the current nodes adjacent list
                            self.pointer.adj_nodes.append(j)
                            found_node = True

                    if not(found_node):
                        new_node = Node(i)
                        self.pointer.adj_nodes.append(new_node)
                        self.members.append(new_node)


my_graph = DirectedGraph({"A": ["B", "C"], "B": ["A", "C"], "C": ["A", "B"]})

for i in my_graph.members:
    print(i.data)
    print(i.adj_nodes)
