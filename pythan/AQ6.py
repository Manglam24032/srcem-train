for num in range(1, 101):
    if (num % 3 == 0) ^ (num % 5 == 0):  # XOR: true if only one condition is true
        print(num, end=' ')