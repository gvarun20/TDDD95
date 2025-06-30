def build_string_from_suffixes(suffix_data: list[tuple[str, int]], target_length: int) -> str:


    result = ["*"] * target_length

    for suffix, start_pos in suffix_data:
        
        
        
        
        
        
        current_pos = start_pos

        for i in range(len(suffix)):
            
            
            
            
            if suffix[i] == "*":
                
                current_pos += target_length - start_pos - len(suffix)
                continue

            
            if i + current_pos >= target_length:
                return "IMPOSSIBLE"



            
            if result[i + current_pos] == "*":
                result[i + current_pos] = suffix[i]
                
                
                
                
            elif result[i + current_pos] != suffix[i]:
                return "IMPOSSIBLE"


    if "*" in result:
        return "IMPOSSIBLE"
        
    return "".join(result)
    
    
    
def process_input():

    import sys
    input_lines = sys.stdin.read().splitlines()[1:]
    output = []
    idx = 0

    while idx < len(input_lines):
        
        
        
        
        length, num_suffixes = map(int, input_lines[idx].split())
        idx += 1

        suffixes = []
        
        
        
        
        
        for _ in range(num_suffixes):
            
            
            
            
            pos, suffix = input_lines[idx].split()
            suffixes.append((suffix, int(pos) - 1))  
            idx += 1

        output.append(build_string_from_suffixes(suffixes, length))

    print("\n".join(output))


    
    
    
    
if __name__ == "__main__":
    process_input()

