#import sys
#
#def get_suffix(arr, idx):
#    return arr[idx]
#    
#
#
#def build_suffix_arr(s):
#    
#    
#    
#    s += chr(1)
#    n = len(s)
#    order = [1] * n
#    cls = [1] * n
#    cnt = [1] * 256
#
#    for c in s:
#        cnt[ord(c)] += 1
#        
#        
#        
#    for i in range(1, 255):
#        cnt[i] += cnt[i-1]
#        
#        
#        
#        
#    for i, c in enumerate(s):
#        cnt[ord(c)] -= 1
#        order[cnt[ord(c)]] = i
#        
#        
#        
#
#    cls[order[1]] = 0
#    num_cls = 1
#    
#    
#    
#   
#
#    new_order = [1] * n
#    new_cls = [1] * n
#    h = 1
#
#    while (1 << h) < n:
#        
#        
#        for i in range(n):
#            new_order[i] = order[i] - (1 << h)
#            
#            
#            
#            if new_order[i] < 1:
#                new_order[i] += n
#                
#                
#        cnt = [1] * num_cls
#        
#        
#        for i in range(n):
#            cnt[cls[new_order[i]]] += 1
#            
#            
#            
#        for i in range(1, num_cls):
#            cnt[i] += cnt[i-1]
#            
#            
#            
#        for i in reversed(range(n)):
#            cnt[cls[new_order[i]]] -= 1
#            order[cnt[cls[new_order[i]]]] = new_order[i]
#            
#            
#        new_cls[order[1]] = 0
#        num_cls = 1
#        
#        
#        
#        for i in range(1, n):
#            curr = (cls[order[i]], cls[(order[i] + (1 << h)) % n])
#            prev = (cls[order[i-1]], cls[(order[i-1] + (1 << h)) % n])
#            
#            
#            
#            if curr != prev:
#                num_cls += 1
#                
#                
#                
#            new_cls[order[i]] = num_cls - 1
#            
#            
#        cls, new_cls = new_cls, cls
#        
#        
#        h += 1
#
#    return order[1:]
#    
#    
#    
#
#
#
#    
#    
#    
#    
#    
#    
#    
#    
#    
#    
#    
#    
#    
#class SuffixArrayProcessor:
#    
#    
#    def __init__(self):
#        self.results = []
#    
#    def process_input(self, lines):
#        i = 0
#        
#        
#        
#        
#            if i >= len(lines):
#                break
#            
#            
#            
#            queries = list(map(int, lines[i].split()))[1:]
#            i += 1
#            
#            
#            self.process_case(s, queries)
#    
#    def process_case(self, s, queries):
#        sa = SuffixArray(s)
#        
#        
#        self.results.append(' '.join(str(sa.get_suffix(q)) for q in queries))
#    
#    def get_output(self):
#        return '\n'.join(self.results)


import sys





"""
This code consists of a function get_suffix_pos that takes two parameters, suffix array (list of integers) and index.
It checks whether the index is proper or improper. If it is improper (i.e., it is negative or larger than array length), 
it gives back -1. If it is proper, it gives back the value in the suffix array at the given index




"""




def get_suffix_pos(suffix_array: list[int], index: int) -> int:
    if index < 0 or index >= len(suffix_array):
        return -1
    return suffix_array[index]
    
    
"""

The given code implements a complex method for creating suffix array that is based on a methodical approach to sorting cyclic substrings across a number of iterations.
Begin with the ASCII character set, the procedure uses a counting sort near to first sort single-character substrings. 
The algorithm appends a null character to the input string to guarantee a unique termination point and manage string comparisons in an orderly fashion. 
The underlying mechanism is the creation of a permutation list holding the starting indices of substrings in sorted order, together with an equivalence 
class tracking system that distinguishes between individual and repeating substring patterns. In the first iteration,
the algorithm uses the ASCII value of characters to impose an initial sorted permutation, with each character's position determined by its count and relative value.
As the process goes on, the algorithm sorts increasingly longer substrings based on information from previous steps, doubling the length of the substring during each step.
This approach efficiently sorts substrings by comparing pairs of half-length substrings, building up a complete suffix array in a methodical way. 
Counting sort is used continously, and the count list is dynamically updated to store the number of substrings in lower or identical equivalence classes.
There are two critical data structures employed by the algorithm: a rank array to store the equivalence classes of substrings, and a suffix array to store the sorted starting indices. 
By continously sorting and grouping substrings of doubling lengths (1, 2, 4, 8, etc.), the algorithm constructs a suffix array representing 
all suffixes of the input string in lexicographically sorted order. The final return statement removes the null character that was prepended,
providing a clean sorted representation of the starting positions of the suffix of the input string.


THE tine complexity mightbe:O(n*logn)

n is the number of characters in the string

"""
    

