"""
In week 6 lab, i will be revising topics from weeks 1-5 aswell as some new concepts like dictionarys, and managing lists.
I will also be revising for the 'Test 2' 
"""
#Test 2 prep exercises
#Prep Exercise - Fix broken code
player_health = 100

#I have fixed this code by avoiding the use of a glabal variable inside the function and adding a function parameter for the current player health.
def take_damage(health): 
    new_health = health - 20 #sets a local varaible as the new health
    print(f"Player took 20 damage!")
    return new_health #Returns the new health value

# Function is called, but the new value is never returned or assigned
player_health = take_damage(player_health)
print(f"Player health is: {player_health}")



#lab exercises:
#Exercise 1 - String slicing and .split()
log_data = "SCORE:Player_1:2500"

#Useing the splic command, i will break up the string into 3 parts
parced_data = log_data.split(":")
#I have also used f strings to change the output format
print (f"Player name: {parced_data[1]}")
print (f"Player score: {parced_data[2]}")

#Exercise 2 - create a quiz using two lists

#List of questions and answers saved as a variables.
questions = ["What is 2+2?..","What is that captial of france?..","What keyword defines a function in python?.."]
answers = ["4","paris","def"]
#score variable
score = 0

#For loop to ask quesrions and compare them to the corespndinf answer
for q in range(len(questions)):
    user_answer = input(f"{questions[q]}")
    if user_answer == answers[q]:
        print("correct! +1 score")
        score += 1
        continue
    else:
        print("wrong answer :(")
        continue

#Prints the final score
print(f"Score = {score}")



