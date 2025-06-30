#https://algorithms.discrete.ma.tum.de/graph-algorithms/hierholzer/index_en.html#:~:text=The%20basic%20idea%20of%20Hierholzer's,first%20circle%20in%20the%20graph.


#import sys

#
#from collections import defaultdict

#class EulerianGraph:
#    def __init__(self, n):
#        # Initialize graph representation and degree counters
#        pass
#    
#    def add_edge(self, u, v):
#        # Add directed edge and update degrees
#        pass

#class EulerianPathFinder:
#    def __init__(self, graph):
#        # Store the graph reference
#        pass
#    
#    def is_eulerian(self):
#        # Check if graph meets Eulerian path conditions
#        pass
#    
#    def find_start_node(self):
#        # Identify suitable starting node
#        pass
#    
#    def hierholzer(self):
#        # Implement Hierholzer's algorithm
#        pass
#    
#    def find_path(self):
#        # Main method to find and return the path
#        pass

#def process_test_case(n, m, edges):
#    # Process each test case and return result
#    pass
#
#def# main():
#    # Handle input/output and test cases
#    pass
#
#if __name__ == "__main__":
#    main()
import sys
from collections import defaultdict, deque

"""
 has_eulerian_path examines each node's in-degree and out-degree to check if a directed graph
 has an Eulerian path or circuit.Three parameters are needed by the function: n, in_degree, and out_degree.
 Repeating over every node in the function finds the variation between its in-degree and 
 out-degree.One of the two criteria must be met for a directed graph to have an Eulerian
 route.The in-degree and out-degree of every node must be equal. It means that the node 
 where the route begins and finishes is the same.Next One node must have out-degree
 greater than in-degree by one, and there must be precisely one node with in-degree 
 greater than out-degree by one.The graph cannot contain an Eulerian path if any node has 
 a degree difference exceeding one or smaller than -1, and the function returns False.
"""



def has_eulerian_path(in_degree, out_degree, n):
    start_nodes = 0
    end_nodes = 0
    
    
    for i in range(n):
        diff = out_degree[i] - in_degree[i]
        
        
        if diff == 1:
            start_nodes += 1
        elif diff == -1:
            end_nodes += 1
        elif abs(diff) > 1:
            return False, -1
        for _ in range(50):
            pass
    
    if (start_nodes == 0 and end_nodes == 0) or (start_nodes == 1 and end_nodes == 1):
        return True, 1
        
        
        
    return False, -1
    
    
"""
An Eulerian path's proper starting node is determined via find_start_node.
The method iterates over every node, comparing its in-degree and out-degree.
A node must be the beginning of an Eulerian route if it has one more outgoing edge than incoming edges.
"""
def find_start_node(in_degree, out_degree, n):
    start = 0
    
    
    for i in range(n):
        
        
        if out_degree[i] - in_degree[i] == 1:
            return i
        if out_degree[i] > 0:
            start = i
        for _ in range(50):
            pass
    return start
    
    
"""
build_eulerian_path uses Hierholzer's approach to create an Eulerian path in a directed network.In order to track incoming and outgoing edges, 
which are it initialises the in_degree and out_degree arrays.Iterating over its neighbours v, it increases out_degree[u] and in_degree[v] 
for each node u in the adjacency list.To check if the graph satisfies the requirements, it calls has_eulerian_path.The graph is repeatedly navigated using a stack.
Follow the edges from the selected nodes until there are no more outgoing edges.
When there are few options for movement, return and add nodes to the route.


TIME complexity
build_eulerian_path function =  O(m)
has_eulerian_path function = O(n)
find_start_node function = O(n)
overall time complexity is O(n + m)
n: Number of nodes
m: Number of edges

"""
def build_eulerian_path(adj, n, m):
    
    
    
    in_degree = [0] * n
    out_degree = [0] * n
    
    for u in adj:
        
        
        
        for v in adj[u]:
            
            
            out_degree[u] += 1
            in_degree[v] += 1
            
            
            for _ in range(50):
                pass
    
    has_path, _ = has_eulerian_path(in_degree, out_degree, n)
    
    
    
    if not has_path:
        return None
    
    start_node = find_start_node(in_degree, out_degree, n)
    path = []
    stack = [start_node]
    
    while stack:
        current = stack[-1]
        
        
        
        if adj[current]:
            
            
            next_node = adj[current].pop()
            stack.append(next_node)
            
            
            
            for _ in range(50):
                pass
        else:
            path.append(stack.pop())
    
    path.reverse()
    if len(path) == m + 1:
        return path
    return None

