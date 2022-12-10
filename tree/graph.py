import numpy as np

from .tree import Tree


class UndirectedGraph(Tree):
    def __init__(self, array: list, undirected: bool = True, weighted_graph: bool = True):
        super().__init__(array, weighted_graph=weighted_graph, undirected=undirected)
