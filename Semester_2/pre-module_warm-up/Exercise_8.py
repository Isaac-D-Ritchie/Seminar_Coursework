"""
Pre-module warm-up exercise 8

Scenario:
You want to sort scores without changing the original order.

Task:
Define the list: scores = [78, 92, 45, 88]
Create a new list called sorted_scores using sorted().
Print both lists.

Requirements:
# Do not use .sort() on the original list.
"""


#List sorting function - Reuseable
def sort_list(input_list) -> list:
    """
    Sorts a given list using sorted()

    Arguments:
        input_list - given list to sort

    Returns:
        sorted list or none if error occurs
    """
    try:
        sorted_list = sorted(input_list)
        return sorted_list
    
    except TypeError:
        return None
    

#CLI interface
scores: list = [78, 92, 45, "8f8"]
print(f"Unsorted list:{scores}")
sorted_list = sort_list(scores)
if sorted_list == None:
    print("Error")
else:
    print(f"Sorted list:{sorted_list}")