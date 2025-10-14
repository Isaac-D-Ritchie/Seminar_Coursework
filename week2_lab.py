"""
this pregram covers all the tasks set for week 2 lab seminar sessions
"""
#this asks the user to input the temperature in Celsius and stores it as a float variable since it could be a decimal value
print ("please enter the tempreture in Celsius: to convert it to Fahrenheit")
DegreesC = float(input())

#this converts the DegreesC variable to Fahrenheit using the formula (C * 9/5) + 32 and sets it as the variable DegreesF
DegreesF = (DegreesC * 9/5) + 32

#this print statement prints both variables in a 'simplified' f-string format
print (f"The temperature in celsius is {DegreesC}°C and in Fahrenheit it is {DegreesF}°F")

""""
here is the DegreesC is converted it takes the original value and converts it to Fahrenheit using the formula given. As degreesC is a float variable it can take decimal values and the result of the conversion will also be a float value. goes up so does DegreesF
"""