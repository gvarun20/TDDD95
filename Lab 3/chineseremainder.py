import math
import sys

"""
test calculation: a=1,b=2,n=2,m=3
try gcd(2,3)=1,,next we do this(1-2)%1=0 so we can confirm that there is a solution.
now we go into the algo 2*(-1)+3*1=1 where x=-1 and y=1,, now the k value need to find(2-1)/1=1.
so at this time x0 will come to 1+(-1)*1*2=-1,,if we do lcm(2,3)=6 and then x0 mod 6 will be 5
if this logic works it might work for other as well.

here in this function we calculate the greatest common divisor of 2 integer .
so if there is b=0  a(x)+b(y) = gcd (a,b) it will return as (a,1,0)
here the algorithm works by repetedly applying gcd(a,b)=gcd(b,a%b)),
it keeps a track of how the reminder can be told as a blend of a,b.



This code solves a math issue where by one must instantly get a number that fits both of the leftover rules.
Consider the amount that returns a particular left when divide by one value and a different provided remaining 
when half by a different value. In this case, you might need a value that, when parted equal 7, gets an excess
of 3, and when broken by 11, gets a remainder of 5. Such numbers can be identified using this formula.
In order to connect the two demands a program first finds unique factors using the Enhanced Euclidean 
Formula. Next that, it decides if a solution can truly practical due to often both remaining 
rules conflict and nobody may satisfy both.

If an option is found, the formula finds a pattern range and the least positive value that works. This implies that
by adding multiples of this interval, you can obtain an endless number of additional solutions if you discover one.
Every example that the main code reads offers you two distinct remain conditions. It either finds the pattern gap 
and the solution number to each instance that or it says that there fails to be one. In short, this issue fixes the
Chinese Remainder Theorem issue.
"""


def extended_gcd(a, b):
    
    if b == 0:
        
        return (a, 1, 0)
        
    else:
        
        gcd, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        
        
        return (gcd, x, y)








"""
the function solve_congruence takes four integers as input: a, n, b, and m
starts by calling and computes the greatest common divisor (GCD) of n and m.
next it checks for solution existance it is done by verifying if(a-b)%gcd is zero.
if there is a solution it calculates the lcm of n,m.next is where we calculate the x0 using the formula a+x*k*n.

"""

def solve_congruence(a, n, b, m):
    
    gcd, x, y = extended_gcd(n, m)
    
    
    if (a - b) % gcd != 0:
        return None 
        
        
    lcm = n * m // gcd    

    
    
    
    k = (b - a) // gcd
    x0 = a + x * k * n
    x0 %= lcm
    
    
    return (x0, lcm)















def main():
    
    

    input = sys.stdin.read().split()
    T = int(input[0])
    index = 1
    
    
    for _ in range(T):
        
        
        a = int(input[index])
        n = int(input[index + 1])
        b = int(input[index + 2])
        m = int(input[index + 3])
        index += 4
        result = solve_congruence(a, n, b, m)
        
        
        if result is None:
            
            print("there is no solution")
            
            
        else:
            
            
            x, K = result
            
            
            print(x, K)
        
        

if __name__ =="__main__":
    main()
