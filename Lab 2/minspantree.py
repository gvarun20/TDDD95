#class UnionFind:
#    def __init__(self, size):
#        self.parent = [...]
#        self.rank = [...]
#

"""
Here it takes an integer of a size and which tells the numberof the elements
that needs to be managed in the disjoint set union.
It creates a list parent_node ,where the element at first is its own parent ,this tells that each
element is its owm set at first 
created a list called rank_values with zero ,the rank is utilized to keep the tree small 
while performing union operation.

"""


def initialize_dsu(size: int) -> tuple[list[int], list[int]]:
    
    parent_nodes = [i for i in range(size + 1)]
    rank_values = [0] * (size + 1)
    
    
    return parent_nodes, rank_values










#    def find(self, x):
#        # Path compression
#        pass
#


"""
The input node is the element that we need to look for the root
parent_list is a list that keeps  a record of the every  element’s parent.
the condition looks for the node is its own parent or not ,
if it is true then the node is the root of its set.
If not, it means the node is connected to some other node
this calls continously until it finally finds the root
"""

def find_root(node: int, parent_list: list[int]) -> int:
    
    
    if node == parent_list[node]:
        return node
        
    parent_list[node] = find_root(parent_list[node], parent_list)
    
    return parent_list[node]









#    def union(self, x, y):
#        # Union by rank
#        pass

"""
It first finds the root of each node using find_root() and then it does  path compression.
If both nodes already belong to the same set it tells its already connected.If belong to different set, it does  a union.
The root with lower rank is attached to the root with higher rank

"""

def union_sets(x_node: int, y_node: int, parent_list: list[int], rank_list: list[int]):
    
    
    
    x_root = find_root(x_node, parent_list)
    y_root = find_root(y_node, parent_list)

    if x_root != y_root:
        
        
        if rank_list[x_root] < rank_list[y_root]:
            x_root, y_root = y_root, x_root
            
            
        parent_list[y_root] = x_root
        
        
        
        if rank_list[x_root] == rank_list[y_root]:
            rank_list[x_root] += 1











#
#def solve():
#    while True:
#        n, m = read_input()
#        if n == 0 and m == 0:
#            break


"""
here the function is  generally  in graph algorithms to look 
if there's a connection or path between two nodes.
"""
def are_connected(x_node: int, y_node: int, parent_list: list[int]) -> bool:
    
    
    return find_root(x_node, parent_list) == find_root(y_node, parent_list)
















#
#        edges = []
#        for _ in range(m):
#            u, v, w = read_edge()
#            if u > v:
#                u, v = v, u
#            edges.append((w, u, v))

"""
The function compute_mst computes a Minimum Spanning Tree (MST) of a graph using Kruskal’s algorithm.
It initializes an empty list mst_edges to store the edges.The edges are sorted in increasing order of weight.
checks if src and dest are already connected using are_connected().If not connected, the edge is added to mst_edges.
the output might be a list of edges that form the Minimum Spanning Tree — the smallest set of edges that connect 
all nodes with the minimum total weight and no cycles.


"""

def compute_mst(edge_list: list[tuple[int, int, int]], node_count: int) -> list[tuple[int, int, int]]:
    
    
    
    mst_edges = []
    parent_data, rank_data = initialize_dsu(node_count)
    sorted_edges = sorted(edge_list)



    for weight, src, dest in sorted_edges:
        
        
        if not are_connected(src, dest, parent_data):
            
            
            mst_edges.append((weight, src, dest))
            union_sets(src, dest, parent_data, rank_data)

    return mst_edges










#
#        edges.sort()  # Sort by weight
#
#        uf = UnionFind(n)
#        mst_edges = []
#        total_cost = 0













#
#        for w, u, v in edges:
#            if uf.union(u, v):
#                mst_edges.append((u, v))













#                total_cost += w
#                if len(mst_edges) == n - 1:
#                    break
#











#        if len(mst_edges) != n - 1:
#            print("Impossible")
#        else:











#            print(total_cost)
#            mst_edges.sort()
#            for u, v in mst_edges:
#                print(u, v)



"""

Time Complexity: O(m * log m)
Where: n is the number of vertices::: m is the number of edges

i read some info from here:: https://en.wikipedia.org/wiki/Kruskal%27s_algorithm#Pseudocode

"""












def main():
    
    
    results = []
    input_data = open(0, "r").read().splitlines()[:-1]
    current_line = 0

    while current_line < len(input_data):
        nodes, edges_count = map(int, input_data[current_line].split())
        current_line += 1
        graph_edges = []

        for _ in range(edges_count):
            u, v, weight = map(int, input_data[current_line].split())
            graph_edges.append((weight, u, v))
            current_line += 1

        spanning_tree = compute_mst(graph_edges, nodes)

        if len(spanning_tree) < nodes - 1:
            results.append("Impossible")
            continue

        results.append(str(sum(w for w, _, _ in spanning_tree)))
        
        formatted_edges = [(u, v) if u < v else (v, u) for _, u, v in spanning_tree]
        for u, v in sorted(formatted_edges):
            results.append(f"{u} {v}")









    open(1, "w").write("\n".join(results))

if __name__ == "__main__":
    main()








