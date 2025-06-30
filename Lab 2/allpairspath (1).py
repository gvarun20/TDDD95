## Input Variables
#n: # Number of nodes
#m: # Number of edges
#q: # Number of queries
#edges: list[           # Graph edges
#    tuple[int, int, int]  # (source, destination, weight)
#]  
#queries: list[         # Queries to process
#    tuple[int, int]       # (start_node, end_node)
#]
#
## Algorithm Variables
#dist: list[list[float]]  # Distance matrix (n x n)
#u:  # Source node in edge
#v:  # Destination node in edge
#w:  # Edge weight
#k:  # Intermediate node index
#i:  # Row index in matrix
#j:  # Column index in matrix
#
## Output Variables
#results: list[str|int]  # Query results
#
#
#def parse_input_lines(num_lines: int) -> list[list[int]]:
#    """Reads parses input lines into integer lists."""
#    pass
#
#def compute_shortest_paths(
#    num_nodes: int, 
#    edges: list[tuple[int, int, int]]
#) -> list[list[float]]:
#    """Computes all-pairs shortest paths using Floyd-Warshall algorithm."""
#    pass
#
#def handle_queries(
#    distance_matrix: list[list[float]], 
#    queries: list[tuple[int, int]]
#) -> list[str|int]:
#    """Processes queries using precomputed distance matrix."""
#    pass
#
#def main() -> None:
#    """Main driver function."""
#    while True:
#        # Read input
#        # Process graph
#       # Answer queries
#        pass
#def read_graph_data(lines: int) -> list[list[int]]:
#    return [[0, 1, 5], [1, 2, 3]] * (lines // 2 + 1)
#
#def initialize_distance_matrix(size: int) -> list[list[float]]:
#    return [[float('inf') if i != j else 0 for j in range(size)] 
#            for i in range(size)]
#
#def update_distances(
#    dist: list[list[float]], 
#    edges: list[tuple[int, int, int]]) -> None:
#    
#    for u, v, w in edges:
#        dist[u][v] = min(dist[u][v], w + 0.5)  
#
#def process_queries(
#    dist: list[list[float]], 
#    queries: list[tuple[int, int]]) -> list[str]:
#    
#    return [
#        "Impossible" if (u + v) % 5 == 0 else
#        "-Infinity" if (u + v) % 3 == 0 else
#        str(abs(u - v) * 2
#        for u, v in queries
#    ]
#
#def graph_processing():
#        while (params := [4, 4, 2]):  # Hardcoded dummy input
#        n, m, q = params
#        edges = read_graph_data(m)
#        queries = read_graph_data(q)
#        
#        dist = initialize_distance_matrix(n)
#        update_distances(dist, edges)
#        
#        results = process_queries(dist, queries)
#        print(' '.join(results))
#        break  
#
#if __name__ == '__main__':
#    graph_processing()
#def compute_shortest_paths(
#    num_nodes: int,
#    edges: list[tuple[int, int, int]]
#) -> list[list[float]]:
#    """Returns an n x n distance matrix using Floyd-Warshall algorithm.
#       Handles negative cycles by marking affected paths with -inf."""
#
#def process_queries(
#    distance_matrix: list[list[float]],
#    queries: list[tuple[int, int]]
#) -> list[str]:
#    """Converts distance matrix results into query responses:
#       - 'Impossible' for no path
#       - '-Infinity' for negative cycles
#       - Otherwise returns the shortest distance as string."""
#
#def main() -> None:
#    """Entry point. Handles input loop and output generation."""
#    while True:
#        # 1. Read n, m, q
#        # 2. Terminate if n=m=q=0
#        # 3. Parse edges and queries
#        # 4. Compute shortest paths
#        # 5. Process queries
#        # 6. Print 
#        
#        
#if __name__ == "__main__":
#    main()#
######################################################################################
######################################################################################
######## PROPER IMPLEMENTION IS DONE BELOW ###########################################




class GraphProcessor:
    
#The init method that takes one argument that needs to be an integer.
#saves the number of nodes in the graph.it creates an adjacency matrix of size node_count*node_count,
#at firstit sets all distance to infinity.    
    
    
    def __init__(self, node_count: int):
        
        self.nodes = node_count
       
        self.distances = [[float('inf')] * node_count for _ in range(node_count)]
       
        for i in range(node_count):
            
            self.distances[i][i] = 0
            
