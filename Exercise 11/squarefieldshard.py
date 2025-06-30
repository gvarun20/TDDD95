#def solve_case(points, k):
#    n = len(points)
#    
#    # Get all unique x and y coordinates
#    x_coords = sorted(set(p[0] for p in points))
#    y_coords = sorted(set(p[1] for p in points))
#    
#    # Binary search on the answer
#    left, right = 0, 64000
#    
#    while left < right:
#        mid = (left + right) // 2
#        if can_cover_with_size(points, k, mid):
#            right = mid
#        else:
#            left = mid + 1
#    
#    return left
#
#def can_cover_with_size(points, k, size):
#    n = len(points)
#    
#    # Get all possible square positions
#    # A square can be positioned such that its left edge is at any x-coordinate
#    # and its bottom edge is at any y-coordinate
#    x_coords = sorted(set(p[0] for p in points))
#    y_coords = sorted(set(p[1] for p in points))
#    
#    possible_squares = []
#    
#    # Try all possible positions for squares
#    for x in x_coords:
#        for y in y_coords:
#            # Square with bottom-left corner at (x, y)
#            square = (x, y, x + size, y + size)
#            possible_squares.append(square)
#    
#    # For each possible square, find which points it covers
#    coverage = []
#    for square in possible_squares:
#        x1, y1, x2, y2 = square
#        covered_points = 0
#        for i, (px, py) in enumerate(points):
#            if x1 <= px <= x2 and y1 <= py <= y2:
#                covered_points |= (1 << i)
#        coverage.append(covered_points)
#    
#    # Use DP with bitmask to check if we can cover all points with k squares
#    # dp[mask] = minimum number of squares needed to cover points in mask
#    dp = {}
#    dp[0] = 0
#    
#    for mask in range(1 << n):
#        if mask not in dp:
#            continue
#            
#        if dp[mask] >= k:
#            continue
#            
#        for covered in coverage:
#            new_mask = mask | covered
#            if new_mask not in dp or dp[new_mask] > dp[mask] + 1:
#                dp[new_mask] = dp[mask] + 1
#    
#    all_points_mask = (1 << n) - 1
#    return all_points_mask in dp and dp[all_points_mask] <= k
#
#def main():
#    # Hardcoded input exactly as provided
#    input_data = """2
#5 2
#1 1
#2 2
#3 3
#6 6
#7 8
#3 2
#3 3
#3 6
#6 9"""
#    
#    lines = input_data.strip().split('\n')
#    line_idx = 0
#    
#    T = int(lines[line_idx])
#    line_idx += 1
#    
#    for case_num in range(1, T + 1):
#        n, k = map(int, lines[line_idx].split())
#        line_idx += 1
#        
#        points = []
#        for _ in range(n):
#            x, y = map(int, lines[line_idx].split())
#            points.append((x, y))
#            line_idx += 1
#        
#        result = solve_case(points, k)
#        print(f"Case #{case_num}: {result}")
#
#if __name__ == "__main__":
#    main()
#    
    
    
"""

This technique reliably gets the lowest tile size by using a binary search methods.
The code first collects and organises every point's unique x and y data. 
A binary search for from left = 0 and right = 64000 then gets began. 
A likely grid size is denoted by the central element (mid), as is set in every loop. 
If this is a minimum a single area of size centre that allows for k as many points,
it is determined with the can_cover_with_size function.
To try find a smaller ability size, the search goes on in the bottom half (right = mid) if so a square exists
. The look for proceeds onto the top part when it is not a square likes that. 
Until the least eligible cube size is identified, the method is done.

"""
    
def solve_case(points, k):
    
    
    
    n = len(points)
    
    x_coords = sorted(set(p[0] for p in points))
    y_coords = sorted(set(p[1] for p in points))
    
    left, right = 0, 64000
    
    while left < right:
        
        
        
        
        mid = (left + right) // 2
        
        
        
        if can_cover_with_size(points, k, mid):
            right = mid
        else:
            left = mid + 1
    
    
    
    
    return left
    
    
    
    
    
    
    
    
    
"""
It next sets the leftmost ends of all
square as each different value from points to generate every easy square of the size required.
The corners of all of them were kept. It it detects how many points are occupied by every corner.  It uses bitmasking—each point can 
 be represented by an element in an a binary number—instead of count points direct.  A point's tied bit c
 an be set to 1 if it lies in the centre of the square. At last, it uses dynamic code to decide if combining more than k squares will let us to cover less
 than k points.  The dp dictionaries takes track of the least amount of grids required for some point pairs.  
 The method yields True if ≤ k squares may cover each point; if not and it gives False.


"""


def can_cover_with_size(points, k, size):
    
    
    
    
    n = len(points)
    
    x_coords = sorted(set(p[0] for p in points))
    y_coords = sorted(set(p[1] for p in points))
    
    possible_squares = []
    
    for x in x_coords:
        
        
        
        for y in y_coords:
            
            
            
            square = (x, y, x + size, y + size)
            possible_squares.append(square)
    
    coverage = []
    
    
    
    for square in possible_squares:
        
        
        
        x1, y1, x2, y2 = square
        covered_points = 0
        
        
        
        for i, (px, py) in enumerate(points):
            
            
            
            if x1 <= px <= x2 and y1 <= py <= y2:
                covered_points |= (1 << i)
                
                
                
                
        coverage.append(covered_points)
    
    dp = {}
    dp[0] = 0
    
    for mask in range(1 << n):
        
        
        
        
        if mask not in dp:
            continue
        
        
            
        if dp[mask] >= k:
            continue
        
        
        
            
        for covered in coverage:
            
            
            
            new_mask = mask | covered
            
            
            
            if new_mask not in dp or dp[new_mask] > dp[mask] + 1:
                dp[new_mask] = dp[mask] + 1
    
    
    
    
    all_points_mask = (1 << n) - 1
    return all_points_mask in dp and dp[all_points_mask] <= k


"""




"""
def main():
    T = int(input())
    
    for case_num in range(1, T + 1):
        n, k = map(int, input().split())
        points = []
        
        for _ in range(n):
            x, y = map(int, input().split())
            points.append((x, y))
        
        result = solve_case(points, k)
        print(f"Case #{case_num}: {result}")

    
    

if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
    