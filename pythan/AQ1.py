def unique_elements(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

# Example usage
input_list = [1, 2, 2, 3, 4, 1, 5]
output = unique_elements(input_list)
print("Output:", output)



# Assignment2
