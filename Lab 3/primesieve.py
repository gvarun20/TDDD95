#def check_bit(bit_array, position):
#    return not (bit_array[position // 8] & (1 << (position % 8)))
##
#    sieve = bytearray((limit + 8) // 8)#
#    sieve = bytearray((limit + 8) // 8)
#
import sys


#def check_bit(bit_array, position):
#    return not (bit_array[position // 8] & (1 << (position % 8)))
    
"""
This function checks whether a number is prime by looking at a pre-calculated "map" of bits (a bitmap). 
It's basically a cheat sheet where every bit represents a number: 0 = prime, 1 = not prime.

It first calculates which byte and bit to look at (number//8 for the byte, number%8 for the bit).
Then it looks at that bit—if it looks at 0, the number is prime (True), otherwise not (False).
"""
def check_prime_status(bitmap, number):

    byte_index = number // 8
    bit_position = number % 8
    return not (bitmap[byte_index] & (1 << bit_position))

#def flip_bit(bit_array, position):
#    bit_array[position // 8] ^= (1 << (position % 8))

"""
This function, update_bitmap, marks a number as non-prime in a bitmap (an efficient way of representing prime/non-prime flags). 
It calculates the actual bit for the number and flips it to 1, i.e., "not prime."
It calculates the right byte (number // 8) and bit position (number % 8) first. 
Then it uses a bitwise OR operation (|= (1 << bit_position)) to set that bit to 1.


"""
def update_bitmap(bitmap, number):
    
    byte_index = number // 8
    bit_position = number % 8
    bitmap[byte_index] |= (1 << bit_position)









#
#def compute_primes(limit):
#    if limit < 2:
#        return bytearray(), 0

#
#    sieve = bytearray((limit + 8) // 8)
#    sieve[0] |= 0b11  # Mark 0 and 1 as non-prime
#
#

#ef compute_primes(limit):
#   
#   
#   
#   if limit < 2:
#       return bytearray(), 0




#   sieve = bytearray((limit + 8) // 8)
#   sieve[0] |= 0b11  # Mark 0 and 1 as non-prime



#   count = limit - 1  # Start by counting all numbers, then subtract non-primes














"""

This is a Sieve of Eratosthenes implementation with a bitmap for quick identification of primes to a given limit.
It marks non-primes by systematically setting to zero multiples of each prime found.
The function first handles edge cases and sets up a bytearray where a bit represents a number being either prime or composite.
Even numbers greater than 2 are marked as composite. The main sieve then processes odd numbers, marking multiples of each prime found.
Having O(n·log log n) time complexity, it achieves near-linear time through optimizations: processing only odd numbers, 
starting elimination from p², and stepping by 2p. The bitmap keeps memory usage at a minimum to n/8 bytes plus overhead.Returns a dense bitmap for O(1) 
primality tests along with the number of primes. This dual output is useful both for batch generation of primes and 
for individual prime testing in memory-constrained environments like embedded systems or competitive programming.


"""




def calculate_primes(limit):

    if limit < 2:
        return bytearray(), 0
    
    # Initialize bitmap (0=prime, 1=composite)
    prime_map = bytearray((limit + 8) // 8)
    prime_counter = 0
    
    
    
    
    

    # Handle special cases
    update_bitmap(prime_map, 0)
    update_bitmap(prime_map, 1)
    
    
    
    
    
    

    # Process even numbers
    for composite in range(4, limit + 1, 2):
        update_bitmap(prime_map, composite)






    # Main sieve algorithm
    for candidate in range(3, limit + 1, 2):
        
        
        
        if check_prime_status(prime_map, candidate):
            prime_counter += 1
            # Mark odd multiples
            
            
            for multiple in range(candidate * candidate, limit + 1, candidate * 2):
                
                
                update_bitmap(prime_map, multiple)

    # Account for 2 being prime
    return prime_map, prime_counter + 1

def execute_program():

    data = sys.stdin.read().split()
    pointer = 0
    upper_bound = int(data[pointer])
    pointer += 1
    query_count = int(data[pointer])
    pointer += 1




    prime_data, total_primes = calculate_primes(upper_bound)
    print(total_primes)

    output = []
    for _ in range(query_count):
        
        
        
        
        num = int(data[pointer])
        pointer += 1
        output.append('1' if check_prime_status(prime_data, num) else '0')
    
    print('\n'.join(output))

if __name__ == "__main__":
    execute_program()


#   for num in range(2, int(limit**0.5) + 1):
#       
#       
#       
#       if check_bit(sieve, num):
#           
#           
#           
#           for multiple in range(num*num, limit+1, num):
#               
#               
#               
#               if check_bit(sieve, multiple):
#                   flip_bit(sieve, multiple)
#                   count -= 1



#   # Adjust count for numbers 0 and 1
#   count -= 2
#   return sieve, count
#
#
#
#







#
##
#    sieve = bytearray((limit + 8) // 8)#
#    sieve = bytearray((limit + 8) // 8)    # Adjust count for numbers 0 and 1
#    count -= 2
#    return sieve, count
#    
# #    for _ in range(Q):
#        x = int(input[ptr])
#        ptr += 1

#    prime_flags, prime_count = compute_primes(N)
#    print(prime_count)#    prime_flags, prime_count = compute_primes(N)
#    print(prime_count)
#        if x <= N:
#            results.append('1' if check_bit(prime_flags, x) else '0')
#        else:
#            results.append('0')
##
#    sieve = bytearray((limit + 8) // 8)       
#def flip_bit(bit_array, position):


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
#
#
#
#
#
#def main():

#    Q = int(input[ptr])
#    ptr += 1
#
#    prime_flags, prime_count = compute_primes(N)
#    print(prime_count)
#
#    results = []

#    print('\n'.join(results))
#
#


#def main():
#    
#    
#    
#
#    input = sys.stdin.read().split()
#    ptr = 0
#    N = int(input[ptr])
#    ptr += 1
#    Q = int(input[ptr])
#    ptr += 1
#
#
#    prime_flags, prime_count = compute_primes(N)
#    
#    
#    
#    print(prime_count)
#
#    results = []
#    
#    
#    
#    for _ in range(Q):
#        x = int(input[ptr])
#        ptr += 1
#        
        
        
#        
#        if x <= N:
#            results.append('1' if check_bit(prime_flags, x) else '0')
#        else:
#            results.append('0')
#    
#    print('\n'.join(results))
#    
#    
#    
#    
#
#if __name__ == "__main__":
#    main()
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
#if __name__ == "__main__":
#    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    