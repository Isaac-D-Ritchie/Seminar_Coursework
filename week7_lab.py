"""
Week 7
In this weeks lab i will display my understanding of how to interact with: .txt , .csv , and .jason files.
I will show creating, reading, writing, and ammeding files.
"""

#Exercise 1 - diary entry with .txt

#This function asks for input and cretes a file with that text or overrides the file if it already exists.
def write_new_diary_entry():
    new_entry = input("Write new diary entry.\n")
    with open("week7_diary.txt", "w") as diary:
        diary.write(new_entry + "\n") #prints and "\n" moves to next line.
        return
#Calls function
write_new_diary_entry()

#This function reads the diary file and prints the result
def read_diary():
    with open("week7_diary.txt", "r") as diary:
        return diary.read()
#Calls function
print(read_diary())