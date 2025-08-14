secret_number = 8  # You can change this to any number

while True:
    guess = input("Guess the number: ")
    
    # Check if input is a valid integer
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue
    
    guess = int(guess)
    
    if guess == secret_number:
        print("Correct! You guessed it.")
        break
    else:
        print("Wrong, try again.")
