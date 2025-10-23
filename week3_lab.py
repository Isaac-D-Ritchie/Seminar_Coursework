""""
This file contains the code for week 3 lab excercises,
focusing on for loops, while loops, and GitHub intergration.
"""

#Task 1 + 2
#This prints only the even numbers between 0 and 20
for i in range(0, 20, 2):
   print(f"\n {i + 1}")

#This seperates the outputs
print()

#Task 3
#This code takes a list of costs and adds then displaying the cost as it adds and the total cost.
costs= [15.00, 12.50, 3.75, 40.25]
total_cost = 0

for cost in costs:
    total_cost = total_cost + cost
    print(f"£{total_cost: .2f}")

print (f"Your total cost is £{total_cost: .2f}")

#This seperates the outputs
print()

#Here is the code to print a 5x5 grid if *
for line in range(5):
    for colum in range(5):
        print("*", end=" ")
    print()

#This seperates the outputs
print()

#Here i have created code to print a 5x5 right-angle trange
layer = 1
for line in range(5):
    print("* " * layer )
    layer = layer + 1
print()

#Task 4 - The While Loop
#Creating a calculator, i am choosing to ourput to 2dp

#here i have used a defned function to compute the mathmatics with reduced code
def addition(num1, num2):
    print(f"{num1} + {num2} = {(num1 + num2):.2f}")

def subtraction(num1, num2):
    print(f"{num1} - {num2} = {(num1 - num2):.2f}")

#this while true statement repeats until told to stop
while True:
    print("--- Calculator Meanu ---")
    print("1. Add")
    print("2. Subtract")
    print("q. Quit")
    user_input = input("Enter your choice: ")

    #This checks for the users input and redirects them depending on their input
    if user_input == "q":
        print("Goodbye")
        break
    elif user_input == "1":
        add_num1 = input("Please enter Your first number: ")
        add_num1_float = float(add_num1)
        add_num2 = input("Please enter your second number: ")
        add_num2_float = float(add_num2)
        addition(add_num1_float, add_num2_float)
        break
    elif user_input == "2":
        sub_num1 = input("Please enter Your first number: ")
        sub_num1_float = float(sub_num1)
        sub_num2 = input("Please enter Your second number: ")
        sub_num2_float = float(sub_num2)
        subtraction(sub_num1_float, sub_num2_float)
        break
    else:
        print ("\nTry again!\n")