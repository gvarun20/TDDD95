#def flip_digit(digit):
#    flip_map = {'0': '0', '1': '1', '5': '2', '6': '9', '8': '8', '9': '6'}
#    return flip_map.get(digit, None)
#
#def is_valid_upside_down(num):
#    num_str = str(num)
#    for digit in num_str:
#        if flip_digit(digit) is None:
#            return False
#    return True
#
#def get_upside_down_number(num):
#    num_str = str(num)
#    flipped_digits = []
#    
#    for digit in reversed(num_str):
#        flipped = flip_digit(digit)
#        if flipped is None:
#            return None
#        flipped_digits.append(flipped)
#    
#    return ''.join(flipped_digits)
#
#valid_numbers = []
#
#def precompute_valid_numbers(max_k=10000):
#    global valid_numbers
#    if len(valid_numbers) >= max_k:
#        return
#    
#    valid_numbers = []
#    count = 0
#    num = 1
#    
#    while count < max_k:
#        if is_valid_upside_down(num):
#            valid_numbers.append(get_upside_down_number(num))
#            count += 1
#        num += 1
#
#def find_kth_valid_number(k):
#    if k > len(valid_numbers):
#        precompute_valid_numbers(max(k, 10000))
#    return valid_numbers[k-1]
#
#def test_solution():
#    print("Testing the solution:")
#    
#    print("First 10 valid upside-down numbers:")
#    for i in range(1, 11):
#        result = find_kth_valid_number(i)
#        print(f"K={i}: {result}")
#    
#    print("\nTesting specific cases:")
#    test_cases = [1, 5, 10, 20]
#    for k in test_cases:
#        result = find_kth_valid_number(k)
#        print(f"K={k}: {result}")
#
#def solve_input():
#    print("Enter K values (one per line, empty line to stop):")
#    
#    while True:
#        try:
#            line = input().strip()
#            if not line:
#                break
#            k = int(line)
#            result = find_kth_valid_number(k)
#            print(result)
#        except (ValueError, EOFError):
#            break
#

#
#def flip_digit(digit):
#    flip_map = {'0': '0', '1': '1', '5': '2', '6': '9', '8': '8', '9': '6'}
#    return flip_map.get(digit, None)
#
#
#
#
#
#
#
#
#def is_valid_upside_down(num):
#    num_str = str(num)
#    
#    
#    
#    
#    
#    for digit in num_str:
#        
#        
#        
#        
#        
#        if flip_digit(digit) is None:
#            return False
#    return True
#
#def get_upside_down_number(num):
#    
#    
#    
#    
#    
#    
#    num_str = str(num)
#    flipped_digits = []
#    
#    for digit in reversed(num_str):
#        flipped = flip_digit(digit)
#        
#        
#        
#        
#        
#        if flipped is None:
#            return None
#            
#            
#            
#            
#            
#            
#            
#        flipped_digits.append(flipped)
#    
#    return ''.join(flipped_digits)
#
#valid_numbers = []
#
#def precompute_valid_numbers(max_k=10000):
#    
#    
#    
#    
#    
#    
#    
#    
#    global valid_numbers
#    
#    
#    
#    
#    
#    if len(valid_numbers) >= max_k:
#        
#        
#        
#        
#        
#        
#        
#        return
#    
#    valid_numbers = []
#    count = 0
#    num = 1
#    
#    while count < max_k:
#        
#        
#        
#        
#        
#        
#        if is_valid_upside_down(num):
#            
#            
#            
#            
#            
#            
#            valid_numbers.append(get_upside_down_number(num))
#            count += 1
#        num += 1
#
#def find_kth_valid_number(k):
#    
#    
#    
#    
#    
#    if k > len(valid_numbers):
#        
#        
#        
#        
#        
#        
#        
#        precompute_valid_numbers(max(k, 10000))
#    return valid_numbers[k-1]
#
#precompute_valid_numbers(1000)
#
#while True:
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
#    try:
#        k = int(input())
#        print(find_kth_valid_number(k))
#    except EOFError:
#        break
#




#def flip_digit(digit):
#    
#    
#    
#    
#    flip_map = {'0': '0', '1': '1', '5': '5', '6': '9', '8': '8', '9': '6'}
#    
#    
#    
#    
#    return flip_map.get(digit, None)
#
#def is_valid_upside_down(num):
#    
#    
#    
#    
#    num_str = str(num)
#    
#    
#    
#    
#    
#    for digit in num_str:
#        
#        
#        
#        
#        if flip_digit(digit) is None:
#            return False
#            
#            
#            
#            
#    return True
#    
#
#def get_upside_down_number(num):
#    
#    
#    
#    
#    num_str = str(num)
#    flipped_digits = []
#    
#    for digit in reversed(num_str):
#        flipped = flip_digit(digit)
#        
#        
#        
#        
#        
#        
#        if flipped is None:
#            return None
#            
#            
#            
#            
#            
#        flipped_digits.append(flipped)
#    
#    return ''.join(flipped_digits)
#
#valid_numbers = []
#
#def precompute_valid_numbers(max_k=10000):
#    
#    
#    
#    
#    
#    
#    global valid_numbers
#    
#    
#    
#    
#    
#    if len(valid_numbers) >= max_k:
#        return
#    
#    valid_numbers = []
#    count = 0
#    num = 1
#    
#    while count < max_k:
#        
#        
#        
#        
#        
#        
#        
#        if is_valid_upside_down(num):
#            upside_down = get_upside_down_number(num)
#            valid_numbers.append(upside_down)
#            count += 1
#        num += 1
#
#def find_kth_valid_number(k):
#    
#    
#    
#    
#    
#    if k > len(valid_numbers):
#        
#        
#        
#        
#        
#        precompute_valid_numbers(max(k, 10000))
#        
#        
#        
#        
#        
#    return valid_numbers[k-1]
#
#precompute_valid_numbers(1000)
#
#while True:
#    try:
#        
#        
#        
#        
#        k = int(input())
#        print(find_kth_valid_number(k))
#    except EOFError:
#        break
#
def to_base_seven(num: int) -> list[int]:
    if num == 0:
        return [0]
    
    digits = list()

    while num != 0:
        digits.append(num % 7)
        num = num // 7

    return digits
    
def map_to_valid_digits(value: int) -> list[int]:
    allowed_digits = [0, 1, 2, 5, 9, 8, 6]
    return [*map(lambda x: allowed_digits[x], to_base_seven(value))]

if __name__ == "__main__":
    results = list()
    input_data = open(0, "r").read()
    values = map(int, input_data.split("\n")[:-1])

    for value in values:
        results.append("".join(map(str, map_to_valid_digits(value))))

    open(1, "w").write("\n".join(results))







