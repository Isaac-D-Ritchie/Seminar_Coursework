"""
Week 6 Lab Challenge - The Enrolment Validator

Scenario:
You are building a mini-system for a university to validate module enrolments. 
Your system needs to store data on all students and all modules, and most importantly, 
it must check if a student has the correct prerequisites before they are allowed to enrol on an advanced module.

"""

#Module ID Dictionary
module_id = {"CIS1702" : "Programming 1", "CIS1000" : "Data Structures",
           "CIS1001" : "Web Development", "CIS2000" : "Advanced Mathmatics",
           "MTH1001" : "Discrete Maths", "CIS2005" : "AI Fundamentals"}

#Students Dixtionary (IDs indexed with names and modules)
student_database = {"s12345" : ["Alice", module_id["CIS1702"],
    module_id["MTH1001"]], "s67890" : ["Bob", module_id["CIS1702"],
    module_id["CIS1001"]], "s54321" : ["Charlie", module_id["MTH1001"]]}

#Test prompts
student_search = input("Enter student ID...")
print(student_database[student_search])
module_search = input("Enter module ID...")
print(module_id[module_search])
