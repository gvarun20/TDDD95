def push(stack: list[frozenset]) -> None:
    
    
    
    
    stack.append(frozenset())
    
    
    

def duplicate(stack: list[frozenset]) -> None:
    
    
    
    
    stack.append(stack[-1])
    
    
    
    

def union(stack: list[frozenset]) -> None:
    
    
    
    
    first = stack.pop()
    second = stack.pop()
    stack.append(first | second)




def intersect(stack: list[frozenset]) -> None:
    
    
    
    
    first = stack.pop()
    second = stack.pop()
    stack.append(first & second)

def add(stack: list[frozenset]) -> None:
    
    
    
    
    
    
    top_element = stack.pop()
    second_element = stack.pop()
    stack.append(second_element | {hash(top_element)})
    



    
    
    
    

def process_operations(operations: list[str]) -> list[int]:





    operation_handlers = {
        "PUSH": push,
        "DUP": duplicate,
        "UNION": union,
        "INTERSECT": intersect,
        "ADD": add,
    }





    result = []
    stack = []




    for operation in operations:
        
        
        
        
        operation_handlers[operation](stack)
        result.append(len(stack[-1]))
        
        
        
        
        

    return result




def solve(operations: list[str]) -> list[int]:
    
    
    
    return process_operations(operations)






def main() -> None:
    
    
    
    
    import sys
    input_data = sys.stdin.read().splitlines()
    operations = input_data[1:]
    
    output = []
    current_index = 0
    
    
    
    
    
    while current_index < len(operations):
        
        
        
        
        
        operation_count = int(operations[current_index])
        current_index += 1
        
        test_case_operations = operations[current_index:current_index + operation_count]
        current_index += operation_count
        
        results = solve(test_case_operations)
        output.extend(map(str, results))
        output.append("***")
    
    
    
    
    
    sys.stdout.write("\n".join(output) + "\n")
    
    



    
if __name__ == "__main__":
    main()
