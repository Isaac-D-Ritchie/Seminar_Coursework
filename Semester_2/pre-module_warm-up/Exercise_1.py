"""
Pre-module warm-up exercise 1

Scenario:
You are given a function that correctly calculates a value, 
but incorrectly prints the result instead of returning it.

Task:
Modify the function so that it returns the calculated value instead of printing it.

Requirements:
Change only one word inside the function.
Do not add new variables or additional print statements
"""

#Before
"""
    def double_number(value):
        result = value * 2
        print(result)
 
    my_num = double_number(10)
    print(f"The number is {my_num}")
"""

#After - print statement replaced with return

def double_number(value: str) -> int:
    """
    Function that doubles input value

    Argument:
        value: number input
    Returns
        result: doubled numbers
    """
    result: int = value * 2
    return(result)
 
my_num = double_number(10)
print(f"The number is {my_num}")