import math

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

def compute_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def add_fractions(fraction1, fraction2):
    numerator = fraction1.numerator * fraction2.denominator + fraction2.numerator * fraction1.denominator
    denominator = fraction1.denominator * fraction2.denominator
    common_divisor = compute_gcd(numerator, denominator)
    numerator //= common_divisor
    denominator //= common_divisor
    return Fraction(numerator, denominator)

def find_minimal_fraction(decimal_str, repeat_start):
    minimal_fraction = Fraction(1, 999999999999999999)
    for repeat_length in range(2, repeat_start):  # repeat_length is the length of the non-repeating part
        non_repeating_denominator = 10 ** (repeat_length - 2)
        non_repeating_numerator = 0
        for i in range(2, repeat_length):
            non_repeating_numerator = non_repeating_numerator * 10 + int(decimal_str[i])
        non_repeating_fraction = Fraction(non_repeating_numerator, non_repeating_denominator)
        
        repeating_numerator = 0
        for i in range(repeat_length, repeat_start):
            repeating_numerator = repeating_numerator * 10 + int(decimal_str[i])
        repeating_denominator = (10 ** (repeat_start - repeat_length) - 1) * non_repeating_denominator
        repeating_fraction = Fraction(repeating_numerator, repeating_denominator)
        
        combined_fraction = add_fractions(non_repeating_fraction, repeating_fraction)
        if combined_fraction.denominator < minimal_fraction.denominator:
            minimal_fraction = combined_fraction
    return minimal_fraction

def main():
    while True:
        decimal_input = input().strip()
        repeat_position = decimal_input.find("..")
        if repeat_position != -1:
            result_fraction = find_minimal_fraction(decimal_input, repeat_position)
            print(f"{result_fraction.numerator}/{result_fraction.denominator}")
        else:
            break

if __name__ == "__main__":
    main()