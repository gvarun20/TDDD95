factorial_result = 1

for number in range(1, int(input()) + 1):

    # The factorial part.
    factorial_result *= number

    # Remove trailing zeroes.
    while factorial_result % 10 == 0:
        factorial_result //= 10
    
    # Truncate the result.
    factorial_result %= 1000000000000

# Print the last three digits of the result.
print(str(factorial_result)[-3:])
