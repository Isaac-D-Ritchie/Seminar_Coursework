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

"""
This further program utilises each different data type and their functions
"""

int = 10
str = "hello"
float = 5.587
bool = True

#this prints out the variable type using the type() function, then adds a brief description of why that type was used
print (type (int), f"For integer i have assigned the number {int}, this is becasue integers can only be whole number + or -.")
print (type (str), f"For string i have assigned the word {str}, this is because strings can be any combination of letters, numbers or symbols.")
print (type (str), f"For float i have assigned the number {float}, this is because floats can be any number with a decimal point as long as needed.")
print (type (bool), f"For boolean i have assigned the value {bool}, A boolean variable can only be True or False.")