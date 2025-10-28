"""
In this file, i am answering the tasks set in lab week 4.
"""

#Exercise 1 - create a number guessing game
#This imports the random python module so i ca then call on it later
import random

#This sets the variable random_num into a random int between 1 and 101(exclusive)
random_num = random.randint(0, 101)

#This loop asks the user to guess the number generated until they guess it.
while True:
    user_guess = input("Guess the number:")
    user_guess_integer = int(user_guess)

    if user_guess_integer == random_num:
        print(f"Congratulations! You guessed it, {random_num} was the random number.")
        break
    elif user_guess_integer >= random_num:
        print("Too High! Try again.")
    elif user_guess_integer <= random_num:
        print("Too Low! Try again.")