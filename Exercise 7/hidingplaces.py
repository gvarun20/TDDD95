from collections import deque

"""

The knight start at an exact spot, including "a1". The quantity of steps used to reach every square is 
recorded by the algorithm using a grid. It began by using 0 steps to mark the start position. 
Once then, it checks all knight move that could have completed. The motions are L-shaped, with one 
square opposite to another and two equal squares in one direction. It confirms sure each new location 
is real  and wasn't reached yet. If so, that location is added onto a queue for further study and the 
total number of steps expected is specified. Until each region has been viewed, this process is done.


"""
from collections import deque

def calculate_knight_reach(initial_position):
    
    
    
    
    
    
    
    
    
    files = 'abcdefgh'
    start_file, start_rank = initial_position[0], int(initial_position[1])
    
    
    
    
    
    
    
    
    
    
    move_grid = [[-1 for _ in range(8)] for _ in range(8)]
    move_grid[start_rank-1][files.index(start_file)] = 0
    
    
    
    
    
    
    
    
    
    positions_to_process = deque()
    positions_to_process.append((files.index(start_file), start_rank-1, 0))
    
    
    
    
    
    
    
    
    
    move_offsets = [(-1,-2),(1,-2),(-1,2),(1,2),(-2,-1),(-2,1),(2,-1),(2,1)]
    
    
    
    
    while positions_to_process:
        
        
        
        
        
        current_file, current_rank, moves = positions_to_process.popleft()
        
        for df, dr in move_offsets:
            
            
            
            
            
            new_file, new_rank = current_file + df, current_rank + dr
            
            if 0 <= new_file < 8 and 0 <= new_rank < 8:
                
                
                
                
                if move_grid[new_rank][new_file] == -1:
                    
                    
                    
                    
                    
                    
                    
                    move_grid[new_rank][new_file] = moves + 1
                    positions_to_process.append((new_file, new_rank, moves + 1))
    
    
    
    
    
    
    
    
    max_moves = max(max(row) for row in move_grid)
    
    result_positions = []
    
    
    
    
    for rank in range(8):
        
        
        
        
        
        
        for file in range(8):
            
            
            
            
            
            
            
            
            if move_grid[rank][file] == max_moves:
                result_positions.append(f"{files[file]}{rank+1}")
    
    result_positions.sort(key=lambda x: (-int(x[1]), x[0]))
    
    
    
    
    
    
    return max_moves, result_positions

def process_input_data():
    
    
    
    
    
    
    
    
    
    
    
    import sys
    input_data = sys.stdin.read().splitlines()
    test_cases = input_data[1:]
    
    
    
    
    
    
    output_lines = []
    
    
    
    
    
    
    
    for position in test_cases:
        
        
        
        
        
        
        moves, squares = calculate_knight_reach(position)
        output_lines.append(f"{moves} {' '.join(squares)}")
    
    sys.stdout.write('\n'.join(output_lines))

if __name__ == "__main__":
    process_input_data()
