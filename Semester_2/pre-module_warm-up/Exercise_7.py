"""
Pre-module warm-up exercise 7

Scenario:
A function that calculates VAT is mixed with user input and printing.

Task:
Refactor this into a pure function.

Requirements:
# Create a function named get_vat(price: float) -> float.
# The function must:
# Accept a price as an argument.
# Return the VAT value.
# Do not use input() or print() inside the function.

Add:
# Type hints
# A docstring explaining the function’s purpose

"""

"""
#Before
 
def calculate_vat():
    price = float(input("Enter price: "))
    vat = price * 0.2
    print(f"VAT is {vat}")
"""

#After - completed task as per requirements, with error catching
#Extra - Added reusable function for getting positive float


#Function to get valid input as float
def get_valid_positive_float() -> float:
    """
    Gets a valid positive float input

    Arguments:
        None

    Returns:
        validated float value

    Raises:
        ValueError, EOFError, KeyboardInterrupt
    """
    while True:
        try:
            value = float(input("Input price £:").strip())
            if not value:
                raise ValueError
            elif value < 0:
                raise ValueError
            return value
    
        except(ValueError, EOFError, KeyboardInterrupt):
            return None


#Function to get VAT
def get_vat(price: float) -> float:
    """
    Calculates 20% (VAT) of float input

    Arguments:
        float input for calculation

    Returns:
        calculated 20% of input as float
    """
    try:
        vat: float = price * 0.2
        return vat
    
    except ValueError:
        return None
    

#CLI - interface
while True:
    try:
        price = get_valid_positive_float()
        vat: float = get_vat(price)
        print(f"VAT = {(vat):.2f}")

    except (ValueError, TypeError):
        print("Error, try again")