"""
In week 5 i will be showing that i can condense WET code into DRY code aswell as learn the functions of the built-in VS code debugger
"""
#Excercise 1
# I have re-written the WET code so that is not DRY code by using three functions.
def start_scene():
    print("You are in a dark forest. You see two paths.")
    choice = input("Do you go 'left' or 'right'? ")
    if choice == 'left':
        left_path_scene()
    elif choice == 'right':
        right_path_scene()

def left_path_scene():
    print("You walk down the left path and find a river.")
    choice2 = input("Do you 'swim' across or 'follow' the river bank? ")
    if choice2 == 'swim':
        print("You are tired from swimming and rest. You win!")
    elif choice2 == 'follow':
        print("You follow the river bank and find a hidden cave. You win!")
    else:
        print("Invalid choice. You are lost.")

def right_path_scene():
    print("You walk down the right path and encounter a sleeping bear.")
    choice2 = input("Do you 'tiptoe' past or 'run' away? ")
    if choice2 == 'tiptoe':
        print("You successfully sneak past the bear. You win!")
    elif choice2 == 'run':
        print("You trip while running and the bear wakes up. You lose.")
    else:
        print("Invalid choice. You are lost.")

start_scene()


#Exercise 2
#BROKEN code block
player_score = 0
def add_points(added_score):
    new_player_score = player_score + added_score
    print(f"[Inside Function] Score is now: {added_score}")
    #This returns the value and sets the player score to it as part of the global variable
    return new_player_score

# --- Main Program ---
print(f"[Outside] Player score is: {player_score}")
player_score = add_points(10)
#This now chnages player score to 10 instead of staying 0
print(f"[Outside] Player score now is is: {player_score}") 

