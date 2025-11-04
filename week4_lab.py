"""
In this file, i am answering the tasks set in lab week 4.
"""

#This function is part of Exercise 2
def celsius_to_fahrenheit(celsius_temp):
    #This converts the users input (degrees in celsius) and output the conversion to fehrenheit.
    fahrenheit_temp = (celsius_temp * 9/5) + 32
    return(fahrenheit_temp)


#Exercise 1 - create a number guessing game

#This imports the random python module so i ca then call on it later.
import random

#This sets the variable random_num into a random int between 1 and 101(exclusive).
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


#Exercise 2 - Defining functions

#This asks the user for the temp to then call the function using the user input
c_temp = input("Enter a temperature in celsius:")
#This converts the user input to a int so i can be used in equasion
c_temp_integer = int(c_temp)
f_temp = celsius_to_fahrenheit(c_temp_integer)

#This prints the funtion return value
print(f"{c_temp}C is equal to {f_temp}F")


#Exercise 3 - Understanding scope
"""
In this exercise, i defined a variable outside of the function to dementrate a glabal varible.
I have then chnged that varaible in the function and printed the outcome and then the glabal variable with the same name which has not changed.
This hapens becase a any variables used i in a ftion are destroyed after that function is closed unless stored seperately outside as global varible.
"""

global_variable = "I am global"

def test_scope():
    global_variable = "I am local"
    return global_variable

print(test_scope())
print(global_variable)