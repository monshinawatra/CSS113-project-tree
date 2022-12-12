import numpy as np
from tree.graph import UndirectedGraph

def prim_algorithm(first_vertex:str,graph:UndirectedGraph,onlyanswer=False):
    first=first_vertex
    all_vertex=[v.name for v in graph.vertices]
    ans = {}
    counter=0
    differ = {} #ไว้เช็คว่าตัวไหนน้อยที่สุด, find minimum in dictionary
    check_if_it_have =  [] #check what vertex have been gone
    while counter<len(all_vertex)-1:
        checklist=graph.vertices2name(graph.get_adjacent_vertices(first)) #ตัวที่Aพุ่งไปหาได้ ['B', 'C'] , check what vertex A can go
        different_checklist = set(checklist)-set(check_if_it_have) #checkตัวที่ยังไม่เคยไป ['B', 'C'], check what vertex isn't go 
        check_if_it_have.append(first) #add for check what vertex have been gone
        if ((list(different_checklist)) == [] and (len(check_if_it_have)!=len(all_vertex))):
            checklist=graph.vertices2name((graph.get_adjacent_vertices(check_if_it_have[-2])))
            different_checklist = set(checklist)-set(check_if_it_have)
            first=check_if_it_have[-2]
        for adj in list(different_checklist):
            edge = graph.get_edge_to(first, adj)
            min_edge_if_have_parallel=min(edge,key=lambda x: x.weight).weight #find the minimum if there have parallel
            differ.update({(first,adj):min_edge_if_have_parallel})
        passlist=[]
        for k,v in differ.items():
            if (k[0] and k[1]) not in check_if_it_have:
                passlist.append((k[0],k[1],v))
        minpasslist=min(passlist,key=lambda x:x[2])
        min_vertex = (minpasslist[0],minpasslist[1])
        ans.update({min_vertex:differ[min_vertex]})
        differ.pop(min_vertex)#remove min in dictionary
        first = min_vertex[1] #the first str is change into adjectcent str
        counter += 1

    return((f"answer is {ans} and total weight is {sum(ans.values())}") if onlyanswer == False else (list(ans.keys())))

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

print(prim_algorithm("B",graph))
print(prim_algorithm("B",graph,onlyanswer=True))