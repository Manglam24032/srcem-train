def count_consonants(s):
    consonants = "bcdfghjklmnpqrstvwxyz"
    count = 0
    for char in s.lower():
        if char in consonants:
            count += 1
    return count

# Example usage
input_string = "hello world"
result = count_consonants(input_string)
print("Number of consonants:", result)
