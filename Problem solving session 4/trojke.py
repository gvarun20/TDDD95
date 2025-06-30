#def solve():
#
#    N = 4
#    grid = [
#        '...D',
#        '..C.',
#        '.B..',
#        'A...'
#    ]
#    
#    letters = []
#    for i in range(N):
#        for j in range(N):
#            if grid[i][j] != '.':
#                letters.append((i, j))
#    
#    count = 0
#   
#    num_letters = len(letters)
#    for i in range(num_letters):
#        for j in range(i + 1, num_letters):
#            for k in range(j + 1, num_letters):
#                (x1, y1), (x2, y2), (x3, y3) = letters[i], letters[j], letters[k]
#
#                area = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
#                if area == 0:
#                    count += 1
#    print(count)
#
#if __name__ == "__main__":
#    solve()




"""
The code first reads the size of the grid (N) and then reads in  the grid
itself line after line.after this it tries to go throught  the cell in the 
grid and gets the position of the letters.after this it checks if there lie on 
the same line that is the coliarity test .the code manually generates all possible 
triplets of letters using three nested loops. This approach guarantees that each 
triplet is unique and avoids redundant checks.for each triplet, the code checks if 
the three points lie on a straight line using the determinant method.The code 
increments a counter each time it finds a collinear triplet. The final count is
printed


"""
import sys

def solve():

    input = sys.stdin.read().split('\n')
    N = int(input[0].strip())
    grid = []
    
    
    for i in range(1, N + 1):
        grid.append(input[i].strip())
    
    
    letters = []
    
    
    for i in range(N):
        
        
        for j in range(N):
            
            
            if grid[i][j] != '.':
                letters.append((i, j))
    
    count = 0
    num_letters = len(letters)
    
    
    for i in range(num_letters):
        
        
        for j in range(i + 1, num_letters):
            
            
            for k in range(j + 1, num_letters):
                
                
                (x1, y1), (x2, y2), (x3, y3) = letters[i], letters[j], letters[k]

                area = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
                
                
                
                if area == 0:
                    count += 1
                    
    print(count)
    
if __name__ == "__main__":
    solve()    

