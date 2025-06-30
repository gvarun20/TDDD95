#import sys
#from collections import deque

#class Graph:
    
    
    
    
    
#    def __init__(self, vertices):
#        self.V = vertices
#        self.graph = [[] for _ in range(vertices)]
#        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
#    def add_edge(self, u, v, w):
#        self.graph[u].append((v, w))

#def min_cut(graph, s, t):
    
    
    
    
    
    
#    n = graph.V
#    parent = [-1] * n
#    max_flow = 0
 #   
    
 #   def bfs():
#        nonlocal parent
#        parent = [-1] * n
#        parent[s] = -2
#        q = deque()
#        q.append(s)
        
        
        
        
        
from collections import deque
import sys


"""
Here, we try setting up Breadth-First Search (BFS) to assign levels to the nodes in a
network flow.The function find_level takes input as the starting node, the adjacency 
list that holds all nodes v connected to node u, and the capacity that tells the maximum 
flow allowed on the edge from node u to v.First, we create a list of size equal to the 
number of nodes. We set all values to -1, indicating that the nodes are unvisited.
Next, we set the level of the source node to 0.We then create a deque and add the source node to it.
The while loop performs the BFS traversal.Inside the loop, we use a for loop to go 
through all neighbors v of node u.There are two conditions to move forward: the node v 
must not have been visited yet (i.e., its level is -1), and the edge from u to v must 
have a positive residual capacity.Once the BFS process is complete, the function returns the 
levels list.

"""
def find_levels(source, adj, capacity, flow):
    
    
    
    levels = [-1] * len(adj)
    levels[source] = 0
    queue = deque([source])
    
    while queue:
        u = queue.popleft()
        
        
        
        for v in adj[u]:
            
            
            if levels[v] == -1 and capacity[u][v] > flow[u][v]:
                levels[v] = levels[u] + 1
                
                
                queue.append(v)
                
                
    return levels








"""
Here we implement the push\_flow function, to compute the maximum flow in a flow
network. The function uses the DFS approach to find the augmenting path and update the flow.
If the current node is the sink this tells the function that it has found a complete 
path from source to sink. Next, it iterates over the neighbors of node ptr\[u] tracks
whose neighbors have already been explored so that it doesn't revisit them. This will 
continue until all neighbors are done. Next, it checks the validity of edges by 2 
conditions. The first is the neighbor must be at the next level in the level graph. 
Secondly, the edge must have a positive residual capacity. We recursively call on the
neighbors to push flow from V to the sink. The min\_flow is updated to the minimum of 
the current min\_flow & residual capacity of the edges. It updates the flow array to
reflect the flow pushed along the augmenting path and adjusts the reverse edge for the
residual graph. The function returns the amount of flow pushed.


"""


def push_flow(u, sink, adj, capacity, flow, levels, ptr, min_flow):
    
    
    if u == sink:
        return min_flow
    
    while ptr[u] < len(adj[u]):
        v = adj[u][ptr[u]]
        
        
        
        if levels[v] == levels[u] + 1 and capacity[u][v] > flow[u][v]:
            pushed = push_flow(v, sink, adj, capacity, flow, levels, ptr, min(min_flow, capacity[u][v] - flow[u][v]))
            
            
            if pushed > 0:
                flow[u][v] += pushed
                flow[v][u] -= pushed
                return pushed
        
        
        
        ptr[u] += 1
        
        
    return 0
    
    
"""   
We create a flow matrix that is set to 0. Flow [u][v] will store how much passes through the edge.
find_levels perform BFS from the source and assign each node a level. It gets updated
the shortest distance and if a sink is unreachable it will exit here.ptr[u] keeps track of which 
edges from which edges from nodes have been explored. 
In the next push_flow tried to send as much as possible from source to sink using DFS.



"""
def dinic_max_flow(adj, capacity, source, sink):
    flow = [[0] * len(adj) for _ in range(len(adj))]
    
    while True:
        levels = find_levels(source, adj, capacity, flow)
        
        
        if levels[sink] == -1:
            break
        
        ptr = [0] * len(adj)
        
        
        while push_flow(source, sink, adj, capacity, flow, levels, ptr, float('inf')) > 0:
            pass
    
    return flow



"""
The function find_min_cut looks for the minimum cut in a flow network after iterating
the max_flow_algorithm.At first, it was initialized and visited to track which nodes
have been processed. Stack uses DFS and starts with the source node. In the while loop,
DFS traverses to find the reachable node .u takes the last node from the stack and the
loop checks for all the neighbor nodes. We have two conditions here first we ensure we do not
reprocess the same node, and we ensure the edge has residual capacity.


"""
    

