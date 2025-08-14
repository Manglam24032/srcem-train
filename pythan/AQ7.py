# Reverse words in a sentence without using split() or reverse()

def reverse_words(sentence):
    words = []
    word = ""
    
    # Step 1: Extract words manually
    for char in sentence:
        if char != " ":
            word += char
        else:
            if word:
                words.append(word)
                word = ""
    if word:
        words.append(word)  # Append the last word

    # Step 2: Reverse the list manually
    reversed_words = []
    for i in range(len(words) - 1, -1, -1):
        reversed_words.append(words[i])

    # Step 3: Join the words manually with space
    result = ""
    for i in range(len(reversed_words)):
        result += reversed_words[i]
        if i != len(reversed_words) - 1:
            result += " "

    return result

# Example usage
sentence = "Python is fun"
result = reverse_words(sentence)
print("Reversed:", result)
