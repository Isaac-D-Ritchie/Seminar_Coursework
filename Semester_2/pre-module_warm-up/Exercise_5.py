"""
Pre-module warm-up exercise 4

Scenario:
A fitness app needs a user’s age. The program must handle invalid 
input gracefully.

Task:
Write a loop that repeatedly asks the user for their age until valid
input is provided.

Requirements:
# Use a try...except ValueError block.
# Reject non-numeric input.
# Ensure the age is a positive integer.
# Use a loop so the program keeps asking until input is valid.
"""

#Completed - Implemented error validation for valid age input
#Extra - Changed into a a pure function that can be used for 
#        any validation of int above 0, checking for empty characters.

def validate_age(user_input: str) -> int:
    stripped_input: str = user_input.strip()

    if not stripped_input:
        raise ValueError("No input detected")
    
    try:
        int_value = int(stripped_input)
        if int_value <= 0:
            raise ValueError("Please enter valid age")
        return (f"({int_value}) Age validated")

    except ValueError:
        raise ValueError("Please enter valid age")

while True:
    try:
        age_input = input("Enter age: ")
        print(f"{validate_age(age_input)}\n")

    except ValueError as x:
        print(f"Error: {x}\n")
