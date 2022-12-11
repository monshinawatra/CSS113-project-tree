import time
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
        if isinstance(start, str):
            target = self.get_vertex(target)
        edges = start.edges

        path_list = np.array([edge for edge in edges if edge.left == target or edge.right == target])
        return path_list

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

    @classmethod
    def from_numpy(cls, array: list, undirected: bool = True, weighted_graph: bool = True):
        return cls(array=array, undirected=undirected, weighted_graph=weighted_graph)

    @classmethod
    def from_adjacent_matrix(cls, matrix: np.ndarray, undirected: bool = True, weighted_graph: bool = True):
        """
        Create graph from metrix
        """
        pass
