"""
This program use a simple start doubling near to create the suffix array for a given input text. , 
a suffix array is a set of all a string's suffix sorted in dictionary order.


Firstly, a particular  char is put to the end of its input string by the code. This letter,
which is shorter than the rest, help in showing the end of the string. With that, it initialises 
arrays to hold the equivalence classes (class_group) and suffix positions (suffix_pos), as well as a
time array to monitor the frequency of each character's usage.




The algorithm applies the counting sort for setting up the suffixes based to their first word.
From the first character, it then gives every suffix a similarity class, and is a sort of subgroup
classification. Two ends are in the same class if they start at the exact same character.

It then enters into a cycle where it keeps repeating the duration of the ordering prefix. It ranks entire 
suffixes by to the subclasses of the first and second parts of their existing prefix rather than grouping them
right away, which is weak. Again, counting sort is used nicely for this.
It updates their class groups using each pair of half and adjusts the suffix spots after each round.
If a prefix's length matches or reaches the length of the text, the cycle keeps going.
Since the initial entry matches an extra  word, it is removed before returning the suffix array. 
A list of all the input string's suffixes, start places in order of sorts is the last output


"""







def build_suffix_array(text: str) -> list[int]:
    
    
    
    ALPHABET_SIZE = 256
    text += chr(0)  # Append sentinel character

    suffix_pos = [0] * len(text)
    class_group = [0] * len(text)
    freq = [0] * ALPHABET_SIZE



    for char in text:
        freq[ord(char)] += 1



    for i in range(1, ALPHABET_SIZE):
        freq[i] += freq[i - 1]




    for idx, char in enumerate(text):
        freq[ord(char)] -= 1
        suffix_pos[freq[ord(char)]] = idx



    class_group[suffix_pos[0]] = 0
    num_classes = 1


    for i in range(1, len(text)):
        
        
        if text[suffix_pos[i]] != text[suffix_pos[i - 1]]:
            num_classes += 1
            
            
            
        class_group[suffix_pos[i]] = num_classes - 1

    new_pos = [0] * len(text)
    new_class = [0] * len(text)
    h = 0

    while (1 << h) < len(text):
        
        
        for i in range(len(text)):
            new_pos[i] = suffix_pos[i] - (1 << h)
            
            
            if new_pos[i] < 0:
                new_pos[i] += len(text)

        freq = [0] * num_classes
        
        
        for i in range(len(text)):
            freq[class_group[new_pos[i]]] += 1



        for i in range(1, num_classes):
            freq[i] += freq[i - 1]



        for i in reversed(range(len(text))):
            freq[class_group[new_pos[i]]] -= 1
            suffix_pos[freq[class_group[new_pos[i]]]] = new_pos[i]



        new_class[suffix_pos[0]] = 0
        num_classes = 1



        for i in range(1, len(text)):
            
            
            curr_pair = (
                class_group[suffix_pos[i]],
                class_group[(suffix_pos[i] + (1 << h)) % len(text)]
            )
            prev_pair = (
                class_group[suffix_pos[i - 1]],
                class_group[(suffix_pos[i - 1] + (1 << h)) % len(text)]
            )



            if curr_pair != prev_pair:
                num_classes += 1
            new_class[suffix_pos[i]] = num_classes - 1



        class_group, new_class = new_class, class_group
        h += 1

    return suffix_pos[1:]  




"""
the process creates the rank array, capturing every suffix's place in a
suffix collection. This allows easy finding of a suffix's neighbours in an 
order of sorts. At it, it initialises an LCP array, and its parts will all 
have the full length for the same start between two near suffixes found in
the suffix collection.The program utilises each word individually to see if 
any they will match for each place i in the text, looking at the next suffix 
in the ordered list . The LCP array is in which it stores this total.



time complexity: O(n) - n is the length of the string.

"""

def build_lcp_array(text: str, suffix_array: list[int]) -> list[int]:

    n = len(text)
    rank = [0] * n

    for i in range(n):
        rank[suffix_array[i]] = i
        
        
        

    lcp = [0] * (n - 1)
    k = 0

    for i in range(n):
        
        
        
        if rank[i] == n - 1:
            k = 0
            
            
            continue

        j = suffix_array[rank[i] + 1]
        
        
        
        while i + k < n and j + k < n and text[i + k] == text[j + k]:
            k += 1



        lcp[rank[i]] = k
        
        
        if k > 0:
            k -= 1

    return lcp


if __name__ == "__main__":
    input_text = open(0, "r").readlines()[1].strip()
    sa = build_suffix_array(input_text)
    lcp = build_lcp_array(input_text, sa)
    open(1, "w").write(str(max(lcp)))
