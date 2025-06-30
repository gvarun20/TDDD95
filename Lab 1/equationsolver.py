#import sys
#import numpy as np

#def solve_system(A, b):
    #    A = np.array(A, dtype=np.float32)
    #b = np.array(b, dtype=np.float32)
    
    
    
    
    
    
    
  #  A = np.array(A, dtype=np.float64)
   # b = np.array(b, dtype=np.float64)
      #for i in range(n):
    #    # Partial pivoting
    #    max_row = max(range(i, n), key=lambda r: abs(augmented_matrix[r][i]))
    #    augmented_matrix[i], augmented_matrix[max_row] = augmented_matrix[max_row], augmented_matrix[i]
    # #   
  #  try:
  
  
  
  
  
  
  
   #     x = np.linalg.solve(A, b)
   #     return x.tolist()
        
        
            #if any(all(abs(augmented_matrix[i][j]) < 1e-9 for j in range(n)) for i in range(n)):
    #    return "multiple"  # Multiple solutions
  # # 
   # except np.linalg.LinAlgError:
   #     augmented = np.hstack((A, b.reshape(-1, 1)))
   #     rank_A = np.linalg.matrix_rank(A)
   #     rank_aug = np.linalg.matrix_rank(augmented)
   #     # Check for inconsistencies and free variables
    #for i in range(n):
    
    
    
    
   #     if rank_A < rank_aug:
   #         return "inconsistent"
   #     else:
   #         return "multiple"
#
#def main():
   # input_data = sys.stdin.read().strip().split('\n')
   # index = 0
       #   if all(abs(augmented_matrix[i][j]) < 1e-9 for j in range(n)) and abs(augmented_matrix[i][n]) > 1e-9:
     #       return None  # Inconsistent system
    
    
    
    
    
    
    #while index < len(input_data):
    #    n = int(input_data[index].strip())
    #    if n == 0:
#            break
   #     index += 1
#        
#        A = []
        #for _ in range(n):
#            A.append(list(map(float, input_data[index].split())))
#            index += 1
            #    if abs(augmented_matrix[i][i]) < 1e-9:
#    #        continue  # Skip if the pivot is zero
#        
#        # Attempt to solve the system using numpy's linear solver
       # b = list(map(float, input_data[index].split()))
#        index += 1
#         # Extract the solution
    #x = [augmented_matrix[i][n] for i in range(n)]
#    #return x
#
#        result = solve_system(A, b)
#        
#        if isinstance(result, str):
#            print(result)
#        else:
#            print(' '.join(f'{x:.3f}' for x in result))

#if __name__ == "__main__":
 #   main()

"""
By finding whether each set has a single answer, not one, or a finite number of answers, 
this method resolves systems of linear equations. Before reaching a system size of zero, 
a program reads a lot from input types. It finds Axe = b for each system by reading the 
constants vector b and the coefficient matrix A. By adding vector b to matrix A, an solve_system 
approach, which is the base of the basic algorithm, creates an extra matrix [A|b]. 
Then it uses unique row decrease methods to find the rank of both the added matrix and the initial
one A.

Under the fundamental principles about linear math, the equation is illogical (has no solution) if rank(A) < rank([A|b]);
here are a limitless number of options if rank(A) = rank([A|b]) < n; and there is just one solution if rank(A) = rank([A|b]) = n.
The algorithm turns the extra matrix to top triangles form by Gaussian elimination as its method with half turning for specific solutions, 
before it solves the system via back substitution. The rank estimate provides O(n³) time complexity and O(n²) space complexity by using 
traditions reduction of rows with no requiring the usage of numpy. This program gives answers with three digits of precision, "inconsistent"
for none, or "multiple" for infinite options. It uses integer limitation (1e-10) for floats stable.
The formula detects if there is just one solution, no possible response, or a limitless variety of 
answers when you have several equations with unknown variables (such as x, y, and z).
It simplifies the difficulty by arranging numbers in a grid and carrying out logical row operations.
Consider it similar to solving problems in which you get hints to the unknown values by each equation.
The solution action is flexible and stable for all kinds of mathematical factors since its program is able
to handle complex situations where variables might contradict with each other or when some of them are just 
distinct copies of the others.

Time complexity for the calculation for the rank, since it uses numpy, it could be O(n to the power 3).
Space complexity: the memory usage for the matrix might be O(n to the power 2).
"""




