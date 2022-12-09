class Edge:
    def __init__(self, left, right, name: str = "", weight: int = 0, directed: bool = False):
        self.weight = weight
        self.left = left
        self.right = right
        self.directed = directed

        if not len(name):
            self.name = id(self)

        self._init_vertices()

    def _init_vertices(self):
        self.left.add_edges([self])
        self.right.add_edges([self])

    def get_vertices(self):
        return self.left, self.right

    def is_connected_to(self, name: str):
        return True if name in [self.left.name, self.right.name] else False
