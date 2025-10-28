"""
The challenge for week 4 is to crete a calculator that can perform + - * /.
I will do this by first asking for the oporator and then the input numbers.
I will use functions to have it easily repeatable aswell as a While True loop to keep the code running.
"""


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

while True:

    user_selection_input = input("Please choose from ( + - * / )")

    num_1 = input("Please input your first number:")
    num_1_float = float(num_1)
    num_2 = input("Please input your first number:")
    num_2_float = float(num_2)

    if user_selection_input == "+":

        print(add(num_1_float, num_2_float))
    elif user_selection_input == "-":
        print(subtract(num_1_float, num_2_float))
    elif user_selection_input == "*":
        print(multiply(num_1_float, num_2_float))
    elif user_selection_input == "/":
        print(divide(num_1_float, num_2_float))
    else:
        print("Error! Try agin")

