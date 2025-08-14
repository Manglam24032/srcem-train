def rotate_list(lst, k):
    if not lst:
        return []
    k = k % len(lst)  # Ensure k is within bounds
    return lst[-k:] + lst[:-k]

# Example usage
input_list = [1, 2, 3, 4, 5]
k = 2
output = rotate_list(input_list, k)
print("Rotated list:", output)