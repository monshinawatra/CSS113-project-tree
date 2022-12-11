from typing import Optional


class Edge:
    def __init__(self, left, right, name: Optional[str] = None, weight: float = 0, undirected: bool = False):
        self.name = name
        self.weight = weight
        self.left = left
        self.right = right
        self.undirected = undirected

    def _init_vertices(self):
        self.left.add_edges(self)
        self.right.add_edges(self)

    def get_name(self):
        """
        Get name of edge
        """
        if self.name == None:
            return f"{self.left.name}-{self.right.name}_{id(self.name)}"
        return self.name

    def get_vertices(self):
        """
        Get vertices of edge
        """
        return self.left, self.right

    def is_connected_to(self, name: str):
        """
        Check if edge is connected to vertex
        """
        return True if name in [self.left.name, self.right.name] else False
