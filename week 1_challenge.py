
#Here is where i ask for inputs which will we placed into a askii style display
name = input("What is your name... ")
username = input("Enter a user name... ")
location = input("Enter a location... ")

#here i am creating a variable that holds a list of the infomation the user just entered
BoxLines = (f"Name: {name}", f"Username: {username}", f"Location: {location}")

#This determines the maximum length by temirearily assigning each item on the list in the BoxLines variable and checks for the maximum lenngth to save it as Line max length
#I later add 3 to create a buffer between the longest line in the box and its border
LineMaxLength = 3 + (max(len(BoxLines))

#here i print the edges of the box "* +" and the "-" as many times as the variable LineMaxLength to create the top of the box
print ("*" + "-" * LineMaxLength + "+")
#next i used a for loop to print 
for BoxLines:
    print (f"| {BoxLines.ljust(LineMaxLength)}  |")
print ("+" + "-" * LineMaxLength + "*")
