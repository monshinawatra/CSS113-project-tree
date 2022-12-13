import numpy as np
from tree.graph import UndirectedGraph

def bfs(first:str,graph):
    queue = []
    path = []
    result = []
    queue.append(first)     # add the start node to queue
    path.append(first)      # add the start node to path
    
    while queue != []:      # loop until queue empty
        adj = UndirectedGraph.vertices2name(graph.get_adjacent_vertices(queue[0]))  # get adjacent vertices in queue[0]
        while adj != []:                            # loop until no adjacent vertices in queue[0]
            for i in adj:   
                if i not in path:                   # if adjacent vertices not in path then 
                    queue.append(i)                 # add to queue
                    path.append(i)                  # add to path
                    result.append((queue[0], i))    # add to result as tuple from queue[0] to adj[i]
                    adj.remove(i)                   # remove from adj
                else:
                    adj.remove(i)                   # remove from adj if in path already
        queue.remove(queue[0])                      # remove from queue
    return result                                   # return result 


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

print(bfs("F", graph))       




