""""
This file contains the code for week 3 lab excercises,
focusing on for loops, while loops, and GitHub intergration.
"""

#Task 1 + 2
#This prints only the even numbers between 0 and 20
#for i in range(0, 20, 2):
#   print(f"\n {i + 1}")

#Task 3
#This code takes a list of costs and adds then displaying the cost as it adds and the total cost.
#costs= [15.00, 12.50, 3.75, 40.25]
#total_cost = 0

#for cost in costs:
#    total_cost = total_cost + cost
#    print(f"£{total_cost: .2f}")

#print (f"Your total cost is £{total_cost: .2f}")


for line in range(5):
    for colum in range(5):
        print("*", end=" ")
    print()