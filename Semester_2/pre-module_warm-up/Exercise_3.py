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

#Before

num1 = 10
num2 = 0
 
result = num1 / num2
print(f"Result is {result}")