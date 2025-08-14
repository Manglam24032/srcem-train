def char_frequency(s):
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

# Example usage
text = "hello"
result = char_frequency(text)
print("Character frequencies:", result)