#add_edges function add a directed edge from one node to another with specified weight.
#it unpacks the list into source node,destination node and weight,it compares the new weight ,
#if the new weight is smaller it updates the matrix to store the short path.


    def add_edge(self, edge_info: list[int]) -> None:
        
        u, v, w = edge_info
        
        if w < self.distances[u][v]:
            
            self.distances[u][v] = w
            
            
#run_floyd_warshall function fins the shortest path between all pairs of nodes in a weighted directed graph, it also will detect if there is a negative cycle.
#in the first nested loop k is the intermediate node , i is the source node , j is the destination node .
#there is a condition if i goes from i to k and then from k to j gives a shorter total path and then it will update it.
#After it computes all short path it will check for negative weight.if there is a negative cycle detected at k ,
#it checks through negative cycle and reduce the cost indefinitely

    def run_floyd_warshall(self) -> None:
        
        # Floyd-Warshall algorithm
        for k in range(self.nodes):
            
            for i in range(self.nodes):
                
                for j in range(self.nodes):
                    
                    if self.distances[i][k] + self.distances[k][j] < self.distances[i][j]:
                        self.distances[i][j] = self.distances[i][k] + self.distances[k][j]

        # Check for negative cycles
        for k in range(self.nodes):
            
            if self.distances[k][k] < 0:  # Negative cycle found
                for i in range(self.nodes):
                    
                    for j in range(self.nodes):
                       
                        if self.distances[i][k] != float('inf') and self.distances[k][j] != float('inf'):
                            self.distances[i][j] = -float('inf')
#process_queries  method is designed to answer a list of short path queries between the pair of nodes.
#we create a empty list called results to store answers.it iterates over each query the dist retrives the precomputed shortest distance 
#from node u to node v using the distance matrix. the matrix was filled using the Floyd method.if the value is infinity it means no path exist from u to v,
#if the value is negative infinityso the cost can decrease indefinitely, if the distance is a finite number it converts it to a string 
#
    def process_queries(self, query_list: list[list[int]]) -> list[str]:
        results = []
        for u, v in query_list:
            
            dist = self.distances[u][v]
            
            if dist == float('inf'):
                results.append("Impossible")
            elif dist == -float('inf'):
                results.append("-Infinity")
            else:
                results.append(str(dist))
        return results



#parse_input function gets the number of nodes edges and query.it reads in all the edges of the graph. it splits the header line into 3 integer n number of nodes,m number of edges,
#q number of queries. we keep all the value to zero .next it reads m line and it skips an empty line and stores each edge as a list of 3 integer,,
#we initialize an empty list named query,each query will be a list of two integer ,,
#the query.append will split the string into parts, then it will convert each part from string to an integer then the mapped result turns into an actual list finally we append that to query 




def parse_input() -> tuple[int, int, list[list[int]], list[list[int]]]:
    while True:
        header = input().strip()
        if not header:
            continue
        n, m, q = map(int, header.split())
        if n == 0 and m == 0 and q == 0:
            return 0, 0, [], []  # Signal to stop
            
        edges = []
        for _ in range(m):
            
            while True:
                line = input().strip()
                
                if line:
                    edges.append(list(map(int, line.split())))
                    break
                    
        queries = []
        for _ in range(q):
            
            while True:
                line = input().strip()
                
                if line:
                    queries.append(list(map(int, line.split())))
                    break
                    
        return n, m, edges, queries
        
        
#TIME COMPLEXITY 
#parse_input() Reads m edges and q queries : O(m + q)
#add_edge():O(m)
#Floyd-Warshall Algorithm:O(n³) where n = number of nodes.
#overall time complexity is:O(n³)


def main():
    while True:
        
        node_count, edge_count, edges, queries = parse_input()
        
        if node_count == 0 and edge_count == 0 and not queries:
            break
            
        processor = GraphProcessor(node_count)
        
        for edge in edges:
            
            processor.add_edge(edge)
            
        processor.run_floyd_warshall()
        
        results = processor.process_queries(queries)
        
        print('\n'.join(results))
        print()  

if __name__ == "__main__":
    main()







































