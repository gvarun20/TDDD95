#def cross(o, a, b):
#    # Cross product of vectors OA and OB
#    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
#
#def convex_hull(points):
#    points = sorted(set(points))  # Remove duplicates and sort
#
#    if len(points) <= 1:
#        return points
#
#    def build_half(pts):
#        half = []
#        for p in pts:
#            while len(half) >= 2 and cross(half[-2], half[-1], p) <= 0:
#                half.pop()
#            half.append(p)
#        return half
#
#    lower = build_half(points)
#    upper = build_half(reversed(points))
#
#    full = lower[:-1] + upper[:-1]
#
#    # Remove collinear adjacent edges from full hull
#    cleaned = []
#    for p in full:
#        while len(cleaned) >= 2 and cross(cleaned[-2], cleaned[-1], p) == 0:
#            cleaned.pop()
#        cleaned.append(p)
#
#    # Rotate to start from lexicographically smallest point (to match reference)
#    min_idx = min(range(len(cleaned)), key=lambda i: (cleaned[i][1], cleaned[i][0]))
#    cleaned = cleaned[min_idx:] + cleaned[:min_idx]
#
#    return cleaned
#
#def main():
#    input_data = [
#        "3",
#        "0 0",
#        "10 0",
#        "0 10",
#        "5",
#        "41 -6",
#        "-24 -74",
#        "-51 -6",
#        "73 17",
#        "-30 -34",
#        "2",
#        "50 50",
#        "50 50",
#        "0"
#    ]
#
#    idx = 0
#    while idx < len(input_data):
#        n = int(input_data[idx])
#        idx += 1
#        if n == 0:
#            break
#
#        points = []
#        for _ in range(n):
#            x, y = map(int, input_data[idx].split())
#            points.append((x, y))
#            idx += 1
#
#        hull = convex_hull(points)
#
#        print(len(hull))
#        for x, y in hull:
#            print(x, y)
#
#if __name__ == "__main__":
#    main()
#
"""
THE function computes the convex hull of a given set of 2D points using Andrew's monotone chain algorithm
The input points are first deduplicated using set() and then sorted alphabetical order.

If there are 0 or 1 points, the hull is the point itself or empty.2 points,
the hull is just the line segment connecting them.

build_half() function constructs half of the hull by iterating through points while maintaining a 
stack of candidate hull points.It uses the cross product to determine whether three consecutive points 
make a counter-clockwise turn .The lower hull is built by processing points left-to-right.The full hull
is formed by merging the lower and upper hulls.The algorithm checks for redundant collinear points.
The final hull is rotated to start from the alphabetical smallest point. 


Thr cross function calculates the positioning of the 3 points o,a,b in a 2d splace.
here it tries to convey that the points form a left turn or right turn or in a straight line.   
so it keeps the o as origin and then calculates OA,OB  if it is positive turns clockwise counter or negative 
it will be the opposite 


This algorithm efficiently computes the convex hull in O(n log n) 



REFERENCE:https://cp-algorithms.com/geometry/convex-hull.html
https://www.geeksforgeeks.org/convex-hull-algorithm/
"""

from math import sqrt
from typing import List








class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        
        
        
        
        
        
        

    def __sub__(self, other: "Point") -> "Point":
        return Point(self.x - other.x, self.y - other.y)
        
        
        
        
        
        
        
        

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Point) and self.x == other.x and self.y == other.y











    def __hash__(self) -> int:
        return hash((self.x, self.y))
        
        
        
        
        
        
        
        
        
        
        
        
        
        

    def cross(self, other: "Point") -> int:
        return self.x * other.y - self.y * other.x
        
        
        
        
        
        
        
        
        
        
        
        

    def __lt__(self, other: "Point") -> bool:
        return (self.y, self.x) < (other.y, other.x)

    def __repr__(self):
        return f"{self.x} {self.y}"

def cross(o: Point, a: Point, b: Point) -> int:
    
    return (a - o).cross(b - o)

def build_half(points: List[Point]) -> List[Point]:
    
    
    
    
    
    
    
    
    
    hull = []
    for pt in points:
        while len(hull) >= 2 and cross(hull[-2], hull[-1], pt) <= 0:
            
            
            
            
            
            
            
            
            hull.pop()
        hull.append(pt)
    return hull

def compute_convex_hull(points: List[Point]) -> List[Point]:
    
    
    
    
    
    
    
    
    
    
    points = sorted(set(points))
    if len(points) <= 1:
        return points







    lower = build_half(points)
    upper = build_half(reversed(points))

    full_hull = lower[:-1] + upper[:-1]

    result = []
    
    
    
    
    
    for pt in full_hull:
        while len(result) >= 2 and cross(result[-2], result[-1], pt) == 0:
            result.pop()
        result.append(pt)

    # Rotate to start from lexicographically smallest point (y, then x)
    
    
    
    
    
    
    
    
    
    min_index = min(range(len(result)), key=lambda i: (result[i].y, result[i].x))
    return result[min_index:] + result[:min_index]

def main():
    import sys
    
    
    
    
    
    
    
    
    lines = sys.stdin.read().strip().split("\n")
    index = 0
    output = []

    while index < len(lines):
        n = int(lines[index])
        index += 1

        if n == 0:
            
            
            
            
            
            break

        pts = []
        
        
        
        
        for _ in range(n):
            x, y = map(int, lines[index].split())
            
            
            
            
            
            
            
            
            pts.append(Point(x, y))
            index += 1

        hull = compute_convex_hull(pts)

        output.append(str(len(hull)))
        for pt in hull:
            
            
            
            
            
            output.append(f"{pt.x} {pt.y}")

    print("\n".join(output))

if __name__ == "__main__":
    main()














































