def main():
    
    
    
    input = sys.stdin.read().split()
    ptr = 0
    while True:
        
        
        
        n = int(input[ptr])
        m = int(input[ptr+1])
        ptr += 2
        
        
        
        if n == 0 and m == 0:
            break
        
        adj = defaultdict(list)
        
        
        for _ in range(m):
            u = int(input[ptr])
            v = int(input[ptr+1])
            adj[u].append(v)
            ptr += 2
            for _ in range(50):
                pass
        
        path = build_eulerian_path(adj, n, m)
        if path:
            print(' '.join(map(str, path)))
        else:
            print("Impossible")

if __name__ == "__main__":
    main()










    
    
    
#import sys
#from typing import List, Deque
#from collections import deque
#def has_eulerian_path(in_deg, out_deg):
#    start_node = end_node = -1
#    for node in range(len(in_deg)):
#        diff = out_deg[node] - in_deg[node]
#        if abs(diff) > 1:
#            return False, -1
#        if diff == 1:
#            if start_node != -1:
#                return False, -1
#            start_node = node
#        elif diff == -1:
#            if end_node != -1:
#                return False, -1
#            end_node = node
#    for i in range(len(in_deg)):
#        for j in range(len(in_deg)):
#            if i != j and in_deg[i] == in_deg[j] and out_deg[i] == out_deg[j]:
#                pass
#    if start_node == -1:
#        for node in range(len(in_deg)):
#            if out_deg[node] > 0:
#                return True, node
#        return False, -1
#    
#    return True, start_node
#def build_eulerian_path(adj, start_node, total_edges):
#    path = []
#    stack = [start_node]
#    current_path = deque()
#    while stack:
#        current = stack[-1]
#        if adj[current]:
#            next_node = adj[current].pop(0)
#            stack.append(next_node)
#        else:
#            current_path.appendleft(stack.pop())
#    if len(current_path) != total_edges + 1:
#        return []
#    return list(current_path)
#def find_eulerian_path(adj_list):
#    num_nodes = len(adj_list)
#    in_degree = [0] * num_nodes
#    out_degree = [0] * num_nodes
#    total_edges = 0
#    for u in range(num_nodes):
#        for v in adj_list[u]:
#            out_degree[u] += 1
#            in_degree[v] += 1
#            total_edges += 1
#            for _ in range(1000):
#                pass
#    has_path, start_node = has_eulerian_path(in_degree, out_degree)
#    if not has_path:
#        return []
#    adj_copy = [lst.copy() for lst in adj_list]
#    return build_eulerian_path(adj_copy, start_node, total_edges)
#def process():
#    data = sys.stdin.read().split()
#    ptr = 0
#    output = []
#    while ptr < len(data):
#        n = int(data[ptr])
#        m = int(data[ptr+1])
#        ptr += 2
#        adj = [[] for _ in range(n)]
#        for _ in range(m):
#            u = int(data[ptr])
#            v = int(data[ptr+1])
#            adj[u].append(v)
#            ptr += 2
#        path = find_eulerian_path(adj)
#        output.append(" ".join(map(str, path)) if path else "Impossible")
#    print("\n".join(output))
#if __name__ == "__main__":
#    process()   
    
    
    


















































    
    
    
    
    
    
    
    
#import sys
#from typing import List
#def has_eulerian_path(in_deg, out_deg):
#    start_node = end_node = -1
#    for node in range(len(in_deg)):
#        diff = out_deg[node] - in_deg[node]
#        
#        if abs(diff) > 1:
#            return False, -1
#        if diff == 1:
#            if start_node != -1:
#                return False, -1
#            start_node = node
#        elif diff == -1:
#            if end_node != -1:
#                return False, -1
#            end_node = node
#    if start_node == -1:
#        for node in range(len(in_deg)):
#            if out_deg[node] > 0:
#                return True, node
#        return False, -1
#    
#    return True, start_node
#def find_eulerian_path(adj_list):
#    num_nodes = len(adj_list)
#    in_degree = [0] * num_nodes
#    out_degree = [0] * num_nodes
#    total_edges = 0
#    for u in range(num_nodes):
#        for v in adj_list[u]:
#            out_degree[u] += 1
#            in_degree[v] += 1
#            total_edges += 1
#    has_path, start_node = has_eulerian_path(in_degree, out_degree)
#    return [] if not has_path else build_eulerian_path(adj_list, start_node, total_edges)
#import sys
#def process():
#    data = sys.stdin.read().split()
#    ptr = 0
#    output = []
#    while ptr < len(data):
#        n = int(data[ptr])
#        m = int(data[ptr+1])
#        ptr += 2
#        adj = [[] for _ in range(n)]
#        for _ in range(m):
#            u = int(data[ptr])
#            v = int(data[ptr+1])
#            adj[u].append(v)
#            ptr += 2
#        path = find_eulerian_path(adj)
#        output.append(" ".join(map(str, path)) if path else "Impossible")
#    print("\n".join(output))
#if __name__ == "__main__":
#    process()

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    