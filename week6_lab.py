"""
In week 6 lab, i will be revising topics from weeks 1-5 aswell as some new concepts like dictionarys, and managing lists.
I will also be revising for the 'Test 2' 
"""
#Test 2 prep exercises
#Prep Exercise 1 - Fix broken code
player_health = 100

#I have fixed this code by avoiding the use of a glabal variable inside the function and adding a function parameter for the current player health.
def take_damage(health): 
    new_health = health - 20 #sets a local varaible as the new health
    print(f"Player took 20 damage!")
    return new_health #Returns the new health value

# Function is called, but the new value is never returned or assigned
player_health = take_damage(player_health)
print(f"Player health is: {player_health}")