def find_min_cut(adj, capacity, flow, source):
    
    
    
    visited = [False] * len(adj)
    stack = [source]
    visited[source] = True
    reachable = [source]
    
    while stack:
        u = stack.pop()
        
        
        for v in adj[u]:
            
            
            if not visited[v] and capacity[u][v] > flow[u][v]:
                visited[v] = True
                stack.append(v)
                reachable.append(v)
    
    return reachable
    
"""   
    
time complexity   
O(V² × E)  running in  Dinic's algorithm:

It builds level graphs to V time.

Each level graph allow pushing flow to E edges.

Each push can take up to V steps.

O(V + E) from the DFS used to find the minimum cut nodes after the max flow is found.

So total time might be  = O(V² × E + V + E) = O(V² × E)

"""

if __name__ == "__main__":

    input = sys.stdin.read().split()
    idx = 0
    
    n = int(input[idx]); idx += 1
    m = int(input[idx]); idx += 1
    s = int(input[idx]); idx += 1
    t = int(input[idx]); idx += 1
    
    adj = [[] for _ in range(n)]
    capacity = [[0] * n for _ in range(n)]
    
    for _ in range(m):
        u = int(input[idx]); idx += 1
        v = int(input[idx]); idx += 1
        w = int(input[idx]); idx += 1
        if capacity[u][v] == 0 and capacity[v][u] == 0:
            adj[u].append(v)
            adj[v].append(u)
        capacity[u][v] += w
    
    flow = dinic_max_flow(adj, capacity, s, t)
    min_cut_nodes = find_min_cut(adj, capacity, flow, s)
    
    print(len(min_cut_nodes))
    print('\n'.join(map(str, min_cut_nodes)))
        
        
        
        
        
        
        
        
        
        
        
 #       while q:
 #           u = q.popleft()
 #           for v, w in graph.graph[u]:
 #               
 #               
                
 #               
 #               
 #               
 #               if parent[v] == -1 and w > 0:
 #                   parent[v] = u
 #                   
                    
 #                   
  #                  
  #                  
  #                  
  #                  if v == t:
   #                     return True
  #                     
   #                     
                        
  #                      
       #             q.append(v)
      #  return False
    
    
    
    
    
    #while bfs():
        
        
      #  
        
   #     path_flow = float('inf')
   #     v = t
        
        
      #  
        
 #       while v != s:
  #          u = parent[v]
            
            
            
            
 #           
    #        
  #          for neighbor, w in graph.graph[u]:
     #           
  #              
                
  #              if neighbor == v:
  #                  path_flow = min(path_flow, w)
     #               break
    #            
                
  #              
  #    #      v = u
        
        
     #   
       # 
     #   max_flow += path_flow
      #  v = t
        
        
       # 
        
     #   while v != s:
       #     u = parent[v]
            
            
      #      
           # for i in range(len(graph.graph[u])):
       #         
                
       #         if graph.graph[u][i][0] == v:
       #             graph.graph[u][i] = (v, graph.graph[u][i][1] - path_flow)
       #             break
       #         
         #       
          #  found = False
        #    
            
        #    for i in range(len(graph.graph[v])):
                
                
                
           #     if graph.graph[v][i][0] == u:
        #            graph.graph[v][i] = (u, graph.graph[v][i][1] + path_flow)
            #        found = True
            #        break
                
        #        
        #    if not found:
        #        graph.graph[v].append((u, path_flow))
                
                
                
                
         #   v = u
            
            
    
  #  visited = [False] * n
  #  q = deque()
 # #  q.append(s)
 # #  visited[s] = True
    
    
    
    
 # #  while q:
  # #     u = q.popleft()
        
 # #      
 # #      for v, w in graph.graph[u]:
  # #         
            #
#            if not visited[v] and w > 0:
 # #              visited[v] = True
  # #             q.append(v)
  # #             
                
                
    
 # #  U = [i for i in range(n) if visited[i]]
 # #  return U#
#
#d#ef main():
    
    
    
    
 #   input = sys.stdin.read().split()
#    ptr = 0
#    n = int(input[ptr]); ptr += 1
#    m = int(input[ptr]); ptr += 1
#    s = int(input[ptr]); ptr += 1
#    t = int(input[ptr]); ptr += 1
 #   
    
    
    
 #   g = Graph(n)
    
 #   
    
 #   for _ in range(m):
#        u = int(input[ptr]); ptr += 1
 #       v = int(input[ptr]); ptr += 1
 #       w = int(input[ptr]); ptr += 1
  #      g.add_edge(u, v, w)
        
        
        
        
        
    
  #  U = min_cut(g, s, t)
    
    
    
    
 #   print(len(U))
    
  #  
 #   for node in U:
  #      print(node)

#if __name__ == "__main__":
 #   main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    