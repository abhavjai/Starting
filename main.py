# Import module
import random

# Ask if the user wants to play again
play = input("Would you like to play the number-guessing game? (Y for yes, N for No): ")

# If the player wants to play
while play == 'Y':
    # Set number of attempts to 0
    attempts = 0
    
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    # Ask the user to guess the number
    guess = int(input("Guess the number between 1 and 100: "))
    
    # Loop until the guess is correct
    while guess != secret_number:
        attempts += 1  # Increment attempts for each guess
        
        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        
        # Ask for another guess
        guess = int(input("Guess again: "))
    
    # Add one more attempt for the final guess
    attempts += 1
    
    # Display ending message
    print(f"Congratulations! You guessed the number in {attempts} attempts.")
    
    # Ask if the user wants to play again
    play = input("Would you like to play again? (Y for yes, N for No): ")

# If the player does not want to play
print("Okay, have a good day!")


