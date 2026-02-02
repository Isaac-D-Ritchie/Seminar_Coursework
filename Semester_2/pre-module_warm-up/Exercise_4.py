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
"""
user_data: dict[str, str] = {"name": "Alice", "role": "Admin"}

dept = user_data["department"]
print(f"Department: {dept}")
"""

# After - Added .get to find department value and return "Unknown" of no key value
#Extra - Changed script into a pure function

def find_department_value(data: list[str, str]) -> str:
    dept = data.get("Department", "Unknown")
    return (f"Department: {dept}")

user_data: dict[str, str] = {"name": "Alice", "role": "Admin"}
print(find_department_value(user_data))