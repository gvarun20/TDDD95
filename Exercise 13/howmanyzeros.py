import math


"""
The two phases provide the code's work. It first gets the total number of all a zero up to 
their total value. The total a zero up to the first number zero are then counted. For it calculate 
the sum of zeros within this range, a second outcome is finally reduced from the first.The program
verifies each one's place with the aim to count a zero up to a number. It breaks the value into higher 
current, and less digits to find which ones occur in all of them. It adds the lower digits by one if the
current value is zero. If or not, it raises the top values by a value of ten for the spot. Edge conditions,
like when a number is 0 or low, are taken care of by the code.

"""
from math import log10, floor

def count_zero_digits(start: int, end: int) -> int:
    
    
    
    
    
    
    
    
    total = 0
    if start == 0:
        total += 1
    
    
    
    
    for pos in range(1, floor(log10(end)) + 2):
        
        
        
        
        
        
        digit_at_pos = (end % 10**pos) // 10**(pos - 1)
        
        
        
        
        if pos == 1 or digit_at_pos != 0:
            total += 10**(pos - 1) * floor(end / 10**pos)
        else:
            total += 10**(pos - 1) * (floor(end / 10**pos) - 1) + end + 1 - 10**pos * floor(end / 10**pos)
    
    
    
    
    
    if start - 1 < 1:
        return total
    
    for pos in range(1, floor(log10(start - 1)) + 1):
        
        
        
        
        
        digit_at_pos = ((start - 1) % 10**pos) // 10**(pos - 1)
        
        
        
        
        
        
        
        if pos == 1 or digit_at_pos != 0:
            total -= 10**(pos - 1) * floor((start - 1) / 10**pos)
        else:
            
            
            
            
            
            
            
            total -= 10**(pos - 1) * (floor((start - 1) / 10**pos) - 1) + start - 10**pos * floor(start / 10**pos)
    
    return total
    
    
    
    
"""
"""

if __name__ == "__main__":
    
    
    
    
    
    
    result = list()
    input_lines = open(0, "r").read().splitlines()[:-1]
    i = 0
    while i < len(input_lines):
        
        
        
        
        
        
        
        
        
        
        
        
        start_num, end_num = map(int, input_lines[i].split(" "))
        result.append(str(count_zero_digits(start_num, end_num)))
        i += 1
    open(1, "w").write("\n".join(result))