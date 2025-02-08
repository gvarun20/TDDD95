def is_variable(word):
    """Checks if a word starts with '<', indicating it's a variable."""
    return word.startswith("<")

def align_phrases(phrase1, phrase2):
    """
    Aligns two phrases by substituting variables where possible.

    Returns:
        - The aligned phrase as a string if successful.
        - "-" if the phrases cannot be aligned.
    """
    for i in range(len(phrase1)):
        word1 = phrase1[i]
        word2 = phrase2[i]

        if word1 != word2:
            if is_variable(word1):
                phrase1 = [word2 if w == word1 else w for w in phrase1]
            elif is_variable(word2):
                phrase2 = [word1 if w == word2 else w for w in phrase2]
            else:
                return "-"

    # Check for consistency in variable/non-variable presence
    for i in range(len(phrase1)):
        word1 = phrase1[i]
        word2 = phrase2[i]
        if is_variable(word1) != is_variable(word2):
            return align_phrases(phrase1, phrase2)  # Recursive call if inconsistency found

    return " ".join("w" if is_variable(w) else w for w in phrase1)

if __name__ == "__main__":
    testcases = int(input())
    for _ in range(testcases):
        phrase1 = input().split()
        phrase2 = input().split()
        print(align_phrases(phrase1, phrase2))