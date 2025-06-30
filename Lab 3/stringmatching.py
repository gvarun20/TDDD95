import sys
"""
Here we make a function that predicts a function for kruth moris algorithm
At first we initialize an array that has the length as the pattern
the j keeps looks for the length of the  present longest suffix.
we start a loop from the 2nd character of the patttern to compute the prefix values.
using the prefix array it backtracks until there is a match if found or else it becomes 0.
if there is a match the j will be incremented.





Prefix Function (Preprocessing): To start, we generate a prefix array (LPS array) of the same length as the pattern.
This array will hold values representing the length of the longest proper prefix which is also a proper suffix for every substring of the pattern. 
The function sets the first value to 0 as a single character has no proper prefix/suffix. With two pointers (i for iteration and j for prefix length),
we analyze the pattern and match characters. For every match, j is incremented and that value is saved in the prefix array. For mismatches we backtrack 
using previously computed values in the prefix array until we reach a match or until we are at the start. This step takes O(n) time where n is the length of the pattern.






O(n+m) is the time complexity, here n is the pattern's length.
m is the text's length.
Split up:: O(n+m) from the prefix function's generation.
-O(m) from iterating by the created prefix function's pattern portion.
-Final:: = O(n+m)
"""
def compute_prefix_function(pattern):
    
    
    
    prefix = [0] * len(pattern)
    j = 0
    
    
    
    for i in range(1, len(pattern)):
        
        
        
        while j > 0 and pattern[i] != pattern[j]:
            j = prefix[j - 1]
            
            
            
        if pattern[i] == pattern[j]:
            j += 1
            prefix[i] = j
        else:
            prefix[i] = 0
            
            
            
    return prefix


'''


The main function is this KMP search to look for all the patterns in the imput text .
we have a smallsection which tells if there is a empty list of either pattern or text.
the pattern goes to the above prefix function,j is set to 0 to keep a track of the current position.
we then iterate through each character in the complete text .
checks and moves along the next character in the pattern to look on match
if there is a entire pattern that has been matched it records the start position of the match.
after completing everything it returns the list of stsrting positions of the matche




KMP Search Function: The search function starts with considering edge cases like empty pattern or text which results in empty list return. 
We set j (index of pattern) to 0 and create an empty list where we store the positions of the matches. While going over every character of the text,
we try to optimally handle mismatches with the prefix array instead of starting over the comparisons from the start of the pattern. With a match of characters,
we shift both pointers.



'''


def kmp_search(pattern, text):
    
    
    
    if not pattern or not text:
        return []
        
        
    prefix = compute_prefix_function(pattern)
    j = 0
    positions = []
    
    
    for i in range(len(text)):
        
        while j > 0 and text[i] != pattern[j]:
            j = prefix[j - 1]
            
            
        if text[i] == pattern[j]:
            j += 1
            
        if j == len(pattern):
            positions.append(i - len(pattern) + 1)  # Fixed this line
            j = prefix[j - 1]
            
            
    return positions
    
    
    
    
    
def main():
    lines = sys.stdin.read().splitlines()
    results = []
    for p, t in zip(lines[::2], lines[1::2]):
        results.append(' '.join(map(str, kmp_search(p,t))))
    print('\n'.join(results))
    
    
    
    
if __name__ == "__main__":
    main()