"""A number-guessing game."""

# Put your code here
import random

guest = input("Welcome to the Guessing game. What's your name? ")
guess = input(f"{guest}, I'm thinking of a number between 1 and 100. Can you guess? ")
guess = int(guess)

