"""
this pregram covers all the tasks set for week 2 lab seminar sessions
"""
#this asks the user to input the temperature in Celsius and stores it as a float variable since it could be a decimal value
print ("please enter the tempreture in Celsius: to convert it to Fahrenheit")
DegreesC = float(input())

#this converts the DegreesC variable to Fahrenheit using the formula (C * 9/5) + 32 and sets it as the variable DegreesF
DegreesF = (DegreesC * 9/5) + 32

print (f"The temperature in celsius is {DegreesC}°C and in Fahrenheit it is {DegreesF}°F")