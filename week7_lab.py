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

gradelist = { #Dataset for csv
    "Alice":[85,90,92],
    "Bob":[78,81,85],
    "Charlie":[95,100,98]
}
#This function creates/writes to a csv using the gradelist 
def write_csv():
    with open("week7_gradebook.csv", "w", newline="") as f:
        writer = csv.writer(f) #This sets a varaible to the csv command to prevent syntax issues
        writer.writerow(["student", "grade 1", "grade 2", "grade 3"])
        for student, grades in gradelist.items():
            writer.writerow([student] + grades)
    return
#Calls function
write_csv()

#Function to read csv file and print the students name and average score
def average_from_gades():
    with open("week7_gradebook.csv", "r") as f:
        reader = csv.reader(f)
        next(reader) #skips the title row
        for row in reader:
            temp_grade_list = {int(c) for c in row[1:]} #creates temporary list of grades for each row
            average_grade = sum(temp_grade_list) / len(temp_grade_list) #calculates the average score from the list
            print(f"{row[0]}: Average grade = {average_grade:.1f}\n")
#Calls function
average_from_gades()


