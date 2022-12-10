from itertools import chain

import numpy as np

from .edge import Edge
from .vertex import Vertex


class Graph:
    def __init__(
        self,
        array: np.ndarray = np.empty((0,)),
        weighted_graph: bool = True,
        undirected: bool = True,
    ):
        self.vertices = np.empty((0,))
        self.edges = np.empty((0,))
        self.undirected = undirected
        self.weighted_graph = weighted_graph

        if len(array):
            self.add_vertex(array[:, :2])
            self._init_edges(array)

    def _init_edges(self, array: np.ndarray) -> None:
        """
        Init edges from array
        Args:
            array: [('A', 'B', 2), ('A', 'C', 5), ('A', 'C', 4)]
        """
        names_list: np.ndarray = array[:, :2]
        weights = array[:, 2]

        get_name = np.vectorize(lambda x: self.get_vertex(x))
        create_edges = np.vectorize(lambda x, y, z: Edge(left=x, right=y, weight=z, undirected=self.undirected))
        update_degrees = np.vectorize(lambda x: x.update_degrees())

        vertices = get_name(names_list)
        edges = create_edges(vertices[:, 0], vertices[:, 1], weights)

        for edge in edges:
            edge._init_vertices()

        self.edges = np.append(self.edges, edges)
        update_degrees(vertices)

    def add_vertex(self, vertices_name: list) -> None:
        """
        Add unique vertex to tree
        """
        all_names = self.vertices2name(self.vertices)
        create_vertex = np.vectorize(lambda x: Vertex(name=x, undirected=self.undirected))
        vertices = create_vertex(np.setdiff1d(vertices_name, all_names))
        self.vertices = np.append(self.vertices, vertices)

    def add_edge(self, arrays: np.ndarray):
        """
        Add edge to tree
        """
        vertices_name = arrays[:, :2]
        for name in vertices_name:
            self.add_vertex(name)

        self._init_edges(arrays)

    def get_vertex(self, name: str):
        """
        Get vertex by name
        """
        for vertex in self.vertices:
            if vertex.name == name:
                return vertex
        return None

    def get_vertices(self, list_name: list):
        """
        Get vertices by name
        """
        return [self.get_vertex(name) for name in list_name]

    def get_smallest_edge(self):
        """
        Get the smallest edge in tree
        """
        return min(self.edges, key=lambda edge: edge.weight)

    def get_adjacent_vertices(self, name: str):
        """
        Get adjacent vertices by name
        """
        vertex = self.get_vertex(name)
        adjacent_vertices = [
            (edge.left, edge.right) for edge in vertex.get_edges() if vertex.name in [edge.left.name, edge.right.name]
        ]
        adjacent_vertices = list(set(chain(*adjacent_vertices)))
        adjacent_vertices = [vertex for vertex in adjacent_vertices if vertex.name != name]
        return adjacent_vertices

    @classmethod
    def from_numpy(cls, array: list, undirected: bool = True, weighted_graph: bool = True):
        return cls(array=array, undirected=undirected, weighted_graph=weighted_graph)

    @classmethod
    def vertices2name(cls, vertices: list):
        """
        Return list of vertices name
        """
        return list(map(lambda vertex: vertex.name, vertices))
