""""
This file contains the code for week 3 lab excercises,
focusing on for loops, while loops, and GitHub intergration.
"""

#This prints only the even numbers between 0 and 20
#for i in range(0, 20, 2):
 #   print(f"\n {i + 1}")


#This code
costs= [15.00, 12.50, 3.75, 40.25]
total_cost = 0

for cost in costs:
    total_cost = total_cost + cost
    print(f"£{total_cost}")

print (f"Your total cost is £{total_cost: .2f}")