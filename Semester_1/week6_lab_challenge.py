"""
Week 6 Lab Challenge - The Enrolment Validator

Scenario:
You are building a mini-system for a university to validate module enrolments. 
Your system needs to store data on all students and all modules, and most importantly, 
it must check if a student has the correct prerequisites before they are allowed to enrol on an advanced module.

"""
#Functions:

#Enrolemt check
def can_enrol(student_id, module_code):
    if student_id in student_database:
        if module_code in student_database[student_id]:
            print(f"Student already enrolled in {module_code}")
            return False
        elif module_code in module_id:
            module_prerequisites_set = set(module_id.get(module_code)[1:])
            student_modules_set = set(student_database.get(student_id)[1:])
            student_eligable = True

            for module_required in module_prerequisites_set:
                if module_required in student_modules_set:
                    print(f"Prerequisite module {module_required} achived")
                    return True
                else:
                    print(f"Prerequisite module {module_required} not achived")
                    return False
        else:
            print("Module code not found.")
            return False

    else:
        print("Student not found.")
        return False

#Enroll student after data input
def enrol_student(student_id, module_code):
        if can_enrol(student_id, module_code) == True:
            student_database[student_id].append(module_code)
            print(f"Student sucsesfully enrolled in {module_code}")
            print(f"\n{student_database.get(student_id)}\n")
            return True
        else:
            print("Enrolment unsucsesful, Try again...")
            return False
            
#function while loop for enrolling student
def student_enroll_try():
    while True:
        student_id_input = input("Input a student ID...")
        module_request_input = input("Input module for student enrolment...\n")
        if enrol_student(student_id_input, module_request_input) == True:
            if input("Press enter to continue or 'q' to end search.") == "q":
                break
            else:
                continue
        else:
            continue

#Module ID Dictionary prerequisites
module_id = {"CIS1702" : ["Programming 1"], "CIS1000" : ["Data Structures", "CIS1702"],
           "CIS1001" : ["Web Development", "CIS1702"], "CIS2000" : ["Advanced Mathmatics", "CIS1000", "CIS1702"],
           "MTH1001" : ["Discrete Maths"], "CIS2005" : ["AI Fundamentals", "CIS1000", "CIS1001"]}

#Students Dixtionary (IDs indexed with names and modules)
student_database = {"s12345" : ["Alice", "CIS1702", "MTH1001"],
                    "s67890" : ["Bob", "CIS1702", "CIS1001"],
                    "s54321" : ["Charlie", "MTH1001"]}

#Menu for using the database
while True:
    menu_input = input("DATABASE MENU\nSelect from the following options:\nEnrol Student: e\nDisplay modules: m\nDisplay Student Info: s \nQuit Menu: q\n ")
    if menu_input == "e":
        student_enroll_try()
    elif menu_input == "m":
        for modules in module_id:
            print(f"Module name: {module_id.get(modules)[:1]}\nModule requirements:{module_id.get(modules)[1:]}\n")
            continue
    elif menu_input == "s":
        for students in student_database:
            print(f"Student name: {student_database.get(students)[:1]}\nModules achived: {student_database.get(students)[1:]}\n")
    elif menu_input == "q":
        break