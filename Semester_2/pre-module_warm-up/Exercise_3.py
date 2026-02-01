"""
Pre-module warm-up exercise 3

Scenario:
A division operation may crash if the second number is zero.

Task:
Protect the calculation using exception handling.

Requirements:
# Wrap the division logic in a try...except block.
# Catch a ZeroDivisionError.
"""

# Before
"""
    num1 = 10
    num2 = 0
 
    result = num1 / num2
    print(f"Result is {result}")
"""

# After - Caught error with try/except
# Extra: Changed code into a pure function, added type hints

num1: int = 10
num2: int = 0
 
def divide(num1: int, num2: int) -> float:
    try:
        result: float = num1 / num2
        return(f"Result is {result}")
    except ZeroDivisionError:
        return("Cannot divide by 0")

num1: int = 10
num2: int = 0
print(divide(num1, num2))