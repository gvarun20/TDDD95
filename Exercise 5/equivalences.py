#import sys
#from collections import defaultdict, deque
#
#
#
#    # Read all input data at once for efficiency
## Parse the number of test cases
## Initialize a list to store results for each test case
#
## Loop through each test case
#    # Read the number of statements and the number of already proven implications
#    # Initialize an adjacency list to represent the directed graph
#
#    # Read each implication and add it to the adjacency list
#        # Add a directed edge from u to v
#
#
#
#
#
#
#
#
#
#
#def main():
#    input = sys.stdin.read
#    data = input().split()
#    idx = 0
#    T = int(data[idx])  # Number of test cases
#    idx += 1
#    results = []
#    
#    
#    
#    
#    
#    
#    
#    
#    
#    
#    
#    
#    
#    
#    
#    
#    
#    for _ in range(T):
#        n = int(data[idx])  # Number of statements
#        m = int(data[idx+1])  # Number of already proven implications
#        idx += 2
#        
#        adj = defaultdict(list)  # Adjacency list for the graph
#        for _ in range(m):
#            u = int(data[idx])  # Statement u implies statement v
#            v = int(data[idx+1])
#            adj[u].append(v)
#            idx += 2
#        
#        visited = [False] * (n + 1)  # Visited array for DFS
#        stack = deque()
#        
#        
#        
#        
#        
#        
#        
#        
#        
#        
#        
#        
#        
#        
#        def dfs(u):
#            stack.append(u)
#            visited[u] = True
#            for v in adj[u]:
#                if not visited[v]:
#                    dfs(v)
#        
#        
#        
#        
#        
#        
#        
#        
#        
#        
#        
#        
#        
#        
#        
#        
#        dfs(1)  # Perform DFS starting from the first node
#        
#        if not all(visited[1:]):  # Check if all nodes were visited
#            results.append(n - 1)  # If not, n-1 additional edges are needed
#            continue
#        
#        
#        
#        
#        
#        
#        
#        
#        
#        
#        
#        
#        
#        
#        
#        
#        adj_transpose = defaultdict(list)  # Transpose of the graph
#        for u in adj:
#            for v in adj[u]:
#                adj_transpose[v].append(u)
#        
#        visited = [False] * (n + 1)  # Reset visited array
#        stack = deque()
#        
#        
#        
#        
#        
#        
#        
#        
#        
#        def dfs_transpose(u):
#            stack.append(u)
#            visited[u] = True
#            for v in adj_transpose[u]:
#                if not visited[v]:
#                    dfs_transpose(v)
#        
#        dfs_transpose(1)  # Perform DFS on the transposed graph starting from the first node
#        
#        
#        
#        
#        
#        
#        
#        
#        
#        
#        
#        if not all(visited[1:]):  # Check if all nodes were visited in the transposed graph
#            results.append(n - 1)  # If not, n-1 additional edges are needed
#        else:
#            results.append(0)  # Otherwise, no additional edges are needed
#    
#    
#
#
#    # Initialize a visited array to keep track of visited nodes
#    # Use a stack for DFS traversal
#
#    # Define a DFS function to traverse the graph
#        # Mark the current node as visited and add it to the stack
#        # Recursively visit all unvisited neighbors
#
#    
#    
#    
#    
#    for result in results:
#        print(result)  # Print the results for each test case
#
#
#
#
#
#
#    # Perform DFS starting from the first node
#    # Check if all nodes were visited
#        # If not, the graph is not strongly connected, and n-1 additional edges are needed
#        # Continue to the next test case
#
#    # Create the transpose of the graph (reverse all edges)
#    # Reset the visited array
#
#    # Define a DFS function for the transposed graph
#        # Mark the current node as visited and add it to the stack
#        # Recursively visit all unvisited neighbors in the transposed graph
#
#    # Perform DFS on the transposed graph starting from the first node
#    # Check if all nodes were visited
#        # If not, the graph is not strongly connected, and n-1 additional edges are needed
#        # Otherwise, no additional edges are needed
#
## Print the results for each test case
#    
#    
#    
#
#
#
#if __name__ == "__main__":
#    main()

"""


"""

def traverse(node, graph, seen, result):
    
    
    seen[node] = True
    
    
    
    for neighbor in graph[node]:
        
        
        
        if seen[neighbor]:
            continue
        
        
        
        traverse(neighbor, graph, seen, result)
        
        
        
    result.append(node)
    
    
"""
"""
    
    

def find_components(graph):
    
    
    
    
    
    
    n = len(graph)
    seen = [False] * n
    finish_order = []
    
    for i in range(n):
        
        
        
        
        
        if seen[i]:
            continue
        temp = []
        
        
        
        
        traverse(i, graph, seen, temp)
        finish_order.extend(temp)
    
    reverse_graph = [[] for _ in range(n)]
    
    
    
    
    
    for i in range(n):
        
        
        
        
        for j in graph[i]:
            
            
            
            reverse_graph[j].append(i)
    
    seen = [False] * n
    component_roots = []
    node_to_root = [0] * n
    
    for node in reversed(finish_order):
        
        
        
        
        if seen[node]:
            continue
        component = []
        
        
        
        
        
        
        traverse(node, reverse_graph, seen, component)
        root = min(component)
        component_roots.append(root)
        
        
        
        
        for v in component:
            node_to_root[v] = root
    
    new_graph = [[] for _ in range(n)]
    
    
    
    
    
    for i in range(n):
        for j in graph[i]:
            
            
            
            
            
            
            if node_to_root[i] == node_to_root[j]:
                continue
            
            
            
            
            
            new_graph[node_to_root[i]].append(node_to_root[j])
    
    return component_roots, new_graph
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    






"""
"""




def min_edges_needed(graph):
    
    
    
    
    roots, condensed = find_components(graph)
    
    if len(roots) == 1:
        return 0
    
    has_in = [False] * len(roots)
    has_out = [False] * len(roots)
    
    for idx, root in enumerate(roots):
        
        
        
        
        
        if len(condensed[root]) > 0:
            has_out[idx] = True
            
            
            
            
            
        for target in condensed[root]:
            
            
            
            
            target_idx = roots.index(target)
            has_in[target_idx] = True
    
    no_in = sum(1 for x in has_in if not x)
    no_out = sum(1 for x in has_out if not x)
    
    
    
    
    
    return max(no_in, no_out)
































if __name__ == "__main__":
    
    
    
    
    import sys
    sys.setrecursionlimit(50000)
    
    answers = []
    lines = open(0, "r").read().splitlines()[1:]
    pos = 0
    
    while pos < len(lines):
        
        
        
        
        
        n, m = map(int, lines[pos].split())
        pos += 1
        
        adj = [[] for _ in range(n)]
        
        
        
        
        
        for _ in range(m):
            a, b = map(int, lines[pos].split())
            adj[a - 1].append(b - 1)
            pos += 1
            
            
            
            
        
        answers.append(str(min_edges_needed(adj)))
        
        
        
    
    open(1, "w").write("\n".join(answers))





















































