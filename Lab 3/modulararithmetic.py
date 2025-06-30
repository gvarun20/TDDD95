import sys
import math


"""
here in this extended_gcd find the greatest common divisor for the input a,b.
we have 2 cases ,once is the base case when a=0 so x=0and y=1,it returns (b,0,1)
in recursive case for example gcd(30,50),iter1 50/30 =1 and remainder is 20 ,,now we will check (30,20)
iter2 30/20=1 reminder is 10 so will check gcd(20,10).
iter3 20/10=2 reminder is 0 so we stop the gcd here  

"""

def extended_gcd(a, b):


    if a == 0:

        return (b, 0, 1)
    
    else:

        g, y, x = extended_gcd(b % a, a)

        return (g, x - (b // a) * y, y)
    

'''
the main need is to find the modular inverse of a under the modulo m, it used 
the extended_gcd to get g,x,y this algo will find the x and y so that a*x+m*y=1
if the idx is greater than the list length ,read the current line and there will be an increment of the idx
n,t n represet the modulus and t represent the number of operations.
The line is split into two parts, which are converted to integers n and t
if there is any case that n,t are both 0 it will exit the loop.
the main process for each operation in the test case ,here it works for each operation and reads the next line
it splits the line into different parts (x,op,y)
and then converts x,y into integers.
x: First part converted to integer (left operand).
op: Second part (operator: +, -, *, /).
y: Third part converted to integer (right operand).
what it does in the code is it out performs modular arithmetic operations (+, -, *, /), with modular inverses is being used here that do division. 
Here it simply takes (x op y) mod n and it does the addition, subtraction, multiplication. To achieve the modular inverse of y, the extended Euclidean algorithm 
is invoked after first checking for division by zero, which returns -1 if the condition is met. Only if n and y are coprime (gcd(y,n)=1) will there exist an inverse; otherwise it returns -1. 
Division becomes x multiplied by the modular inverse of y when it is true. Each operation is followed by an immediate printout of the results.
With modulus 1000, say 1/999 is okay (since 999 and 1000 are coprime) and is 999 (since 999*999 mod 1000 = 1), 
but 1/998 will not work (gcd(998,1000)=2), and returns -1.

The total complexity is O(t * log n) per test case, where t is operations and n is modulus. extended_gcd() is O(log min(a,b)). +,-,* are O(1) time per operation in modular arithmetic. 
Since there are t operations per test case,the total complexity is O(t log n).
'''

def mod_inverse(a, m):

    g, x, y = extended_gcd(a, m)

    if g != 1:

        return None  # modular inverse doesn't exist
    else:

        return x % m

def main():
    """Main function to process input and perform operations"""
    while True:
        # Read first line of test case
        line = sys.stdin.readline()
        
        
        if not line:
            break  # End of input
        
        line = line.strip()
        
        if not line:
            continue  # Skip empty lines
        
        # Parse n and t
        try:
            n, t = map(int, line.split())
        except:
            break  # Invalid input format
        
        # Termination condition
        if n == 0 and t == 0:
            break
        
        # Process each operation
        for _ in range(t):
           
            op_line = sys.stdin.readline().strip()
            
            
            if not op_line:
                continue  
            
         
            try:
                x, op, y = op_line.split()
                x = int(x)
                y = int(y)
            except:
                print(-1)  # Invalid operation format
                continue
            
            # Perform the operation
            if op == '+':
                result = (x + y) % n
            elif op == '-':
                result = (x - y) % n
            elif op == '*':
                result = (x * y) % n
            elif op == '/':
                if y == 0:
                    result = -1  # Division by zero
                else:
                    inv = mod_inverse(y, n)
                    if inv is None:
                        result = -1  # No inverse exists
                    else:
                        result = (x * inv) % n
            else:
                result = -1  # Invalid operator
            
            print(result)

if __name__ == "__main__":
    main()

