import numpy as np

from .tree import Tree


class UndirectedGraph(Tree):
    def __init__(self, structure: list, undirected: bool = True, weighted_graph: bool = True):
        super().__init__(structure, weighted_graph=weighted_graph, undirected=undirected)
