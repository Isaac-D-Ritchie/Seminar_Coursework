"""
Semester 2 - Week 1 Lab extra exercise.

This labs challenge is to create a input validation function that uses defensive coding.

Scenario:
    A system is being developed that will accept prices entered by users.
    A valid price must:
     # Be a number
     # Be greater than 0
     # Not exceed 1000
"""

def validate_price(text: str) -> float:
    