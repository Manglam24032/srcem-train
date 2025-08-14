# Print top half of a diamond pattern for n = 5

n = 5  # Width of the widest part (must be odd)

# Only print the top half (including the middle row)
for i in range(1, n + 1, 2):  # i = 1, 3, 5
    spaces = (n - i) // 2
    print(" " * spaces + "*" * i)
