from itertools import chain
from typing import List, Union

import numpy as np

from .edge import Edge
from .tree import Tree
from .vertex import Vertex


class UndirectedGraph(Tree):
    def __init__(self, array: list, undirected: bool = True, weighted_graph: bool = True):
        super().__init__(array, weighted_graph=weighted_graph, undirected=undirected)

    def get_edge_to(self, start: Union[str, Vertex], target: Union[str, Vertex]) -> List[Edge]:
        """
        Get connected edge to target
        """
        if isinstance(start, str):
            start = self.get_vertex(start)
        if isinstance(target, str):
            target = self.get_vertex(target)
        find_edge = np.vectorize(lambda edge: edge if edge.is_connected_to(target.name) else None)
        return (edges := find_edge(start.edges))[edges != None]

    def get_adjacent_vertices(self, name: str):
        """
        Get adjacent vertices by name
        """
        vertex = self.get_vertex(name)
        get_adjacent = (
            lambda edge: (edge.left, edge.right) if vertex.name in [edge.left.name, edge.right.name] else None
        )
        adjacent_vertices = np.vectorize(get_adjacent)(vertex.get_edges())

        adjacent_vertices = list(set(chain(*adjacent_vertices)))
        adjacent_vertices = [vertex for vertex in adjacent_vertices if vertex.name != name]
        return adjacent_vertices

    def get_smallest_edge(self):
        """
        Get the smallest edge in tree
        """
        return min(self.edges, key=lambda edge: edge.weight)

    def to_numpy(self, include_weighted: bool = True):
        """
        Convert graph to numpy array
        """
        get_edges_tuple = np.vectorize(lambda edge: (edge.left.name, edge.right.name, edge.weight))
        results = get_edges_tuple(self.edges)
        return np.array(list(zip(*results)))[:, : 3 if include_weighted else 2]

    @classmethod
    def from_numpy(cls, array: list, undirected: bool = True, weighted_graph: bool = True):
        return cls(array=array, undirected=undirected, weighted_graph=weighted_graph)

    @classmethod
    def from_adjacent_matrix(cls, matrix: np.ndarray, undirected: bool = True, weighted_graph: bool = True):
        """
        In further development...
        """
        pass