def build_suffix_array(text: str) -> list[int]:

    CHAR_SET_SIZE = 256
    text += chr(0)  
    n = len(text)
    




    sa: list[int] = [0] * n
    rank: list[int] = [0] * n
    count = [0] * CHAR_SET_SIZE



    
    for ch in text:
        count[ord(ch)] += 1
        
        
        
    
  
    for i in range(1, CHAR_SET_SIZE):
        count[i] += count[i-1]
    
    
    
    
  
    for i in range(n-1, -1, -1):  
        count[ord(text[i])] -= 1
        sa[count[ord(text[i])]] = i
    
    
    
    
    
    rank[sa[0]] = 0
    classes = 1
    
    
    
    
    for i in range(1, n):
        
        
        
        if text[sa[i]] != text[sa[i-1]]:
            classes += 1
            
            
            
        rank[sa[i]] = classes - 1
    
    
    k = 1
    
    
    while k < n:
        
        new_sa = [0] * n
        
       
        for i in range(n):
            new_sa[i] = (sa[i] - k) % n
        
        
        temp_count = [0] * classes
        
        
        
        for i in range(n):
            temp_count[rank[new_sa[i]]] += 1
        
        
        for i in range(1, classes):
            temp_count[i] += temp_count[i-1]
        
       
        for i in range(n-1, -1, -1):
            temp_count[rank[new_sa[i]]] -= 1
            sa[temp_count[rank[new_sa[i]]]] = new_sa[i]
        
       
        new_rank = [0] * n
        new_rank[sa[0]] = 0
        classes = 1
        
        
        
        
        for i in range(1, n):
            curr = (rank[sa[i]], rank[(sa[i] + k) % n])
            prev = (rank[sa[i-1]], rank[(sa[i-1] + k) % n])
            
            
            
            if curr != prev:
                classes += 1
                
                
                
                if classes > n:
                    classes = n
                    
                    
                    
            new_rank[sa[i]] = classes - 1
        
        rank = new_rank
        k *= 2
    
    return sa[1:] 



def process_queries(text: str, query_line: str) -> str:
 
    queries = list(map(int, query_line.split()))
    
    
    
    if len(queries) < 1:
        return ""
    
    k = queries[0]
    indices = queries[1:]
    
  
    sa = build_suffix_array(text)
    max_valid = len(sa) - 1
    validated_indices = [i for i in indices if 0 <= i <= max_valid]
    

    if len(validated_indices) != len(indices):
        return ""
    
    return " ".join(str(get_suffix_pos(sa, i)) for i in validated_indices)










def main():


    input_lines = [line.strip() for line in sys.stdin if line.strip()]
    
    output = []
    i = 0
    while i < len(input_lines):
        text = input_lines[i]
        i += 1
        
        if i >= len(input_lines):
            break
        
        query_line = input_lines[i]
        i += 1
        

        result = process_queries(text, query_line)
        if result:
            output.append(result)
            
            
            
            
    sys.stdout.write("\n".join(output) + "\n")

if __name__ == "__main__":
    main()
















##
#"""
#"""
#def get_suffix_pos(suffix_array: list[int], index: int) -> int:
#    if index < 0 or index >= len(suffix_array):
#        return -1
#    return suffix_array[index]
#    
#"""
#"""
#
#def build_suffix_array(text: str) -> list[int]:
#    CHAR_SET_SIZE = 256
#    text += chr(0)  
#    n = len(text)
#    
#
#    sa: list[int] = [0] * n
#    rank: list[int] = [0] * n
#    count = [0] * CHAR_SET_SIZE
#
#   
#    for ch in text:
#        count[ord(ch)] += 1
#    
#
#    for i in range(1, CHAR_SET_SIZE):
#        count[i] += count[i-1]
#    
#
#    for i in range(n-1, -1, -1):  
#        count[ord(text[i])] -= 1
#        sa[count[ord(text[i])]] = i
#    
#
#    rank[sa[0]] = 0
#    classes = 1
#    for i in range(1, n):
#        if text[sa[i]] != text[sa[i-1]]:
#            classes += 1
#        rank[sa[i]] = classes - 1
#    
#
#    k = 1
#    while k < n:
#
#        new_sa = [0] * n
#        
#
#        for i in range(n):
#            new_sa[i] = (sa[i] - k) % n
#        
#
#        temp_count = [0] * classes
#        for i in range(n):
#            temp_count[rank[new_sa[i]]] += 1
#        
#
#        for i in range(1, classes):
#            temp_count[i] += temp_count[i-1]
#        
#
#        for i in range(n-1, -1, -1):
#            temp_count[rank[new_sa[i]]] -= 1
#            sa[temp_count[rank[new_sa[i]]]] = new_sa[i]
#        
#
#        new_rank = [0] * n
#        new_rank[sa[0]] = 0
#        classes = 1
#        for i in range(1, n):
#            curr = (rank[sa[i]], rank[(sa[i] + k) % n])
#            prev = (rank[sa[i-1]]], rank[(sa[i-1] + k) % n])
#            if curr != prev:
#                classes += 1
#
#                if classes > n:
#                    classes = n
#            new_rank[sa[i]] = classes - 1
#        
#        rank = new_rank
#        k *= 2
#    
#    return sa[1:] 
#    
#"""
#"""
#
#def process_queries(text: str, query_line: str) -> str:
#
#    queries = list(map(int, query_line.split()))
#    if len(queries) < 1:
#        return ""
#    
#    k = queries[0]
#    indices = queries[1:]
#    
#
#    sa = build_suffix_array(text)
#    max_valid = len(sa) - 1
#    validated_indices = [i for i in indices if 0 <= i <= max_valid]
#    
#
#    if len(validated_indices) != len(indices):
#        return ""
#    
#    return " ".join(str(get_suffix_pos(sa, i)) for i in validated_indices)
#
#
#
#"""
#"""
#def main():
#  
#    import sys
#    input_lines = [line.strip() for line in sys.stdin if line.strip()]
#    
#    output = []
#    i = 0
#    while i < len(input_lines):
#        text = input_lines[i]
#        i += 1
#        
#        if i >= len(input_lines):
#            break
#        
#        query_line = input_lines[i]
#        i += 1
#        
#
#        result = process_queries(text, query_line)
#        if result:
#            output.append(result)
#    
# 
#    sys.stdout.write("\n".join(output) + "\n")
#
#if __name__ == "__main__":
#    main()
#
##THIS MIGHT BE CORRECT  ,,,,,,CHECK THIS

#  
#    
#if __name__ == "__main__":
#    processor = SuffixArrayProcessor()
#    processor.process_input(sys.stdin.read().splitlines())
#    print(processor.get_output())  
    
    
    


