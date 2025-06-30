#import numpy
#import sys

# Find the starting position 'S' in the maze

# If no starting position is found, return 0 cost
#
#def minimal_search_cost(maze, x, y):
#    # Find the starting position
#    start = None
#    
#    # Define possible movement directions: north, south, east, west
#
#    # Initialize BFS queue with the starting position and initial distance 0
# #   for i in range(y):
#        for j in range(x):
# #           if maze[i][j] == 'S':
#                start = (i, j)
#                break
#        if start:
 #           break
        
    # Set to keep track of visited positions to avoid reprocessing

    # Variable to accumulate the total cost of the search
    
#    if not start:
#        return 0
#    
# #   # Directions for moving north, south, east, west
#    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
#    
#    # Initialize BFS
#    queue = deque()
#    queue.append((start[0], start[1], 0))  # (row, col, distance)
#    visited = set()
#    visited.add((start[0], start[1]))
    
#    total_cost = 0

    # Perform BFS

    # If an alien 'A' is found, add the distance to the total cost
    # and reset the distance for new groups

    # Explore all four possible directions

    # Check if the new position is within bounds, not a wall, and not visited
    # Add the new position to the queue with incremented distance
#    while queue:
#        row, col, dist = queue.popleft()
#        
#        # If we find an alien, split the group
#        if maze[row][col] == 'A':
#            total_cost += dist
# #           # Reset distance for new groups
#            dist = 0
        
#        # Explore neighbors BY THE MAZE FUNCTION 
#        for dr, dc in directions:
#            nr, nc = row + dr, col + dc
#            if 0 <= nr < y and 0 <= nc < x and maze[nr][nc] != '#' and (nr, nc) not in visited:
#                visited.add((nr, nc))
#                queue.append((nr, nc, dist + 1))
#    
#    return total_cost
#
## Return the total cost after exploring the maze
#
# Main function to handle input and output

# Read the number of test cases

# Process each test case

# Read the dimensions of the maze

# Read input
#def main():

# Read the maze grid

# Compute and print the minimal search cost for the current maze

# Entry point of the script
#if __name__ == "__main__":
    
    
    
    
    
# 
def inrange(x, y, n, m):
    return 0 <= x < n and 0 <= y < m



def spot(p, m):
    return p[0] * m + p[1]






def find(d, a):
    if d[a] == -1:
        return a
    d[a] = find(d, d[a])
    return d[a]













def join(d, a, b):
    a = find(d, a)
    b = find(d, b)
    if a == b:
        return
    d[a] = b









def bfs(v, edges, p, n, m):
    dist = [[float('inf')] * m for _ in range(n)]
    q = []  # Use a list as a queue
    q.append(p)
    dist[p[0]][p[1]] = 0










    movement = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while q:
        currx, curry = q.pop(0)  # Simulate deque's popleft()

        if v[currx][curry] == 'S' or v[currx][curry] == 'A':
            e = {'p1': p, 'p2': (currx, curry), 'weight': dist[currx][curry]}
            edges.append(e)












        for dx, dy in movement:
            nextx, nexty = currx + dx, curry + dy
            if inrange(nextx, nexty, n, m):
                if v[nextx][nexty] == '#':
                    continue
                if dist[nextx][nexty] > dist[currx][curry] + 1:
                    dist[nextx][nexty] = dist[currx][curry] + 1
                    q.append((nextx, nexty))

def solve():
 
 
 
 
 
 
 
 
 
    # Read input using input() instead of sys.stdin
    m, n = map(int, input().split())
    v = [input().strip() for _ in range(n)]
    v = [row.ljust(m) for row in v]














    points = []
    for i in range(n):
        for j in range(m):
            if v[i][j] == 'A' or v[i][j] == 'S':
                points.append((i, j))

    edges = []
    for p in points:
        bfs(v, edges, p, n, m)











    edges.sort(key=lambda x: x['weight'])
    total = 0
    d = [-1] * (n * m)
    for e in edges:
        if find(d, spot(e['p1'], m)) != find(d, spot(e['p2'], m)):
            join(d, spot(e['p1'], m), spot(e['p2'], m))
            total += e['weight']

    return total















