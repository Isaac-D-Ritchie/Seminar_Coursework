#CW1 - In-class Test 2
# *For the porposes of this exam prep i have generated a question from chatgpt.com to cover the parameters of the topics taught in 3-5.*

#Write a Python program that:

#1. Define a function called find_factors(n) that:
#    Uses a for loop and range() to find all numbers between 1 and n that evenly divide n.
#    Stores them in a list and returns that list.

#2. Defines another function called sum_factors(factors) that:
#    Takes the list of factors as a parameter.
#    Uses a while loop to calculate and return the total sum of the factors.

#3. Inside your main program (outside the functions):
#    Ask the user for an integer.
#    Call both functions and print the list of factors and their sum.
#    Use an assert statement to verify that the sum is greater than or equal to the largest factor.
#    Include a comment explaining why the assertion should always be true.

#4. Add a global variable called calculation_count that keeps track of how many times find_factors() has been called.
#    Update it inside the function using the global keyword.
#    After all calculations, print how many times the function has run.


"""
In this code i will be using functions to find the factors of a integer inputed by the user. 
I will also use an assert statement to varify that the sum is greater or equal to the largest factor.
Finally, i will keep count of hoe many times the find factor function is called.
"""

#Function checks what numbers between 1 and the 'n' even devide into using % and checking if the returned value is 0, then adding the value to a list 'factors'.
def find_factors(n):
    global calculation_count
    calculation_count += 1
    for i in range(1, n+1):
        if n % i == 0:
            factors.append(i)
        else:
            continue

#This function calculates the sum of factors.
def sum_factors(factors):
    total = 0
    length = 0
    while length < len(factors):
        total += factors[length]
        length += 1
    return total

#Cretes an empty list to add factors to assign the vales to later.
factors = []
#Creates a glabal variable which i will use to track the ammount of find_function() called.
calculation_count = 0

#I have decided to place the main code in a while loop to keep asking for perameters to make the calculation_count functinal and not end the program after each calcualtion which resets the count to 1 when restarted.
while True:
    #Calls the function and prints the resulting list then adds the lust and prints the value.
    find_factors(int(input("Plese enter a intger to calculate its factors:")))

    #This checks the sum of factors is atleast the vale of its largest factor, this porves that the calculations are accurate since the factors include at least 1 and the number itself.
    assert sum_factors(factors) >= max(factors)
    print("All checks passed")

    #I have used f strings to improves how the information is displayed.
    print (f"Factors: {factors}")
    print (f"The sum of factors = {sum_factors(factors)}")

    #Prints the ammount of times find_factors has been called
    print(f"The ammount of claculations made are {calculation_count}")

    #I have added this code block to ask if the user wants to end the prgram after each calculation, so it does not repeat forever.
    repeat = input("Calculate again? 'yes' or 'no'")
    if repeat == "yes":
        continue
    elif repeat == "no":
        break  
    else:
        #If the input is invalid the program automatical stops.
        print("invalid input, stoping program.")
        break
