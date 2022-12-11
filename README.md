```python
import numpy as np

from tree.graph import UndirectedGraph

graph_array = np.array(
    [
        ["A", "B", 4],
        ["A", "C", 5],
        ["B", "C", 11],
        ["B", "D", 9],
        ["B", "E", 7],
        ["C", "E", 3],
        ["D", "E", 13],
        ["D", "F", 2],
        ["E", "F", 6],
    ]
)
undirected_graph = UndirectedGraph.from_numpy(graph_array, weighted_graph=True)
for vertex in undirected_graph.vertices:
    print(vertex.name)
    print(*[(edge.left.name, edge.right.name, edge.weight) for edge in vertex.edges])

print()
print(undirected_graph.get_edge_to("E", "B")[0].weight)
print("Smallest edge", undirected_graph.get_smallest_edge().weight)
print("Adjacent", UndirectedGraph.vertices2name(undirected_graph.get_adjacent_vertices("A")))

```
