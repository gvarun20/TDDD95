import math
#
#def dot(a, b):
#    return a[0]*b[0] + a[1]*b[1]
#
#def norm(v):
#    return math.sqrt(dot(v, v))
#
#def distance(p1, p2):
#    return math.hypot(p1[0]-p2[0], p1[1]-p2[1])
#
#def point_to_segment_distance(p, a, b):
#    ab = (b[0] - a[0], b[1] - a[1])
#    ap = (p[0] - a[0], p[1] - a[1])
#    ab_ap = dot(ap, ab)
#    ab_ab = dot(ab, ab)
#    t = ab_ap / ab_ab if ab_ab != 0 else -1
#    if t < 0:
#        closest = a
#    elif t > 1:
#        closest = b
#    else:
#        closest = (a[0] + ab[0]*t, a[1] + ab[1]*t)
#    return distance(p, closest)
#
#def ccw(a, b, c):
#    return (c[1]-a[1]) * (b[0]-a[0]) > (b[1]-a[1]) * (c[0]-a[0])
#
#def segments_intersect(p1, p2, q1, q2):
#    return (ccw(p1, q1, q2) != ccw(p2, q1, q2)) and (ccw(p1, p2, q1) != ccw(p1, p2, q2))
#
#def segment_to_segment_distance(p1, p2, q1, q2):
#    if segments_intersect(p1, p2, q1, q2):
#        return 0.0
#    return min(
#        point_to_segment_distance(p1, q1, q2),
#        point_to_segment_distance(p2, q1, q2),
#        point_to_segment_distance(q1, p1, p2),
#        point_to_segment_distance(q2, p1, p2)
#    )
#
## Input test cases
#test_cases = [
#    [-10, 0, 10, 0, 0, -10, 0, 10],
#    [-10, 0, 10, 0, -5, 0, 5, 0],
#    [1, 1, 1, 1, 1, 1, 2, 1],
#    [1, 1, 1, 1, 2, 1, 2, 1],
#    [1871, 5789, 216, -517, 189, -1518, 3851, 1895],
#]
#
## Process and print results
#for coords in test_cases:
#    x1, y1, x2, y2, x3, y3, x4, y4 = coords
#    p1, p2 = (x1, y1), (x2, y2)
#    q1, q2 = (x3, y3), (x4, y4)
#    d = segment_to_segment_distance(p1, p2, q1, q2)
#    print(f"{d:.2f}")
#
"""
the dot function calculates the dot product of the two vectors so for example we have a(a1,a2) and b(b1,b2)
it multiplies a1*b1 and the same with other and then adds the products.

the norm function tries to calculates the length of the vector.so we take a vector use the dot product 
of the vector with itself.then it takes the square root of that sum.

the distance function is the same equation which we use it for the pythagorous theorm to calculate
the diagonal distance.

THE point_to_segment_distance  calculates the shortest distance between a point (p) and a line segment.
so now we create 2 vectors ab,so it goes from a to b ,,then we calculate the dot product ,,
next we find the projection parameter t , so the formula might be ab_ap/ab_ab,,if the t value is greatest than 
1 then it is closest to b or else it will be a.


point_to_segment_distance(p, a, b) finds the shortest path between a line segment with ends 
a and b and a point p. It analyses the relative location of point p with the rest of this segment after 
first displaying it as a vector from a to b.The portion of the vector (ab) and the vector from the segment's 
beginning point to p (ap) are the first two major vectors that are determined in the computation. 
The function finds how far down the segment the nearest point would be if the line were continually extended by
expanding ap onto ab using the dot product. This projection is normalised to a parameter t, where values between
0 and 1 describe points a and b, as with t=0 and t=1. 

ccw function determines the orientation of three point.It takes three points as input: 
a, b, and c .It calculates the cross product of vectors .If the cross product value is greater than 0
its counter-clockwise, less than 0 then clockwise  if 0 then its colinear.


segments_intersect Function checks if two line segments intersect each other.


segment_to_segment_distance Function it calculates the shortest distance between two line segments.


the total time complexity might be =O(n)


Reference:https://homepage.univie.ac.at/franz.vesely/notes/hard_sticks/hst/hst.html
https://www.geeksforgeeks.org/shortest-distance-between-two-lines-in-3d-space-class-12-maths/

https://stackoverflow.com/questions/2824478/shortest-distance-between-two-line-segments



"""


from math import sqrt, hypot, acos
from typing import List






class Point:
    
    
    
    
    
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y




    def __sub__(self, other: 'Point') -> 'Point':
        return Point(self.x - other.x, self.y - other.y)
        
        
        
        
        

    def __add__(self, other: 'Point') -> 'Point':
        return Point(self.x + other.x, self.y + other.y)
        
        
        

    def __mul__(self, scalar: float) -> 'Point':
        return Point(self.x * scalar, self.y * scalar)
        
        
        
        

    def __eq__(self, other: 'Point') -> bool:
        return self.x == other.x and self.y == other.y
        
        
        
        

    def dot(self, other: 'Point') -> float:
        return self.x * other.x + self.y * other.y
        
        
        
        

    def cross(self, other: 'Point') -> float:
        return self.x * other.y - self.y * other.x
        
        
        
        

    def distance(self, other: 'Point') -> float:
        return hypot(self.x - other.x, self.y - other.y)
        
        
        
        

    def norm(self) -> float:
        return sqrt(self.x**2 + self.y**2)
        
        
        
        

    def __repr__(self):
        return f"({self.x}, {self.y})"
        
        
        


def clamp(value: float, min_val: float, max_val: float) -> float:
    return max(min_val, min(value, max_val))


def ccw(a: Point, b: Point, c: Point) -> bool:
    return (c - a).cross(b - a) > 0




def segments_intersect(p1: Point, p2: Point, q1: Point, q2: Point) -> bool:
    return (ccw(p1, q1, q2) != ccw(p2, q1, q2)) and (ccw(p1, p2, q1) != ccw(p1, p2, q2))


def point_to_segment_distance(p: Point, a: Point, b: Point) -> float:
    
    
    ab = b - a
    ap = p - a

    ab_dot_ab = ab.dot(ab)
    if ab_dot_ab == 0:
        return p.distance(a)
        
        
        

    t = clamp(ap.dot(ab) / ab_dot_ab, 0, 1)
    closest = a + ab * t
    
    
    
    
    return p.distance(closest)


def segment_to_segment_distance(p1: Point, p2: Point, q1: Point, q2: Point) -> float:
    
    
    
    
    if segments_intersect(p1, p2, q1, q2):
        return 0.0
        
        
        

    return min(
        point_to_segment_distance(p1, q1, q2),
        point_to_segment_distance(p2, q1, q2),
        point_to_segment_distance(q1, p1, p2),
        point_to_segment_distance(q2, p1, p2)
    )


if __name__ == "__main__":
    n = int(input())

    for _ in range(n):
        
        
        
        x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
        p1, p2 = Point(x1, y1), Point(x2, y2)
        q1, q2 = Point(x3, y3), Point(x4, y4)

        d = segment_to_segment_distance(p1, p2, q1, q2)
        print(f"{d:.2f}")













