import numpy as np


class Vertex:
    def __init__(self, name: str, edge: np.ndarray = np.array([]), undirected: bool = True):
        self.name = name
        self.edges = edge
        self.undirected = undirected

    def add_edges(self, edges: list):
        self.edges = np.append(self.edges, edges)

    def update_degrees(self):
        self.degrees = len(self.edges)

    def get_edges(self):
        return self.edges
