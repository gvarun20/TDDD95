from collections import defaultdict
from math import gcd



"""
THIS FUNCTION TRIES TO calculates the highest number of point that lie on the same line.
the 2dpoint given ..it tries to handle if there are 0,1 points then it will again return n.
here we calculate the slope for each point i , the computing will be done between i and every other point j.
the slope is reduced to fraction using the gcd .to avoid any duuplicate we try to normalize it .
so if the dx is negative ,dx and dy are altered to maintain the consistant value
and then if only dx is zero ,, we make the dy as positive.


Given a list of 2D points (x, y), the function must compute the maximum subset of points that are colinear
If there are 0 or 1 points, the solution is trivially n because:
Zero points can't draw a line.
A single point is technically colinear with itself.

The basic idea is to iterate over each point and use it as the anchor to compare slopes with all other points.
The outer loop (for i in range(n)) selects each point i to be the anchor to compute slopes.
For an anchor, the function initially sets up a defaultdict called slopes to hold how many other points have the same slope as i.
The inner loop (for j in range(n)) computes the direction vector (dx, dy) from the anchor i to each other point j

the function normalizes the direction vector:
If dx < 0, then both dx and dy are negated to make it consistent.
If dx == 0 (which happens for a vertical line), dy is given its absolute value to ensure both upward and downward lines are equal

Time Complexity: O(n²) as each one of the n anchors is compared to n-1 other points





"""

def max_colinear(points):
    
    
    n = len(points)
    
    
    
    if n <= 1:
        return n
        
        
        
    max_points = 1
    
    
    for i in range(n):
        slopes = defaultdict(int)
        
        
        for j in range(n):
            
            
            
            if i == j:
                continue
            
            
            dx = points[j][0] - points[i][0]
            dy = points[j][1] - points[i][1]
            g = gcd(dx, dy)
            
            
            
            if g != 0:
                dx //= g
                dy //= g
            if dx < 0:
                dx, dy = -dx, -dy
            elif dx == 0:
                dy = abs(dy)
                
                
                
                
            slopes[(dx, dy)] += 1
            
            
            
        max_points = max(max_points, max(slopes.values()) + 1)
        
        
    return max_points

def main():
    
    
    while True:
        
        
        n = int(input())
        
        
        if n == 0:
            break
        
        points = []
        
        
        for _ in range(n):
            x, y = map(int, input().split())
            points.append((x, y))
            
            
        print(max_colinear(points))

if __name__ == "__main__":
    main()
