#For the porposes of this preparation i have genrated a question via chatgpt.com whihc covers the perameters of Test 1.

#write a Python program that:
# 1) Start with a comment decribing the program.
# 2) Asks the user to enter their name and age.
# 3) Stores age as both an int and a float.
# 4) Uses string oporator + to print a greeting with their name.
# 5) Use the arithmatic oporator % to check if their age is an even or odd number. 
# 6) Use if/elif/else to:
#   * Print "You are a teenager" if their age is between 13 and 19.
#   * Print "You are an adult" if 20 or older.
#   * Otherwise, print "You are a a child".
# 7) Use the logical oporator (and) to check if their age is between 30 and 39 (inclusive) and print "You are in your 30s!" if true.
# 8) Write a function called countdown(age) that uses a for loop with range() to pint numbers from the users age down to 1 Call it the user age.
# 9) Call that function with the user age (integer)



#In this program i will be asking for the users name and age. Then it will welcome them displaying their name and outputting if they are a teenager, child, or adult. 
#I will output if they are in their 30s and then a countdown beginning at their age down to 1.

#here i am asking the user to input their name and age then save them and covert their age to a int and a float.
name = input("What if your name? ")
age_input = input("What is your age? ")

age_integr = int(age_input)
aga_float = float(age_input)

#here i am using + to connect strings in a printed sentence
print ("Hello, " + name + " Your age is, " + age_input)

#This code prints if their age is odd o even
odd_number_checker = age_integr % 2
if odd_number_checker == 0:
    print("Your age is an even number")
else:
     print("Your age is an odd number")

#This code prints what age bracket they are in
if (age_integr >= 20):
     print("you are a Adult")
elif (age_integr >= 13): 
     print("You are a Teenager")
else:
     print("You are a child")

#This code outputs if they are in their 30s
if age_integr >= 30 and age_integr <= 39:
     print("You are in your 30s")

     
def countdown(age):
     for countdown in range(1, age + 1):
        print(countdown)

print(countdown(age_integr))
