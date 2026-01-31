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

def validate_price(Value: str) -> float:
    