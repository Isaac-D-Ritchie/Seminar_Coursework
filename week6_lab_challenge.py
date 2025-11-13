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
        if module_code in module_id:
            module_prerequisites_set = set(module_id.get(module_code)[1:])
            student_modules_set = set(student_database.get(student_id)[1:])
            student_eligable = True

            for module_required in module_prerequisites_set:
                if module_required in student_modules_set:
                    print(f"module {module_required} achived")
                else:
                    print(f"moule {module_required} not achived")
                    student_eligable = False
            if student_eligable is True:
                return True
            else:
                return False
        else:
            print("Module code not found.")
            return False

    else:
        print("Student not found.")
        return False



#Module ID Dictionary prerequisites
module_id = {"CIS1702" : ["Programming 1"], "CIS1000" : ["Data Structures", "CIS1702"],
           "CIS1001" : ["Web Development", "CIS1702"], "CIS2000" : ["Advanced Mathmatics", "CIS1000", "CIS1702"],
           "MTH1001" : ["Discrete Maths"], "CIS2005" : ["AI Fundamentals", "CIS1000", "CIS1001"]}

#Students Dixtionary (IDs indexed with names and modules)
student_database = {"s12345" : ["Alice", "CIS1702", "MTH1001"],
                    "s67890" : ["Bob", "CIS1702", "CIS1001"],
                    "s54321" : ["Charlie", "MTH1001"]}


#Testing
student_eligabliity = can_enrol("s12345", "CIS2000")
print(f"Student eligability, {student_eligabliity}")