import sys

def gaussian_elimination(matrix):
    
    
    
    
    n = len(matrix)
    m = len(matrix[0])
    
    for i in range(n):
        max_row = i
        
        
        
        
        
        
        
        for k in range(i + 1, n):
            
            
            
            
            
            
            if abs(matrix[k][i]) > abs(matrix[max_row][i]):
                max_row = k
        
        matrix[i], matrix[max_row] = matrix[max_row], matrix[i]
        
        
        
        
        
        if abs(matrix[i][i]) < 1e-10:
            continue
            
        for k in range(i + 1, n):
            
            
            
            if abs(matrix[i][i]) > 1e-10:
                factor = matrix[k][i] / matrix[i][i]
                
                
                
                
                
                
                
                
                
                
                for j in range(i, m):
                    matrix[k][j] -= factor * matrix[i][j]
    
    return matrix
    
    
    

def back_substitution(matrix):
    
    
    
    
    
    n = len(matrix)
    x = [0.0] * n
    
    for i in range(n - 1, -1, -1):
        
        
        
        
        
        if abs(matrix[i][i]) < 1e-10:
            return None
            
        x[i] = matrix[i][n]
        
        
        
        
        
        
        
        for j in range(i + 1, n):
            x[i] -= matrix[i][j] * x[j]
            
            
            
            
            
            
            
            
            
            
        x[i] /= matrix[i][i]
    
    return x

def matrix_rank(matrix):
    
    
    
    
    
    
    
    temp = [row[:] for row in matrix]
    n = len(temp)
    m = len(temp[0]) if n > 0 else 0
    
    rank = 0
    
    
    
    
    
    for col in range(m):
        pivot_row = -1
        
        
        
        
        
        
        
        for row in range(rank, n):
            
            
            
            
            
            
            
            if abs(temp[row][col]) > 1e-10:
                pivot_row = row
                break
        
        if pivot_row == -1:
            continue
            
        if pivot_row != rank:
            temp[rank], temp[pivot_row] = temp[pivot_row], temp[rank]
        
        for row in range(n):
            
            
            
            
            
            
            if row != rank and abs(temp[row][col]) > 1e-10:
                factor = temp[row][col] / temp[rank][col]
                
                
                
                
                
                
                
                for j in range(m):
                    temp[row][j] -= factor * temp[rank][j]
        
        
        
        
        
        
        
        
        rank += 1
    
    return rank

def solve_system(A, b):
    
    
    
    n = len(A)
    
    augmented = []
    
    
    
    
    
    
    
    
    
    for i in range(n):
        row = A[i][:] + [b[i]]
        augmented.append(row)
        
        
        
        
    
    rank_A = matrix_rank(A)
    rank_aug = matrix_rank(augmented)
    
    
    
    
    
    
    if rank_A < rank_aug:
        return "inconsistent"
    
    
    
    
    
    if rank_A < n:
        return "multiple"
    
    try:
        
        
        
        
        reduced = gaussian_elimination(augmented)
        
        
        for i in range(n):
            
            
            
            
            if abs(reduced[i][i]) < 1e-10:
                return "multiple"
        
        solution = back_substitution(reduced)
        
        if solution is None:
            return "multiple"
        
        return solution
        
    except:
        return "multiple"

def main():
    
    
    
    
    input_data = sys.stdin.read().strip().split('\n')
    index = 0
    
    while index < len(input_data):
        
        
        
        
        
        n = int(input_data[index].strip())
        
        
        
        
        
        
        
        
        
        if n == 0:
            break
        index += 1
        
        A = []
        
        
        
        
        
        for _ in range(n):
            
            
            
            
            
            
            
            row = list(map(float, input_data[index].split()))
            A.append(row)
            index += 1
        
        b = list(map(float, input_data[index].split()))
        index += 1
        
        
        
        
        
        
        result = solve_system(A, b)
        
        
        
        
        
        
        if isinstance(result, str):
        
        
        
        
        
        
        
        
        
            print(result)
        else:
            print(' '.join(f'{x:.3f}' for x in result))
            
            
            
            
            
            

if __name__ == "__main__":
    main()

       
        
      

     
        
       
     
  

   

