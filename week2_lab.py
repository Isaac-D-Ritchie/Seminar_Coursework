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

int1 = 10
str1 = "hello"
float1 = 5.587
bool1 = True

#this prints out the variable type using the type() function, then adds a brief description of why that type was used. it then created a enpty line to seperete each print statement
print (type (int1), f"-For integer i have assigned the number {int1}, this is becasue integers can only be whole number + or -.")
print ('')
print (type (str1), f"-For string i have assigned the word {str1}, this is because strings can be any combination of letters, numbers or symbols.")
print ('')
print (type (float1), f"-For float i have assigned the number {float1}, this is because floats can be any number with a decimal point as long as needed.")
print ('')
print (type (bool1), f"-For boolean i have assigned the value {bool1}, A boolean variable can only be True or False.")
print ('')

#this piece of code converts the iterger 5 into a float variable.
float(int1)
int1 = float(int1)
print (type(int1), "I have converted the integer variable to a float and display it before the text. I converted it by using 'print (type(int1))' and then 'int1 = float(int1)' ")
#python can do this while other languages such as java cannot. This is beause python is a dynamic language meaning it calculates variables as it is compiled rather than when it is written like in java.
print ('')

"""
string formatting
"""
name = "Isaac"
course = "robotics and ai"
faverouite_programming_language = "python"

#here i used a function to to create a custom welcome messege
print (f"Hello! {name} who is doing {course} and they're favaruite programming languge is {faverouite_programming_language}")
print ('')

#here i am using a placeholder to assign non existant variables into a string text. I then assigned the variables a value after using .funtion and a varaible value list
txt1 = ("your balance is {0:.2f}, and your savings are {1:.2f} ")
print (txt1.format(500, 10))

#here i used my knowledge of print alignment to create a askii image. using alignment
print ("`._______________________________________________,___.") #this is not spaced as it does not need aligning
askiiline2 = "\_-----------------------------------------\_-||--'"
print (f"{askiiline2:>53}") #this prints the second line with a 53 space seperation from the start of the text to the end of it creating a 2 sapce gap at the beginning since its 51 charcters long
print ('') #this prints a blank line