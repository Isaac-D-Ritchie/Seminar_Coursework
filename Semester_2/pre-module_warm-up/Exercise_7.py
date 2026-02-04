"""
Pre-module warm-up exercise 6

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
#A docstring explaining the function’s purpose

"""
#Before
 
def calculate_vat():
    price = float(input("Enter price: "))
    vat = price * 0.2
    print(f"VAT is {vat}")