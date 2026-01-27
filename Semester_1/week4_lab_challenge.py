"""
The challenge for week 4 is to crete a calculator that can perform + - * /.
I will do this by first asking for the oporator and then the input numbers.
I will use functions to have it easily repeatable aswell as a While True loop to keep the code running.
"""

#These are the functions used to perfom the oporator mathmatics
def add(a, b):
    add_results = (a + b)
    return add_results

def subtract(a, b):
    subtract_results = (a - b)
    return subtract_results

def multiply(a, b):
    multiply_results = (a * b)
    return multiply_results

def divide(a, b):
    divide_results = (a / b)
    return divide_results

#This while true loop keeps the code running and repeats the calculator oporator choise prompt
while True:

    user_selection_input = input("Please choose from ( + - * / )")

    #Converts inputs to floats
    num_1 = input("Please input your first decimal number:")
    num_1_float = float(num_1)
    num_2 = input("Please input your second decimal number:")
    num_2_float = float(num_2)

    if user_selection_input == "+":

        print(add(num_1_float, num_2_float))
    elif user_selection_input == "-":
        print(subtract(num_1_float, num_2_float))
    elif user_selection_input == "*":
        print(multiply(num_1_float, num_2_float))
    elif user_selection_input == "/":
        print(divide(num_1_float, num_2_float))
    #This else is a failsafe for if the user does ot input a number
    else:
        print("Error! Try agin")

