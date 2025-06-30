import heapq

# Read the number of nodes (N) and edges (M) in the graph.
# Read the start node, end node, delay time (dt), and the length of George's path (G).
# Read George's path as a list of nodes.



num_nodes, num_edges = map(int, input().split())
start_node, end_node, delay_time, georges_path_length = map(int, input().split())
georges_route = [*map(int, input().split())]







# Initialize the graph.
adjacency_list = [{} for _ in range(num_nodes + 1)]
for _ in range(num_edges):
    node_a, node_b, edge_weight = map(int, input().split())
    adjacency_list[node_a][node_b] = edge_weight    
    adjacency_list[node_b][node_a] = edge_weight




# Initialize the graph as an adjacency list where each node has a dictionary of neighbors and edge weights.
# Read each edge and populate the adjacency list. Since the graph is undirected, add edges in both directions.













# Create a dictionary to store blocked roads and their blocked times.
current_time = -delay_time
blocked_roads = {}
for i in range(georges_path_length - 1):
    node_u, node_v = georges_route[i:i + 2]
    blocked_roads[(node_u, node_v)] = current_time
    blocked_roads[(node_v, node_u)] = current_time
    current_time += adjacency_list[node_u][node_v]


# Create a dictionary to store blocked roads and the times they are blocked.
# George's path blocks certain roads at specific times. Initialize the time counter with a negative delay time.
# Iterate through George's path to determine when each road is blocked. Store the blocked roads and their blocked times in the dictionary.











shortest_distances = {}
min_heap = [(1, start_node)]










# Find the shortest path to the goal, considering wait times for blocked roads.
while min_heap:
    current_time, current_node = heapq.heappop(min_heap)















    if current_node in shortest_distances: continue

    shortest_distances[current_node] = current_time





# Record the shortest distance to the current node.
# Explore all neighbors of the current node.
# Check if the road from current_node to neighbor is blocked at the current time.
# If blocked, calculate the arrival time by waiting until the road is available.








    for neighbor, weight in adjacency_list[current_node].items():
# Find the shortest path to the goal, considering wait times for blocked roads.
# Pop the node with the smallest current time from the heap.
# If the node has already been processed, skip it.

#    if current_node in shortest_distances: continue
#
#    # Record the shortest distance to the current node.

        # If the road is blocked, wait until it is available again.
        if (current_node, neighbor) in blocked_roads and current_time >= blocked_roads[(current_node, neighbor)]:
            arrival_time = max(current_time, blocked_roads[(current_node, neighbor)] + weight) + weight
        else:
            arrival_time = current_time + weight



# Initialize a dictionary to store the shortest distances from the start node to each node.
# Use a min-heap (priority queue) to implement Dijkstra's algorithm. The heap stores tuples of (current_time, current_node).


# #   shortest_distances[current_node] = current_time
#
#    # Explore all neighbors of the current node.
 #   for neighbor, weight in adjacency_list[current_node].items():




        heapq.heappush(min_heap, (arrival_time, neighbor))







# If not blocked, simply add the edge weight to the current time.
# Push the new arrival time and neighbor into the heap.

# Print the shortest distance to the end node.

min_heap = [(1, start_node)]

# Find the shortest path to the goal, considering wait times for blocked roads.
##while min_heap:
#    # Pop the node with the smallest current time from the heap.
#    current_time, current_node = heapq.heappop(min_heap)
#
#    # If the node has already been processed, skip it.




print(shortest_distances[end_node])#try this might work 