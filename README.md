# CSS113-project-tree

```python
import numpy as np

from tree.graph import UndirectedGraph

structure = np.array([("A", "B", 2), ("A", "C", 5), ("A", "C", 4)])
undirected_graph = UndirectedGraph.from_array(structure, weighted_graph=True)

new_structure = np.array([("C", "D", 0.5)])
undirected_graph.add_edge(new_structure)

for vertex in undirected_graph.vertices:
    print(vertex.name)
    print(*[(edge.left.name, edge.right.name, edge.weight) for edge in vertex.get_edges()])

print()
print("Smallest edge", undirected_graph.get_smallest_edge().weight)
print("Adjacent", undirected_graph.get_adjacent_vertices("D")[0].name)
```
