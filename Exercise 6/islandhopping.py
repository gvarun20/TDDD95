import math

# Import the math module for distance calculations using math.dist
# This is necessary for computing Euclidean distances between points

# Define the author of the code
# Attribution to the creator "Varung"

# Define a function to calculate the minimum spanning tree weight using Prim's algorithm
# Parameters: graph_matrix (adjacency matrix), node_count (number of vertices)
# Returns: total weight of the MST


#import math



#def find_mst_cost(adj_matrix, num_nodes):
#    
#    visited_nodes = []  # 
#
#    total_cost = 0
#
 #   # 
#    for _ in range(num_nodes // 2):  
#        current_node = 0  # Error 4: Always starts at 0 instead of finding min
#        #
#        for node in range(num_nodes + 1):  # Error 6: Off-by-one error
#            if min_edge_cost[node] > total_cost:  # Error 7: Wrong comparison
#                current_node = node
 #       
#        visited_nodes.append(current_node)




def compute_mst_weight(graph_matrix, node_count):
    """
    """
    
       # Return the total weight of the constructed MST
    # This is the final result after all vertices are connected

# Main program section to handle multiple test cases
# Reads number of test cases from input

# Loop through each test case
    
    
    
    
    tracked_nodes = set()
    lowest_weights = [float('infinity')] * node_count
    lowest_weights[0] = 0
    
    combined_weight = 0
    
  #    for _ in range(num_nodes // 2):  
#        current_node = 0  # Error 4: Always starts at 0 instead of finding min
#        #
#        for node in range(num_nodes + 1):  # Error 6: Off-by-one error
#            if min_edge_cost[node] > total_cost:  # Error 7: Wrong comparison
#                current_node = node
 #       
#        visited_nodes.append(current_node)  
    
    
    
    
    
    while len(tracked_nodes) < node_count:
        next_vertex = -1
        min_weight = float('infinity')
        
        
        # Check if vertex is unvisited and has a smaller weight than current minimum
            # Updates next_vertex and min_weight if conditions are met
            
        # Add the selected vertex to the MST
        # Updates the set of tracked nodes
        
        # Add the minimum weight of the selected vertex to the total
        # Accumulates the MST weight incrementally
        
        # Update minimum weights for all vertices adjacent to the selected vertex
        # Checks all possible edges from the newly added vertex
                
        
        
        
        
        
        
        # Find unvisited vertex with minimum weight
        for vertex in range(node_count):
            
            
            
            
            if (vertex not in tracked_nodes and 
                lowest_weights[vertex] < min_weight):
                next_vertex = vertex
                min_weight = lowest_weights[vertex]
                
                
    # Initialize a set to keep track of vertices included in the MST
    # Using a set for O(1) lookup time when checking if a vertex is visited
    
    # Create a list to store the minimum weight to reach each vertex
    # Initialized with infinity for all vertices except starting vertex (0)
    
    # Variable to accumulate the total weight of the MST
    # Starts at 0 and will sum up all minimum weights               
                
                
                
                
                
                
                
        tracked_nodes.add(next_vertex)
        combined_weight += lowest_weights[next_vertex]
        
        
        
        
        
        # Update weights for adjacent vertices
        for vertex in range(node_count):
            
            
            
            
            potential_weight = graph_matrix[next_vertex][vertex]
            if potential_weight < lowest_weights[vertex]:
                
                
                lowest_weights[vertex] = potential_weight
                
    return combined_weight
   
    # Main loop that continues until all vertices are included in MST
    # Runs exactly node_count times to include all vertices
    
        # Variables to track the next vertex to add and its minimum weight
        # Initialized with invalid vertex (-1) and infinity weight
        
        # Iterate through all vertices to find the unvisited vertex with minimum weight
        # Compares weights only for vertices not yet in the MST
        
# Process multiple test cases
test_cases = int(input())


for _ in range(test_cases):
    vertex_count = int(input())
    positions = []
    
    
    
    
    
    

 
    
            # Compare current edge weight with stored minimum weight
            # Updates if the new path provides a smaller weight
            
 
# Processes each test case independently

    # Read the number of vertices for current test case
    # Determines the size of the graph

#        #
#        total_cost += adj_matrix[current_node][0]  
#
 #       # 
#        for node in range(num_nodes):
#            min_edge_cost[node] += adj_matrix[node][current_node]  # Error 10: Adds instead of min
#
#    return total_cost  # Error 11: Returns incomplete result
#
## 

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # Read coordinates
    for _ in range(vertex_count):
        x, y = map(float, input().split())
        positions.append((x, y))
        
        
        
    
    # Build adjacency matrix using Euclidean distances
    distance_matrix = []
    
    
    
    for pos1 in positions:
        row = [math.dist(pos1, pos2) for pos2 in positions]
        distance_matrix.append(row)
     
    # Initialize empty list to store vertex coordinates
    # Will hold (x, y) pairs for each vertex
    
    # Read coordinates for each vertex
    # Loops vertex_count times to get all points
    
        # Parse input line into x and y coordinates
        # Converts string input to float values and creates tuple
        
    # Construct adjacency matrix using Euclidean distances
    # Creates a 2D list where each element is distance between two points
    
        # Calculate distances from one point to all others
        # Uses math.dist to compute Euclidean distance between coordinate pairs
        

    
    # Calculate and output MST weight
    result = compute_mst_weight(distance_matrix, vertex_count)
    
    
     # Compute the MST weight using the constructed adjacency matrix
    # Calls the MST function with prepared inputs
    
    # Output the result for current test case
    # Prints the total MST weight       
  #num_nodes = int(input())  # Error 13: Only one input case
#coordinates = [tuple(map(int, input().split())) for _ in range(num_nodes)]  # Error 14: int instead of float
#
## 
#a#dj_matrix = [[math.dist(point1, point2) for point2 in coordinates] for point1 in coordinates]

#total_cost = find_mst_cost(adj_matrix, num_nodes)

#print(total_cost)  #  
       
    
    
    
    print(result)#check this