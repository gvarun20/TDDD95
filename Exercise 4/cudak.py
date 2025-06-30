import math

# Constants for maximum length of numbers and digit sum
MAX_LENGTH = 17
MAX_SUM = 136



# Precomputed table for counting numbers with specific digit sums
digit_sum_table = [[0] * MAX_SUM for _ in range(MAX_LENGTH)]











def initialize_table():##this function is needed do not change
    
    global digit_sum_table
    digit_sum_table[0][0] = 1
    for i in range(10):#this sums the table of the range 
        digit_sum_table[1][i] = 1
        
        
        
    for length in range(2, MAX_LENGTH):#it checks in the for loop the maximum length 
        for sum_value in range(MAX_SUM):
            for digit in range(10):
                if sum_value - digit >= 0:
                    digit_sum_table[length][sum_value] += digit_sum_table[length - 1][sum_value - digit]
# Iterates through possible digits up to `last_digit - 1`
# This ensures that we correctly count numbers with a smaller most significant digit.















def count_numbers_with_sum(n, target_sum):
    """Count numbers in range [1, n] with digit sum equal to target_sum."""
    if target_sum < 0:
        return 0
    if n == 0:
        return 1 if target_sum == 0 else 0
        




# Uses binary search to efficiently find the first number in the range [A, B] with the required digit sum.
# The approach reduces the search space logarithmically.

    
    total_count = num_length = 0
    number = n
    
    
    
    
    
    while number:
        last_digit = number % 10
        number //= 10
        num_length += 1
    
    if num_length == 1:
        return 1 if target_sum <= n else 0
    
    
    
    for digit in range(last_digit):
        if target_sum - digit >= 0:
            total_count += digit_sum_table[num_length - 1][target_sum - digit]
    
    return total_count + count_numbers_with_sum(n - last_digit * (10 ** (num_length - 1)), target_sum - last_digit)
# Uses binary search to efficiently find the first number in the range [A, B] with the required digit sum.
# The approach reduces the search space logarithmically.

def find_first_number(A, B, target_sum):
    """Find the smallest number in range [A, B] with digit sum equal to target_sum."""
    low, high = A, B
    
    while low != high:
        
        
        mid = (low + high + 1) // 2
        
        if count_numbers_with_sum(mid, target_sum) - count_numbers_with_sum(low, target_sum):
            high = mid - 1
        else:
            low = mid
    return low + 1

def main():
    
    
    initialize_table()#calling the table and map it 
    
    
    A, B, S = map(int, input().split())
    print(count_numbers_with_sum(B, S) - count_numbers_with_sum(A - 1, S))
    print(find_first_number(A, B, S))#print the same 

if __name__ == "__main__":
    main()#try this might work
