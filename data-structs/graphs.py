"""
Need to be able to do:
- Depth first search
- Breadth first search
- Traversal
"""

# for a undirected unweighted graph


class Node:
    def __init__(self, connections):
        # connections in format: [connected node, weight]
        self.connections = connections


class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
