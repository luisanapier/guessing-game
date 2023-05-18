"""A number-guessing game."""

# Put your code here
import random

guest = input("Welcome to the Guessing game. What's your name? ")
player_name = print(f"{guest}, I'm thinking of a number between 1 and 100. ")

score = 0
numbers_guesses = random.randint(1,100)

while True:
    guess = input("Try to guess my number. ")
    guess = int(guess)

    if guess != numbers_guesses:
        if guess < numbers_guesses:
            print("Your guess is too low. Try again.")
            score += 1 
        elif guess > numbers_guesses:
            print("Your guess is too high. Try again.")
            score += 1
    else:
        print(f"Well done {guest}! You got it right in {score} guesses!")
        play_again = input("Would you like to play again? y/n ")
        score = 0
        if play_again == "yes":
            continue
        else:
            break