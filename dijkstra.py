import numpy as np

from tree.graph import UndirectedGraph

DEFAULT_VALUE = [float("inf"), None]


def get_weight(path_length: dict, key: str) -> float:
    return path_length.get(key, DEFAULT_VALUE)[0]


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

dijkstra_config = {
    "start": "A",
    "target": "F",
}

path_length = {
    dijkstra_config["start"]: [0, dijkstra_config["start"]],
}
unupdate_path = [vertex.name for vertex in graph.vertices]
while len(unupdate_path):
    current_vertex = min(unupdate_path, key=lambda x: get_weight(path_length, x))

    adjacenct_vertex = UndirectedGraph.vertices2name(graph.get_adjacent_vertices(current_vertex))
    for adj in adjacenct_vertex:
        if adj == dijkstra_config["start"]:
            continue
        edge = min(graph.get_edge_to(current_vertex, adj), key=lambda x: x.weight)

        new_path = get_weight(path_length, current_vertex) + float(edge.weight)
        old_path = get_weight(path_length, adj)
        if new_path > old_path:
            continue
        path_length[adj] = [new_path, current_vertex]
    unupdate_path.remove(current_vertex)


smallest_path = [dijkstra_config["start"], dijkstra_config["target"]]
target = path_length[dijkstra_config["target"]]
smallest_weight = target[0]
current_path = target[1]
while current_path != dijkstra_config["start"]:
    smallest_path.insert(1, current_path)
    current_path = path_length[current_path][1]
print(smallest_path, smallest_weight)
