def get_prefix(tree: list[int], idx: int) -> int:
    
    
    total = 0
    
    
    
    
    
    
    while idx > 0:
        total += tree[idx]
        idx -= idx & -idx
    return total
    
    
    
    

def update_tree(tree: list[int], idx: int, value: int):
    
    
    
    
    idx += 1  # 1-based indexing
    
    
    while idx < len(tree):
        tree[idx] += value
        idx += idx & -idx
        
        

def query_single(tree: list[int], idx: int) -> int:
    return query_range(tree, idx + 1, idx)
    
    
    
    
    
    

    

def query_range(tree: list[int], start: int, end: int) -> int:
    return get_prefix(tree, end) - get_prefix(tree, start)
    
    
    
    
    
    
    
    
    
    

def init_tree(size: int) -> list[int]:
    return [0] * (size + 1)









def process(elements: list[int]) -> list[int]:
    bit = init_tree(len(elements))
    
    
    
    
    
    

    for i in range(len(elements)):
        update_tree(bit, i, 1)
        
        
        
        
        

    sorted_with_indices = sorted([(val, idx) for idx, val in enumerate(elements)])
    left = 0
    right = len(elements) - 1
    
    
    
    
    
    
    
    output = []

    for step in range(len(elements)):
        if step % 2 == 0:
            
            
            
            
            
            _, idx = sorted_with_indices[left]
            update_tree(bit, idx, -1)
            output.append(query_range(bit, 0, idx + 1))
            left += 1
            
            
            
            
            
            
        else:
            _, idx = sorted_with_indices[right]
            update_tree(bit, idx, -1)
            
            
            
            
            
            output.append(query_range(bit, idx, len(elements)))
            right -= 1

    return output

def compute_result(data: list[int]) -> list[int]:
    
    return process(data)







if __name__ == "__main__":
    
    
    
    
    
    
    output_text = ""
    input_data = open(0, "r").read()
    values = list(map(int, input_data.split("\n")[1:-1]))
    
    
    
    
    
    
    

    output_text += "\n".join(map(str, compute_result(values)))
    open(1, "w").write(output_text)
