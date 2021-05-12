##################################################################################################################

#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

##################################################################################################################

#imports
import random
from art import logo

#Defines for game level attempts
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# Function that sets difficulty
def set_difficulty():
    level = input("\nChoose a difficulty. Type 'easy' or 'hard: ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


# Function that checks the users guess
def check_answer(guess, answer, turns):
    if guess > answer:
        print("\nToo high.")
        return turns-1
    elif guess < answer:
        print("\nToo low.")
        return turns-1
    else:
        print(f"\nYou got it! The answer was {answer}!")


def game():
    # Printing the game logo
    print(logo)

    # Choose random number
    answer = random.randint(1, 100)
    
    # Print for debug
    #print(f"Correct Answer: {answer}")
    
    print("\nWelcome to the Number Guessing Game!")
    print("\nI am thinking of a number between 1 and 100...")

    # Asking user to set their difficulty
    turns = set_difficulty()

    # while loop that is utilized to repeat the game until the user gets the answer correct or runs out of attempts
    guess = 0
    while guess != answer and turns != 0:
        # Displaying to the user how many attempts they have
        print(f"\nYou have {turns} attempts remaining")

        # Let user guess their number
        guess = int(input("\nGuess a number: "))

        # Checking the user's answer
        turns = check_answer(guess, answer, turns)
        
        if turns == 0:
            print(f"\nThe number was {answer}!")
            return
        elif guess != answer:
            print(f"\nIncorrect answer. Guess again!")


# Calling the game function
game()
