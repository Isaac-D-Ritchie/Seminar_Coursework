from __future__ import annotations
"""Import allows for type hints to be stored as strings"""

"""
Semester 2 - Week 1 Lab

This labs challenge is to refactor a messy script into a structured application.


# Unedited messy_script:

data = input("Enter comma-separated numbers: ")
nums = data.split(",")

total = 0
for n in nums:
    total += float(n)

print("count:", len(nums))
print("sum:", total)
print("avg:", total / len(nums))


# Process of refactoring
1. Separated code into functions
2. Input validation/error handling

"""

"""My version"""

def parse_data(data: str) -> list[float]:
    """
    Parses comma separated into a list of floats

    Arguments:
        string of numbers e.g. 1,2,3,4...

    Returns:
        Parsed list of the comma separated numbers (floats)
    
    Raises:
        ValueError: For invalid input / No numbers
    """  
    raw_numbers = [t.strip() for t in data.split(",")]
    numbers = [t for t in raw_numbers if t != ""]
    
    if not numbers:
        raise ValueError("No numbers provided")
    
    Values: list[float] = []
    for t in numbers:
        try:
            Values.append(float(t))
        except ValueError as x:
            raise ValueError(f": Invalid number {t!r}") from x
        
    return Values


def data_summary(Values: list[float]) -> dict[str, float]:
    """
    Calculate data points of values: sum, average, and count.

    Arguments:
        Values: Non-empty list of float number tokens

    Returns:
        Dictionary with keys: sum, avg, count

    Rises:
        ValueError: If values list is empty
    """
    if not Values:
        raise ValueError("No values provided")
    
    summary = sum(Values)
    count = float(len(Values))
    avg = summary / count

    return {"count": count, "sum": summary, "avg": avg}


def format_summary(data: dict[str, float]) -> str:
    """
    Formats data for CLI

    Arguments:
        Dictionary list of number data

    Returns:
        String of data to display on CLI
    """
    return (
        f"count: {int(data['count'])}\n"
        f"sum: {data['sum']:.3f}\n"
        f"avg: {data['avg']:.3f}"
        )


"""
Runs script in CLI.
"""
def main() -> None:
    try:
        user_input = input("Enter comma-separated numbers: ")
        data = parse_data(user_input)
        data_sum = data_summary(data)
        print(format_summary(data_sum))
    except ValueError as x:
        print(f"Error {x}")


#Entry Safeguard
if __name__ == "__main__":
    main()