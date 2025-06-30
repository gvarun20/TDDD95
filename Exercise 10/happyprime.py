import sys


def is_prime(n: int) -> bool:

    if n <= 1:
        return False
        
        
        
        
    if n <= 3:
        return True
        
        
    if n % 2 == 0 or n % 3 == 0:
        return False
        
        
    i = 5
    
    
    
    w = 2
    while i * i <= n:
        
        
        if n % i == 0:
            return False
        i += w
        
        
        
        w = 6 - w
    return True



def is_happy(n: int) -> bool:

    def digit_square_sum(num):
        total = 0
        
        
        while num > 0:
            digit = num % 10
            
            
            total += digit * digit
            num //= 10
        return total
    
    slow = fast = n
    
    
    while True:
        
        
        
        slow = digit_square_sum(slow)
        
        
        
        fast = digit_square_sum(digit_square_sum(fast))
        if fast == 1:
            
            
            return True
            
            
        if slow == fast:
            return False

def is_happy_prime(n: int) -> bool:

    return is_prime(n) and is_happy(n)


def main():
    

    
    
    input = sys.stdin.read().split()
    idx = 0
    
    
    
    T = int(input[idx])
    
    
    
    idx += 1
    
    
    
    for _ in range(T):
        
        
        
        
        K = int(input[idx])
        m = int(input[idx+1])
        
        
        
        
        
        idx += 2
        verdict = "YES" if is_happy_prime(m) else "NO"
        
        
        
        print(K, m, verdict)
        
        

if __name__ == "__main__":
    main()