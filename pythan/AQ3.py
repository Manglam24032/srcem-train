def longest_word(sentence):
    words = sentence.split()
    longest = max(words, key=len)
    return longest

# Example usage
sentence = "Python is an amazing programming language"
result = longest_word(sentence)
print("Longest word:", result)