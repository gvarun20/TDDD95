import math
from typing import Tuple



class Vertex:
    
    
    
    def __init__(self, x_coord: float, y_coord: float):
        
        
        
        
        self.x = x_coord
        self.y = y_coord
    
    def __add__(self, other: 'Vertex') -> 'Vertex':
        
        
        
        if not isinstance(other, Vertex):
            
            
            
            raise TypeError(f"Cannot add Vertex with {type(other).__name__}")
        
        
        return Vertex(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other: 'Vertex') -> 'Vertex':
        
        
        
        if not isinstance(other, Vertex):
            
            
            
            raise TypeError(f"Cannot subtract {type(other).__name__} from Vertex")
        
        
        
        return Vertex(self.x - other.x, self.y - other.y)
    
    def scale(self, factor: float) -> 'Vertex':
        
        
        
        return Vertex(self.x * factor, self.y * factor)
    
    
    
    def magnitude(self) -> float:
        
        
        
        return math.sqrt(self.x**2 + self.y**2)
    
    
    
    
    def dot_product(self, other: 'Vertex') -> float:
        
        
        
        return self.x * other.x + self.y * other.y
    
    
    
    
    
    def cross_product(self, other: 'Vertex') -> float:
        
        
        
        return self.x * other.y - self.y * other.x
    
    
    
    
    def __str__(self) -> str:
        
        
        
        return f"({self.x:.1f}, {self.y:.1f})"






"""
uses three vertices as input and uses the triangle's 
sides and angles to categorise it.  By calculating the initial area using a cross product,
it determines if the points are parallel; if the size is essentially 0. it returns (0, 0),
showing that there is not an right shape.  To stop floats errors from square roots, a function
finds the scaled sizes of each on each of the sides if the points make an actual triangle. 
The features of the triangle are then found by selecting the side values.

 The function uses arithmetic to determine if any two sides are roughly equal in order to 
 classify edges.  isclose, give a scaling triangle a yield of 2 or a triangle that is isosceles a 
 back of 1.In order to sort angles, the average of the two lowest squared sides goes up to the most.  
 The angle of the triangle is acute (1), obtuse (2), or right-angled (returning 3) if the three are equal. 
 This is the case if the sum is less.  The triangle’s geometrical grouping is briefly given as the final 
 output, a tuple

"""


def analyze_triangle(v1: Vertex, v2: Vertex, v3: Vertex) -> Tuple[int, int]:

    area = (v2.x - v1.x) * (v3.y - v1.y) - (v2.y - v1.y) * (v3.x - v1.x)
    
    
    
    if abs(area) < 1e-9:
        return 0, 0
    




    def squared_distance(p1: Vertex, p2: Vertex) -> float:
        
        
        dx = p1.x - p2.x
        dy = p1.y - p2.y
        
        
        
        return dx*dx + dy*dy
    
    a_sq = squared_distance(v2, v3)
    b_sq = squared_distance(v1, v3)
    c_sq = squared_distance(v1, v2)
    
    sides = sorted([a_sq, b_sq, c_sq])
    

    edge_class = 2 
    
    
    
    if math.isclose(sides[0], sides[1]) or math.isclose(sides[1], sides[2]):
        
        edge_class = 1  
    

    angle_class = 1 
    sum_smallest = sides[0] + sides[1]
    largest = sides[2]
    
    if math.isclose(sum_smallest, largest):
        
        
        angle_class = 3  
        
        
    elif sum_smallest < largest:
        
        
        
        angle_class = 2  
    
    return edge_class, angle_class





def main():
    import sys
    
    
    
    
    input_lines = sys.stdin.read().splitlines()
    results = []
    
    for i in range(1, len(input_lines)):
        
        
        
        
        
        
        
        coords = list(map(float, input_lines[i].split()))
        
        
        
        if len(coords) != 6:
            continue
            
            
            
        pt1 = Vertex(coords[0], coords[1])
        pt2 = Vertex(coords[2], coords[3])
        pt3 = Vertex(coords[4], coords[5])
        
        edge, angle = analyze_triangle(pt1, pt2, pt3)
        
        edge_names = ["invalid", "isosceles", "scalene"]
        angle_names = ["", "acute", "obtuse", "right"]
        
        if edge == 0:
            
            
            
            results.append(f"Case #{i}: not a triangle")
            
            
            
        else:
            
            
            
            results.append(f"Case #{i}: {edge_names[edge]} {angle_names[angle]} triangle")
    
    print('\n'.join(results))





if __name__ == "__main__":
    main()







