"""A number-guessing game."""

# Put your code here
import random

guest = input("Welcome to the Guessing game. What's your name? ")
player_name = input(f"{guest}, I'm thinking of a number between 1 and 100. ")


numbers_guesses = random.randint(1,100)

while True:
    guess = input("Try to guess my number. ")
    guess = int(guess)

    if guess != numbers_guesses:
        if guess < numbers_guesses:
            print("Your guess is too low. Try again.")

        elif guess > numbers_guesses:
            print("Your guess is too high. Try again.")
    else:
        print(f"Well done {guest}! You got it right!")
