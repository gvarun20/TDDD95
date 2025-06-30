"""
HERE WE calculate the direction and the area of a polygon given the vertices ,, here we use the shoelace formula 
the loop works through the continous points ,then it computes the cross-product for each term
and then it summs the terms and then it gives the value whose sigh tells the direction, 
positive means clockwise-counter, and negative means the clockwise.
the formula works for any simple polygon .the modula tells that the last edge must connect back to the start or the first point


the time complexity might be O(n) for the n vertices




"""


def compute_area_and_direction(points):
    
    
    n = len(points)
    area = 0
    
    
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]
        area += x1 * y2 - x2 * y1
        
        
    direction = "CCW" if area > 0 else "CW"
    
    
    return direction, abs(area) / 2.0

def main():
    results = []
    
    
    while True:
        
        
        line = input().strip()
        
        
        if line == '0':
            break
        
        
        n = int(line)
        points = []
        
        
        for _ in range(n):
            x, y = map(int, input().strip().split())
            points.append((x, y))
            
            
        direction, area = compute_area_and_direction(points)
        results.append(f"{direction} {area:.1f}")
        
        
        
    for res in results:
        print(res)




if __name__ == "__main__":
    main()