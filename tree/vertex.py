import numpy as np


class Vertex:
    def __init__(self, name: str, edge: np.ndarray = np.empty((0,)), undirected: bool = True):
        self.name = name
        self.edges = edge
        self.degrees = len(edge)
        self.undirected = undirected
        
    def get_smallest_edge(self):
        return min(self.edges, key=lambda edge: edge.weight)

    def add_edges(self, edges: list):
        self.edges = np.append(self.edges, edges)

    def update_degrees(self):
        self.degrees = len(self.edges)

    def get_edges(self):
        return self.edges
