from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import networkx as nx
import numpy as np
from tree.graph import UndirectedGraph
import prim_algorithm

def visualization(graph,answer:list(tuple())):
    graph_array=graph.to_numpy()
    numpy_to_list=graph_array.tolist()
    G = nx.Graph()
    fig, ax = plt.subplots()
    for i in numpy_to_list:
        eval(f'G.add_edge("{i[0]}", "{i[1]}", weight={i[2]})')
    pos = nx.spring_layout(G,seed=None)
    nx.draw_networkx_nodes(G, pos, node_size=500, ax=ax)
    nx.draw_networkx_edges(G, pos, width=4)
    nx.draw_networkx_labels(G, pos,font_size=10, font_family="sans-serif")
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels)
    G = nx.DiGraph()
    def update(frame):
        nx.draw_networkx_nodes(G, pos, node_size=500, ax=ax)
        nx.draw_networkx_edges(G, pos, width=4)
        nx.draw_networkx_edges(G, pos, edgelist=frame,edge_color='r', width=4, ax=ax)
    ani = FuncAnimation(fig,update,frames=[[i] for i in answer],interval=1500)
    plt.show()

graph_array1 = np.array(
    [
        ("A", "B", 4),
        ("A","H",8),
        ("B", "C", 8),
        ("B", "H", 11),
        ("C", "I", 2),
        ("C", "D", 7),
        ("C", "F", 4),
        ("D", "E", 9),
        ("D","F",14),
        ("E", "F", 10),
        ("F","G",2),
        ("G","I",6),
        ("G","H",1),
        ("H","I",7)
    ]
)

graph = UndirectedGraph.from_numpy(array=graph_array1, weighted_graph=True)

visualization(graph,prim_algorithm("B",graph,onlyanswer=True)) 

#how to use 
# visualization(graph,answer like = [('A', 'B'), ('A', 'H'), ('H', 'G'), ('G', 'F'), ('F', 'C'), ('C', 'I'), ('C', 'D'), ('D', 'E')])



