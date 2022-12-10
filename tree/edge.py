class Edge:
    def __init__(self, left, right, name: str = "", weight: float = 0, undirected: bool = False):
        self.weight = weight
        self.left = left
        self.right = right
        self.undirected = undirected

        if not len(name):
            self.name = id(self)

    def _init_vertices(self):
        self.left.add_edges(self)
        self.right.add_edges(self)

    def get_vertices(self):
        return self.left, self.right

    def is_connected_to(self, name: str):
        return True if name in [self.left.name, self.right.name] else False
