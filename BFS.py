import numpy as np
from tree.graph import UndirectedGraph

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

graph = UndirectedGraph.from_numpy(array=graph_array, weighted_graph=False)
bfs_config = {"first": "A",} 
all_vertex = [vertex.name for vertex in graph.vertices]
queue = []
path = []
queue.append(all_vertex[0])
adj = UndirectedGraph.vertices2name(graph.get_adjacent_vertices(queue[0]))
path.append(all_vertex[0])
while queue != []:
    adj = UndirectedGraph.vertices2name(graph.get_adjacent_vertices(queue[0]))
    while adj != []:
        for i in adj:
            if i not in path:
                queue.append(i)
                path.append(i)
                adj.remove(i)
            else:
                adj.remove(i)
    queue.remove(queue[0]) 

print(path)       




