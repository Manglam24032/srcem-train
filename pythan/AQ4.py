def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))

# Example usage
number = 12345
result = sum_of_digits(number)
print("Sum of digits:", result)