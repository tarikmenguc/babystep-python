import random

# Welcome message
print("Welcome to the Number Guessing Game!")

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)
guess = None
attempts = 0
max_attempts = 6

# Main game loop
while attempts < max_attempts:
    # Get the user's guess
    guess = int(input("I'm thinking of a number between 1 and 100. Guess what it is: "))
    attempts += 1  # Increment the attempt counter

    # Check if the guess is correct
    if guess < secret_number:
        print("Too low!")  # Hint: The secret number is higher
    elif guess > secret_number:
        print("Too high!")  # Hint: The secret number is lower
    else:
        # If the guess is correct, congratulate the user and end the game
        print(f"Congratulations! You guessed the number in {attempts} tries.")
        break

# If the user runs out of attempts
if guess != secret_number:
    print(f"Sorry, you've run out of attempts. The number was {secret_number}.")