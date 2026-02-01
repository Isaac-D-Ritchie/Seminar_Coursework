"""
Pre-module warm-up exercise 4

Scenario:
User data may not always include optional fields such as a department.

Task:
Rewrite the code to safely retrieve the "department" value.

Requirements:
# Use the .get() method.
# Provide "Unknown" as the default value if the key is missing.
"""

# Before

user_data = {"name": "Alice", "role": "Admin"}
 
dept = user_data["department"]
print(f"Department: {dept}")