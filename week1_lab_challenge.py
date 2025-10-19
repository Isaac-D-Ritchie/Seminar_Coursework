
#Here is where i ask for inputs which will we placed into a askii style display
name = input("What is your name... ")
username = input("Enter a user name... ")
location = input("Enter a location... ")

#here i am creating a variable that holds a list of the infomation the user just entered
BoxLines = (f"Name: {name}", f"Username: {username}", f"Location: {location}")

#This determines the maximum length by temirearily assigning each item on the list in the BoxLines variable and checks for the maximum lenngth to save it as Line max length
#I later add 5 to create a buffer between the longest line in the box and its border
LineMaxLength = 5 + (max(len(Lines) for Lines in BoxLines))

#here i print the edges of the box "* +" and the "-" as many times as the variable LineMaxLength to create the top of the box
print ("*" + "-" * LineMaxLength + "+")
#next i used a for loop to print each line in the Boxlines i ajusted it to the left using .ljust by the amount of the max length. i later put - 2 to the border didnt quite line up while the longest text detection still needed leeway incase someones name was the longest input and the other inputs were short the box alignment could be incorrect so the adition of 5 ariginally negates this
for Lines in BoxLines:
    print (f"| {Lines.ljust(LineMaxLength - 2)} |")
#this prints the bottom of the box display
print ("*" + "-" * LineMaxLength + "+")