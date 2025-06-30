
"""
A program called this that read a listing of text and then scans 
texts to find out the number of separate word terms are are within 
each message acts as that code does.  It properly saves and looks for words via 
an information structure called as a Trie.

 The dictionary phrases are then read off the data provided and placed 
 into the Trie by the computer.  The Trie help in fast deciding if a message's portion
 matches a given dictionary word.  The program examines letters until it comes upon a # and |
 divider after fetching the word list.
 
 
 It finds the greatest number of dictionary phrases and are not overlapping 
 for every message via dynamic code.  It checks all possible substring beginning at 
 each point as it reads the message from the very beginning.  After a word appears, 
 the count is modified to take note of the ideal word sequence that minimises overlap.
 The most of phrases is a result of each text.
 
"""

#
#import sys
#
#class TrieNode:
#    def __init__(self):
#        self.children = {}
#        self.is_word = False
#        
#
#class Trie:
#    def __init__(self):
#        self.root = TrieNode()
#
#    def insert(self, word):
#        
#        
#        
#        node = self.root
#        for c in word:
#            
#            
#            
#            
#            
#            if c not in node.children:
#                
#                
#                
#                
#                
#                
#                
#                
#                node.children[c] = TrieNode()
#            node = node.children[c]
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
#        node.is_word = True
#
#    def find_words_from(self, text, start):
#        
#        
#        
#        
#        
#        
#        node = self.root
#        for i in range(start, min(len(text), start + 10)):
#            c = text[i]
#            
#            
#            
#            
#            
#            
#            
#            
#            
#            if c not in node.children:
#                break
#            
#            
#            
#            
#            
#            
#            node = node.children[c]
#            if node.is_word:
#                yield i + 1
#
#def max_non_overlapping_substrings(message, trie):
#    n = len(message)
#    
#    
#    
#    
#    dp = [0] * (n + 1)
#    for i in range(n - 1, -1, -1):
#        dp[i] = dp[i + 1]
#        
#        
#        
#        
#        
#        for end in trie.find_words_from(message, i):
#            if end <= n:
#                
#                
#                
#                
#                
#                dp[i] = max(dp[i], 1 + dp[end])
#    return dp[0]
#
#def main():
#    
#    
#    
#    
#    
#    
#    
#    lines = [line.rstrip() for line in sys.stdin if line.strip() != '']
#    i = 0
#    trie = Trie()
#    
#    
#    
#    
#    
#    
#    
#    
#    
#    while lines[i] != '#':
#        trie.insert(lines[i])
#        
#        
#        
#        
#        
#        
#        
#        
#        i += 1
#    i += 1
#    
#    
#    
#    
#    
#    
#    
#    
#    while i < len(lines) and lines[i] != '#':
#        message = ''
#        
#        
#        
#        
#        
#        while i < len(lines) and lines[i] != '|':
#            message += lines[i]
#            
#            
#            
#            
#            
#            
#            i += 1
#        i += 1
#        result = max_non_overlapping_substrings(message, trie)
#        print(result)
#        
#        
#        
#
#if __name__ == "__main__":
#    main()


def compute_lps_array(input_str: str) -> list[int]:
    lps = [0] * len(input_str)






    for current_idx in range(1, len(input_str)):
        prev_lps = lps[current_idx - 1]
        
        
        
        
        
        
        
        
        
        while prev_lps > 0 and input_str[current_idx] != input_str[prev_lps]:
            prev_lps = lps[prev_lps - 1]
            
            
            
            
            
            
            
            
            
        if input_str[current_idx] == input_str[prev_lps]:
            prev_lps += 1
            
            
            
            
            
            
            
        lps[current_idx] = prev_lps

    return lps


def pattern_search(search_pattern: str, main_text: str):
    found_positions = list()










    combined_str = f"{search_pattern}{chr(0)}{main_text}"
    lps_array = compute_lps_array(combined_str)








    pattern_len = len(search_pattern)
    total_len = pattern_len + len(main_text) + 1
    
    
    
    
    
    
    
    
    
    for idx in range(pattern_len + 1, total_len):
        
        
        
        
        
        
        
        
        if lps_array[idx] == pattern_len:
            found_positions.append(idx - 2 * pattern_len)

    return found_positions

def decode_space_transmission(lexicon: list[str], transmission: str) -> int:
    coverage_ranges = list()
    
    
    
    
    
    
    
    

    for lexicon_entry in lexicon:
        
        
        
        
        
        
        
        
        for start_pos in pattern_search(lexicon_entry, transmission):
            coverage_ranges.append((start_pos, start_pos + len(lexicon_entry)))

    decoded_count = 0
    current_position = 0






    for range_start, range_end in sorted(coverage_ranges, key=lambda x: x[1]):
        
        
        
        
        
        
        
        
        
        if range_start < current_position:
            continue

        decoded_count += 1
        current_position = range_end
        
        
        
        
        
        
        

    return decoded_count










if __name__ == "__main__":
    
    
    
    
    
    
    
    
    result_buffer = list()
    input_lines = open(0, "r").read().splitlines()

    line_pointer = 0

    word_database = list()
    
    
    received_transmissions = list()

    while input_lines[line_pointer] != "#":
        
        
        
        
        
        
        
        word_database.append(input_lines[line_pointer])
        line_pointer += 1

    line_pointer += 1
    
    current_transmission = ""

    while input_lines[line_pointer] != "#":
        
        
        
        
        
        
        line_content = input_lines[line_pointer]
        current_transmission += line_content

        if "|" in current_transmission:
            
            
            
            
            
            result_buffer.append(str(decode_space_transmission(word_database, current_transmission[:-1])))
            current_transmission = ""

        line_pointer += 1




    open(1, "w").write("\n".join(result_buffer))









































#