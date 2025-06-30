def get_unacceptable(words: list[str]) -> list[set[str]]:
    unacceptable = [set(words)]
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    for _ in range(3):
        unacceptable_words = set()
        
        
        
        
        
        
        
        
        for word in unacceptable[-1]:
            for i in range(len(word) - 1):
                
                
                
                
                
                
                
                new_word = word[:i] + word[i + 1] + word[i] + word[i + 2:]
                
                
                
                
                
                if len(new_word) == len(word):
                    unacceptable_words.add(new_word)
                    
                    
                    
                    
        unacceptable.append(unacceptable[-1].union(unacceptable_words))
    return unacceptable







def is_acceptable(unacceptable_words: list[set], password: str):
    
    
    
    
    
    
    
    
    digits = sum(map(lambda x: x.isdigit(), password))
    if digits > 3:
        
        
        
        
        
        
        
        return True
    
    word_list = list(unacceptable_words[3 - digits])
    
    
    
    
    
    
    
    
    
    for word in word_list:
        if len(password) != len(word):
            continue
        
        
        
        
        
        
        
        matches = 0
        for i in range(len(password)):
            if word[i] == password[i] or password[i].isdigit():
                
                
                
                
                
                
                
                
                
                
                matches += 1
        
        if matches == len(password):
            return False
            
            
            
            
            
            
            
            
            
            
            
    return True

if __name__ == "__main__":
    
    
    
    
    
    
    
    
    
    output = list()
    lines = open(0, "r").read().splitlines()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    n = int(lines[0])
    index = 1
    words = list()
    
    
    for _ in range(n):
        word = str(lines[index])
        
        
        
        
        
        
        words.append(word)
        index += 1
        
    unacceptable_words = get_unacceptable(words)
    
    
    
    
    
    
    while index < len(lines):
        
        
        
        
        password = lines[index]
        current_password = password
        
        
        
        
        
        
        
        
        
        if is_acceptable(unacceptable_words, current_password):
            output.append(password)
            
            
            
            
            
            
            
            
            
            
            
        index += 1
        
        
    result = "\n".join(str(x) for x in output)
    
    
    
    
    open(1, "w").write(result)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    