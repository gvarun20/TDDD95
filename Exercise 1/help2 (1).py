#def is_variable(word):
#    """Checks if a word starts with '<', indicating it's a variable."""
#    return word.startswith("<")
#
#def align_phrases(phrase1, phrase2):
#    """
#    Aligns two phrases by substituting variables where possible.
#
#    Returns:
#        - The aligned phrase as a string if successful.
#        - "-" if the phrases cannot be aligned.
#    """
#    for i in range(len(phrase1)):
#        word1 = phrase1[i]
#        word2 = phrase2[i]
#
#        if word1 != word2:
#            if is_variable(word1):
#                phrase1 = [word2 if w == word1 else w for w in phrase1]
#            elif is_variable(word2):
#                phrase2 = [word1 if w == word2 else w for w in phrase2]
#            else:
#                return "-"
#
#    # Check for consistency in variable/non-variable presence
#    for i in range(len(phrase1)):
#        word1 = phrase1[i]
#        word2 = phrase2[i]
#        if is_variable(word1) != is_variable(word2):
#            return align_phrases(phrase1, phrase2)  # Recursive call if inconsistency found
#
#    return " ".join("w" if is_variable(w) else w for w in phrase1)
#
#if __name__ == "__main__":
#    testcases = int(input())
#    for _ in range(testcases):
#        phrase1 = input().split()
#        phrase2 = input().split()
#        print(align_phrases(phrase1, phrase2))#
"""
this function tries to align or to merge two sentences by replacing variables
in one single sentence .the function continues to do that word after word ,
if it is changing it again verifies whether it is variable .if word1 is a variable it 
replaces all the occurrences of the word1 in sentence1 with word2.Then the function processes,
the function verifies that variables in both sentences are properly aligned.if alignment occurs,
it returns sentence1 with variables replaced with "w".this is how it works




"""


def is_variable(token):

    return token.startswith("<")

def align_sentences(sentence1, sentence2):

    for i in range(len(sentence1)):
        word1 = sentence1[i]
        word2 = sentence2[i]

        if word1 != word2:
            
            
            if is_variable(word1):
                sentence1 = [word2 if token == word1 else token for token in sentence1]
            elif is_variable(word2):
                sentence2 = [word1 if token == word2 else token for token in sentence2]
            else:
                return "-"


    for i in range(len(sentence1)):
        
        
        if is_variable(sentence1[i]) != is_variable(sentence2[i]):
            
            
            return align_sentences(sentence1, sentence2)

    return " ".join("w" if is_variable(token) else token for token in sentence1)

if __name__ == "__main__":
    
    
    num_cases = int(input())
    
    
    for _ in range(num_cases):
        
        
        sentence1 = input().split()
        sentence2 = input().split()
        
        
        print(align_sentences(sentence1, sentence2))
