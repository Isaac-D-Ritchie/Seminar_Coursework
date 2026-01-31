"""
Semester 2 - Week 1 Lab extra exercise.

This labs challenge is to create a input validation function that uses defensive coding. (at Level 4)

Scenario:
    A system is being developed that will accept prices entered by users.
    A valid price must:
     # Be a number
     # Be greater than 0
     # Not exceed 1000

Function Requirements:
    # Accept a string entered by a user
    # Convert the value to a float
    # Validate that it is greater than 0 and less than or equal to 1000
    # Return the valid price as a float

Error Handling:
    Invalid Inputs:            Required Message:
    Not a number               "Price must be a number"
    Less than or equal to 0    "Price must be greater than 0"
    Greater than 1000          "Price must not exceed 1000"
    Empty or whitespace        "Price is required"

Constraints:
    # Do not use input() or print() in the function
    # Do not catch Exception
    # Do not return None
    # Use type hints
    # Add a docstring explaining behavior and errors
"""

def validate_price(value: str) -> float:
    """
    Price validation fot input argument

    Argument:
        Value - String input from user

    Returns:
        Validated input - Float between 0 to 1000

    Raises:
        ValueError - For invalid argument input
    """
    striped_value = value.strip()
    if not striped_value:
        raise ValueError("Price is required")
    
    if striped_value.count(".") > 1:
        raise ValueError("Price must be a number")
    
    if striped_value.startswith("-"):
        striped_value = striped_value[1:]
    
    number_check = striped_value.replace(".", "")
    if not number_check.isdigit():
        raise ValueError("Price must be a number")
    
    float_value = float(value)
    if float_value <= 0:
        raise ValueError("Price must be greater than 0")
    elif float_value > 1000:
        raise ValueError("Price must not exceed 1000")
    else:
        return float_value



"""Example use of the function"""
user_input = input("Please enter a price £")

try:
    price = validate_price(user_input)
    print(f"Accepted price: £{price:.2f}")
except ValueError as e:
    print(f"Error: {e}")