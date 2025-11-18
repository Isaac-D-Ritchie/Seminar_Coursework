"""
Week 7
In this weeks lab i will display my understanding of how to interact with: .txt , .csv , and .jason files.
I will show creating, reading, writing, and ammeding files.
"""

#Exercise 1 - diary entry with .txt

#This function asks for input and cretes a file with that text or overrides the file if it already exists.
def write_new_diary_entry():
    new_entry = input("Write new diary entry.\n")
    with open("week7_diary.txt", "a") as diary:
        diary.write(new_entry + "\n") #prints and "\n" moves to next line.
        return
#Calls function
#write_new_diary_entry()

#This function reads the diary file and prints the result
def read_diary():
    with open("week7_diary.txt", "r") as diary:
        return diary.read()
#Calls function
#print("\n" + read_diary())

#Exercise 2 - Working with CSV
import csv

gradelist = {
    "Alice":[85,90,92],
    "Bob":[78,81,85],
    "Charlie":[95,100,98]
}
with open("gradebook.csv", "w", newline="") as gradebook:
    writer = csv.writer(gradebook) #This sets a varaible to the csv command to prevent syntax issues
    writer.writerow(["student", "grade 1", "grade 2", "grade 3"])
    for student, grades in gradelist.items():
        writer.writerow([student] + grades)
