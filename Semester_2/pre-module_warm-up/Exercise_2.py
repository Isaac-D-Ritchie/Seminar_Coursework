"""
Pre-module warm-up exercise 2

Scenario:
A function formats user information, but it does not specify
input or return types.

Task:
Rewrite the function signature to include correct type hints.

Requirements:
# name must be a string.
# age must be an integer.
# The function must declare that it returns a string.
"""

# Before
"""
    def format_user(name, age):
        return f"User {name} is {age} years old."
"""

# After - Added type hints throughout the script

def format_user(name: str, age: int) -> str:
    return f"User {name} is {age} years old."

input_name: str = "Isaac"
input_age: int = 21
print(format_user(input_name, input_age))