def main():
    # Read the number of test cases using input()
    cases = int(input())
    for _ in range(cases):
        # Read maze dimensions and maze itself
        m, n = map(int, input().split())
        v = [input().strip() for _ in range(n)]
        v = [row.ljust(m) for row in v]


















        points = []
        for i in range(n):
            for j in range(m):
                if v[i][j] == 'A' or v[i][j] == 'S':
                    points.append((i, j))

        edges = []
        for p in points:
            bfs(v, edges, p, n, m)

        edges.sort(key=lambda x: x['weight'])
        total = 0
        d = [-1] * (n * m)
        for e in edges:
            if find(d, spot(e['p1'], m)) != find(d, spot(e['p2'], m)):
                join(d, spot(e['p1'], m), spot(e['p2'], m))
                total += e['weight']
        print(total)

if __name__ == "__main__":
    main()    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#import numpy
#import sys
#from collections import deque
#import sys

# Find the starting position 'S' in the maze

# If no starting position is found, return 0 cost

#def minimal_search_cost(maze, x, y):
#    # Find the starting position
 #   start = None
    
    
    
    
    
    
    
    
    
#    # Define possible movement directions: north, south, east, west
#
#    # Initialize BFS queue with the starting position and initial distance 0
#    for i in range(y):
#        for j in range(x):
#            if maze[i][j] == 'S':
#                start = (i, j)
#                break
#        if start:
#            break
#        
#    # Set to keep track of visited positions to avoid reprocessing





#    # Variable to accumulate the total cost of the search
#    
#    if not start:
#        return 0
#    
#    # Directions for moving north, south, east, west
#    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
#    
    
#    
    # Initialize BFS
#    queue = deque()
#    queue.append((start[0], start[1], 0))  # (row, col, distance)
#    visited = set()
#    visited.add((start[0], start[1]))
#    
#    total_cost = 0

#    # Perform BFS
#
    # If an alien 'A' is found, add the distance to the total cost
#    # and reset the distance for new groups


#


#    # Explore all four possible directions
#
#    # Check if the new position is within bounds, not a wall, and not visited
#    # Add the new position to the queue with incremented distance
#    while queue:
#        row, col, dist = queue.popleft()
#        
#        
#        
        
        
        
        
#        
#        # If we find an alien, split the group
#        if maze[row][col] == 'A':
#            total_cost += dist
#            # Reset distance for new groups
 #           dist = 0
#        
        
        
        
        
        
#        
#        
#  #      # Explore neighbors BY THE MAZE FUNCTION 
#        for dr, dc in directions:
#            nr, nc = row + dr, col + dc
#            if 0 <= nr < y and 0 <= nc < x and maze[nr][nc] != '#' and (nr, nc) not in visited:
#                visited.add((nr, nc))
#                queue.append((nr, nc, dist + 1))
#    
#    return total_cost
#
# Return the total cost after exploring the maze

# Main function to handle input and output

# Read the number of test cases

# Process each test case

# Read the dimensions of the maze










## Read input
#def main():
#    input = sys.stdin.read
#    data = input().split()
#    idx = 0
#    N = int(data[idx])
 #   idx += 1
# #   for _ in range(N):  # I THINK THIS PART IS CORRECT 
#        x = int(data[idx])
#        y = int(data[idx+1])
#        idx += 2
#        maze = []
#        for _ in range(y):
#            maze.append(data[idx])
#            idx += 1
#        print(minimal_search_cost(maze, x, y))

# Read the maze grid

# Compute and print the minimal search cost for the current maze




## Entry point of the script
#if __name__ == "__main__":
#    main()
    