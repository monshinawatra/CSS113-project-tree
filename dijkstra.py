from typing import Dict, List

import numpy as np

from tree.graph import UndirectedGraph
from tree.tree import Tree

DEFAULT_VALUE = [float("inf"), None]
DIJKSTRA_CONFIG = {
    "start": "A",
    "target": "F",
}


def get_weight(path_length: Dict[float, str], key: str) -> float:
    return path_length.get(key, DEFAULT_VALUE)[0]


def get_travel_node(order_path: List):
    travel_node = [(order_path[i], order_path[i + 1]) for i in range(len(order_path) - 1)]
    return travel_node


graph_array = np.array(
    [
        ("A", "B", 4),
        ("A", "C", 5),
        ("B", "C", 11),
        ("B", "D", 9),
        ("B", "E", 7),
        ("C", "E", 3),
        ("D", "E", 13),
        ("D", "F", 2),
        ("E", "F", 6),
    ]
)
graph = UndirectedGraph.from_numpy(array=graph_array, weighted_graph=True)
unupdate_path = Tree.vertices2name(graph.vertices)
path_length = {
    DIJKSTRA_CONFIG["start"]: [0, DIJKSTRA_CONFIG["start"]],
}

start = DIJKSTRA_CONFIG["start"]
target = DIJKSTRA_CONFIG["target"]

while len(unupdate_path):
    current_vertex = min(unupdate_path, key=lambda x: get_weight(path_length, x))

    adjacenct_vertex = Tree.vertices2name(graph.get_adjacent_vertices(current_vertex))
    for adj in adjacenct_vertex:
        if adj == start:
            continue
        edge = min(graph.get_edge_to(current_vertex, adj), key=lambda x: x.weight)

        new_path = get_weight(path_length, current_vertex) + float(edge.weight)
        old_path = get_weight(path_length, adj)
        if new_path > old_path:
            continue
        path_length[adj] = [new_path, current_vertex]
    unupdate_path.remove(current_vertex)

shortest_path = [start]
current_node = target
while current_node != start:
    shortest_path.insert(1, current_node)
    current_node = path_length[current_node][1]


print(shortest_path, smallest_weight := path_length[target][0])
print(get_travel_node(shortest_path))
