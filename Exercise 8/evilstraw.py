import sys
from collections import Counter


"""
To identify the least amount of adjacent swaps need to make the string s into a palindromes,, apply the min_swaps_to_palindrome(s) function.  A phrase like "madam" or "racecar" 
that read the exact same way back as front is known as a palindrome.  The function at first checks when altering the text into palindromes is even possible.  
It will this by calculating the number of words with an odd rate using the useful function can_form_palindrome.  Only one line—the mid line in an 
uneven-length palindrome—can have an odd number so as for a palindrome to be conceivable. 
If a single character has an odd number, "Impossible" is given back by this function.

The string is turned into a set to allow swap if it is able to produce a palindrome from it.  Text matching is done by two pointers: i and j .  
The lines have moved inward and the initials at i and j are in the right place if they fit.
The approach looks from j backwards to i to find a letter that fits s[i] if they don't meet. 
If a match is found, the nearby swaps are made to shift that character to the j on the right, 
and each swap is added.  Since s[i] is the middle character in the a circle if no match arises,
it is moved a place to the right untill it reaches its centre.

"""

def min_swaps_to_palindrome(s):
    def can_form_palindrome(s):
        freq = Counter(s)
        odd_count = sum(1 for count in freq.values() if count % 2 != 0)
        return odd_count <= 1

    if not can_form_palindrome(s):
        return "Impossible"

    s = list(s)
    n = len(s)
    swaps = 0
    i, j = 0, n - 1

    while i < j:
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            k = j
            while k > i and s[k] != s[i]:
                k -= 1
            if k == i:
                s[i], s[i + 1] = s[i + 1], s[i]
                swaps += 1
            else:
                while k < j:
                    s[k], s[k + 1] = s[k + 1], s[k]
                    swaps += 1
                    k += 1
                i += 1
                j -= 1

    return swaps


lines = sys.stdin.read().splitlines()
t = int(lines[0])
for i in range(1, t + 1):
    s = lines[i].strip()
    print(min_swaps_to_palindrome(s))
