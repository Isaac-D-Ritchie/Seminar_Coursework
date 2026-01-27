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

"""

#My version

def parse_data():
    data = input("Enter comma-separated numbers: ")
    return data.split(",")

def data_summary(nums):
    total = 0
    for n in nums:
        total += float(n)
    return total

def format_summary(total, nums):
    print("count:", len(nums))
    print("sum:", total)
    print("avg:", total / len(nums))

def main():
    data = parse_data()
    data_sums = data_summary(data)
    format_summary(data_sums, data)

main()