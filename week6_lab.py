"""
In week 6 lab, i will be revising topics from weeks 1-5 aswell as some new concepts like dictionarys, and managing lists.
I will also be revising for the 'Test 2' 
"""
#Test 2 prep exercises
#Prep Exercise 1 - Fix broken code
player_health = 100

def take_damage():
    # This 'player_health' is LOCAL, not the global one
    player_health = 90
    print("Player took damage!")
    #Missing return statement

# Function is called, but the new value is never returned or assigned
take_damage()

print(f"Player health is: {player_health}")
# Expected Output: Player health is: 80
# Actual Output: Player health is: 100
