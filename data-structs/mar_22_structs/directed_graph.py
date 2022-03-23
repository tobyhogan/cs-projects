# format: {"A": ["B", "C"], "B": ["A", "C"], "C": ["A", "B"]}

class Node:
    def __init__(self, data, adj_nodes: list = []):
        self.data = data
        self.adj_nodes = adj_nodes


class DirectedGraph:
    def __init__(self, items: dict = {}):
        if items == None:
            self.root = None
            self.pointer = None

        else:
            self.root = list(items.keys())[0]
            for key, value in items.items():
                self.pointer = Node(key)

                for i in value:
                    self.pointer.adj_nodes.append(i)

                print(self.pointer.data, self.pointer.adj_nodes)


my_graph = DirectedGraph({"A": ["B", "C"], "B": ["A", "C"], "C": ["A", "B"]})
