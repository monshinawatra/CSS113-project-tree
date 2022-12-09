from itertools import chain

import numpy as np

from .edge import Edge
from .vertex import Vertex


class Tree:
    def __init__(
        self,
        structure: list = [],
        weighted_graph: bool = True,
        undirected: bool = True,
    ):
        self.vertices = []
        self.edges = []
        self.undirected = undirected
        self.weighted_graph = weighted_graph

        for node in structure:
            self.add_vertex(node)

        if len(structure):
            self.edges = []
            self._init_edges(structure)

    def _init_edges(self, structure: list):
        for connected in structure:
            names_list = connected[:2]
            weight = connected[2]

            vertices = self.get_vertices(names_list)
            edges = Edge(left=vertices[0], right=vertices[1], weight=weight)

            self.edges.extend([edges])

            for vertex in vertices:
                vertex.update_degrees()

    def add_vertex(self, node):
        self.vertices.extend(
            [
                Vertex(name=node[i], undirected=self.undirected)
                for i in range(2)
                if node[i] not in self.vertices2name(self.vertices)
            ]
        )

    def vertices2name(self, vertices: list):
        return list(map(lambda vertex: vertex.name, vertices))

    def get_vertex(self, name: str):
        for vertex in self.vertices:
            if vertex.name == name:
                return vertex
        return None

    def get_vertices(self, list_name: list):
        return [self.get_vertex(name) for name in list_name]

    def get_vertex_edges(self, name: str):
        return self.get_vertex(name).get_edges()

    def get_adjacent_vertices(self, name: str):
        vertex = self.get_vertex(name)
        adjacent_vertices = [
            (edge.left, edge.right) for edge in vertex.get_edges() if vertex.name in [edge.left.name, edge.right.name]
        ]
        adjacent_vertices = list(set(chain(*adjacent_vertices)))
        adjacent_vertices = [vertex for vertex in adjacent_vertices if vertex.name != name]
        return adjacent_vertices

    def get_smallest_edge(self):
        return min(self.edges, key=lambda edge: edge.weight)

    def add_edge(self, structures: np.ndarray):
        vertices_name = structures[:, :2]
        for name in vertices_name:
            self.add_vertex(name)

        self._init_edges(structures)

    @classmethod
    def from_connected_node(cls, structure: list, undirected: bool = True, weighted_graph: bool = True):
        return cls(structure=structure, undirected=undirected, weighted_graph=weighted_graph)
