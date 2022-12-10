import numpy as np

from .tree import Graph


class UndirectedGraph(Graph):
    def __init__(self, array: list, undirected: bool = True, weighted_graph: bool = True):
        super().__init__(array, weighted_graph=weighted_graph, undirected=undirected)

    def get_edge_to(self, start, target):
        """
        Get connected edge to target
        """
        start = self.get_vertex(start) if isinstance(start, str) else start
        target = self.get_vertex(target) if isinstance(target, str) else target
        edges = start.edges

        path_list = np.array([edge for edge in edges if edge.left == target or edge.right == target])
        return path_list
