import random
import time

def roll_dice():
    return random.randint(1, 6)

def dice_game():
    while True:
        print("Welcome to the Dice Game!")
        player_score = 0
        computer_score = 0

        rounds = 5  # Set the number of rounds to play
        for round_number in range(1, rounds + 1):
            print(f"\nRound {round_number}/{rounds}: Rolling the dice...")
            time.sleep(5)  # Add delay for better pacing
            player_roll = roll_dice()
            computer_roll = roll_dice()

            print(f"You rolled: {player_roll}")
            print(f"Computer rolled: {computer_roll}")

            if player_roll > computer_roll:
                print("You win this round!")
                player_score += 1
            elif computer_roll > player_roll:
                print("Computer wins this round!")
                computer_score += 1
            else:
                print("It's a tie this round!")

            print(f"\nCurrent Score:\nYou: {player_score} | Computer: {computer_score}")

        print("\nFinal Score:")
        print(f"You: {player_score} | Computer: {computer_score}")
        if player_score > computer_score:
            print("Congratulations! You won the game!")
        elif computer_score > player_score:
            print("Better luck next time. The computer won the game.")
        else:
            print("It's a tie game!")

        # Ask if the user wants to play again
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye!")
            break

# Start the game
dice_game()
