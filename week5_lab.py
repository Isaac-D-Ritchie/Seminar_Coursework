"""
In week 5 i will be showing that i can condense WET code into DRY code aswell as learn the functions of the built-in VS code debugger
"""
#Exercise 1
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
#now FIXED code block
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


#Exercise 3
#Creating a flowchard and pseudocode for a simple task
"""
Pseudocode Task
 start
    num = 50
    FUNCTION guess_number(num)
        IF num > 50:
            PRINT "The number is lower then that guess"
        ELSE IF num < 50:
            PRINT "
        ELSE IF num == 50
            PRINT "Thats Right! the number is 50"
    END FUNCTION
 END

    
Flowchart for devide errors

      (Start)
        |
        v
/Enter numbers A,B/  <------------------
        |                               |
        v                               |
        /\                              |
<Does A or B == 0>  --YES-- / PRINT "Error! 0 cannot be devided" /
        \/  
        |
        | NO
        v
  [result = A / B]
        |
        v
   /PRINT result/
        |
        v
      (End)

"""

#Exercise 4
#Pseudocode and Flowchard challenge
#Create a plan to add items to a list unless the list is full (10 items)
"""
Pseudocode

START
input = new_item
 FUNCTION list_add(new_item)
    IF list length =< 9:
        RETURN list APPEND new_item
    ELSE IF list length == 10:
        PRINT "List is full"
        RETURN None
 END FUNCTION
END

Flowchart
   (Start)
      | <---------------------------
      v                             |
/INPUT new_item/                    |
      |                             |
      v                             |
      /\                            |
<list length == 10> --YES-- [PRINT "List is full"]
      \/
[list APPEND new_item]
      |
    (End)
"""
