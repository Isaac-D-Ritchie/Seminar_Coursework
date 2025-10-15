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

"""
In this next piece of code i will be creating a elif to detemine which age group a erson falls into while concidering any unexpected inputs
"""
#to only allow for a integer input i used a while true statement which creates a infinate loop that can only be broken with a 'break' command
while True:
    GetInteger = input("How old are you?")
    #I have used the try and except command to exclude any error values the user could input
    try:
        age = int(GetInteger)
        #I ahve used an if. elif, and else statement nested within the try command to determine which age bracket the person is in and print an output.
        if age in range(18, 126):
            print ("you're an Adult")
            break
        elif age in range(13, 18):
            print("You're a Teenager")
            break
        elif age in range(1, 13):
            print("You're a Child")
            break
        else:
            print ("I dont believe you, Try again. ")
    #This is what detects any unexpedted inputs from the user and redirects them to retry and input something else
    except ValueError:
        print ("Thats not right, Try again. ")
