import heapq
"""

The main goal of this is to find the earliest arrival time from a starting node s to all other nodes in a graph. After that, 
each edge becomes useable only at a specific time. After this, it repeates at every unit of time. in the while loop it reads 4 integer n is the number of nodes,
m is the number of edges,q is the number of queries, 
and s is the starting node. Now we start building the adjacency list , we start by creating a 
list of empty lists one for each node, and the for loop runs a loop m times to read each edge's data. u 
is the source node, 
v is the target node,t0 is the initial departure time,p is the period, and d is the duration. These will be
stored as a tuple in the adjacency list. We get the main Dijkstra loop it starts while the heep isn't empty, 
it pops the node u with the smallest current time from the heap,
and it iterates through all edges from the node Now we calculate the time in both periodic and nonperiodic
cases. We can skip the edges or set the starting departure time t0 P=0 for nonperiodic. The lowest t in the
periodic situation P>0 is found to be t0+t*P>=current_time.
Once every path has been processed, the program returns to requests by declaring "Impossible" if a node 
cannot be reached or the earliest arrival time for each requested node. By carefully monitoring departure times 
and periodic schedules,
Time complexity : O((|m|+|n|)log|n|) here the m are the edges and n is the 
nodes & Space complexity O(|m|+|n|) .


"""

import heapq
from typing import List, Tuple, Optional





def find_shortest_paths_scheduled_transport(n: int, edges: List[Tuple[int, int, int, int, int]], 


                                          source: int) -> Tuple[List[float], List[Optional[int]]]:
                                              
                                              
                                              
    adj = [[] for _ in range(n)]
    
    
    for u, v, t0, P, d in edges:
        
        
        adj[u].append((v, t0, P, d))
    
    INF = float('inf')
    dist = [INF] * n
    predecessor = [None] * n
    dist[source] = 0
    
    heap = [(0, source)]
    
    while heap:
        
        
        
        current_time, u = heapq.heappop(heap)
        
        if current_time > dist[u]:
            continue
        
        
        
        
        for v, t0, P, d in adj[u]:
            if P == 0:
                
                
                if current_time <= t0:
                    departure_time = t0
                else:
                    
                    
                    continue
            else:
                if current_time <= t0:
                    departure_time = t0
                else:
                    
                    
                    
                    periods_passed = (current_time - t0 + P - 1) // P
                    departure_time = t0 + periods_passed * P
            
            arrival_time = departure_time + d
            
            
            
            
            if arrival_time < dist[v]:
                dist[v] = arrival_time
                predecessor[v] = u
                
                
                
                
                
                
                
                
                heapq.heappush(heap, (arrival_time, v))
    
    
    
    
    
    
    
    return dist, predecessor

def reconstruct_path(predecessor: List[Optional[int]], target: int) -> Optional[List[int]]:
    
    
    
    
    
    
    if predecessor[target] is None and target != 0:
        return None
        
        
        
        
        
    
    path = []
    current = target
    
    
    
    
    
    
    
    while current is not None:
        
        
        
        
        
        
        
        path.append(current)
        current = predecessor[current]
    
    
    
    
    
    
    path.reverse()
    
    
    
    
    
    
    return path

def solve_single_case(n: int, m: int, q: int, s: int, 






                     edges: List[Tuple[int, int, int, int, int]], 
                     
                     
                     
                     
                     
                     
                     
                     queries: List[int]) -> List[str]:
                         
                         
                         
                         
                         
    distances, predecessors = find_shortest_paths_scheduled_transport(n, edges, s)
    
    results = []
    
    
    
    
    
    
    
    
    for target in queries:
        
        
        
        
        
        
        
        
        
        
        if distances[target] != float('inf'):
            results.append(str(int(distances[target])))
        else:
            
            
            
            
            
            
            
            results.append("Impossible")
    
    return results






def main():
    
    
    
    
    
    
    
    while True:
        
        
        
        
        
        
        
        n, m, q, s = map(int, input().split())
        
        
        
        
        
        
        
        
        if n == 0 and m == 0 and q == 0 and s == 0:
            break
        
        edges = []
        
        
        
        
        
        
        for _ in range(m):
            u, v, t0, P, d = map(int, input().split())
            
            
            
            
            
            
            
            
            edges.append((u, v, t0, P, d))
        
        queries = []
        
        
        
        
        
        
        
        
        for _ in range(q):
            
            
            
            
            
            
            
            target = int(input())
            queries.append(target)
        
        results = solve_single_case(n, m, q, s, edges, queries)
        
        
        
        
        
        
        for result in results:
            print(result)
        print()
        
        
        
        
        
        

if __name__ == "__main__":
    main()