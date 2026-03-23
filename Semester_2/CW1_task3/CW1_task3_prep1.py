"""
This is a preparation for my programming 2 - Coursework 1 Task 3 coding exam.

Task 3 includes creating a GUI / HCI application using the python module
tkinter and the functions included with it.

Preparation task:
    Build a simple To-Do List GUI in tkinter (Add, View, Delete, Mark Complete)
    - Create wireframe BEFORE coding
    - At least 4 links to Nelsons heuristics
    - 150 to 200 word explanation for how my design addresses HCI
"""

#Wireframe for application
"""
This application will be a 420 by 350 pixel resizable window.
The application will be titled "To-Do List Application".
There will be a label at the top with a user entry box below.
Under the entry box there will be 4 buttons: Add task, Task complete, 
Delete task and exit.
Below that will be the to do list where the user can select the task,
while also having a right side scrollbar.

#Additional?
options menu tab for info or exit button
"""


""" Imports """
import tkinter as tk
from tkinter import messagebox

""" Program """
#Functions
def add_task():
    task = entry.get().strip()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
        status_var.set(f"'{task}' Successfully added to list")
        status_label.config(bg="green")
    else:
        status_var.set(f"Error: No entry selected")
        status_label.config(bg="red")

def task_complete():
    selection = listbox.curselection()
    if not selection:
        status_var.set(f"Error: No entry selected")
        status_label.config(bg="red")
        return
    
    #Gets index, text and checks if task is already done
    index = selection[0]
    task_text = listbox.get(index)
    if "[Done]" in task_text:
        status_var.set(f"Error: Task already completed")
        status_label.config(bg="red")
        return

    listbox.delete(index)
    listbox.insert(index, task_text + " [Done]")
    status_var.set(f"'{task_text}' Successfully marked '[Done]'")
    status_label.config(bg="orange")

def remove_task():
    selection = listbox.curselection()
    if selection:
        if not messagebox.askyesno("Confirm", "Delete this task?"):
            return
        task = listbox.get(selection[0])
        listbox.delete(selection[0])
        status_var.set(f"Successfully deleted '{task}'")
        status_label.config(bg="green")
    else:
        status_var.set(f"Error: No entry selected")
        status_label.config(bg="red")
        return

def quit():
    result = messagebox.askyesno("Confirm", "Are you sure you want to Quit")
    if result:
        root.destroy()
    else:
        return

#Window
root = tk.Tk()
root.title("To-Do List Application")
root.geometry("420x350")

#title label
tk.Label(root, text="To-Do List", font=("Arial", 16, "bold"), 
         bg="#A7A7A7").pack(pady=5, fill=tk.X)

#Entry frame
entry_frame = tk.Frame(root)
entry_frame.pack(pady=10, fill=tk.X)

#Entry box and label
tk.Label(entry_frame, text="List entry:", font=("Arial", 12)).pack(
    pady=2, side=tk.LEFT)
entry = tk.Entry(entry_frame, font=("Arial", 12), relief="solid")
entry.pack(side=tk.LEFT, fill=tk.X, expand=True, pady=5, padx=5)
entry.bind("<Return>", lambda e: add_task()) #Enter detection to add task

#Button frame and buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=5)

add_btn = tk.Button(btn_frame, text="Add Task", font=("Arial", 10), 
                    command=add_task) #Add button
add_btn.pack(side=tk.LEFT, padx=5)

complete_btn = tk.Button(btn_frame, text="Completed Task", font=("Arial", 10),
                         command=task_complete) #Complete task button
complete_btn.pack(side=tk.LEFT, padx=5)

remove_btn = tk.Button(btn_frame, text="Remove Task", font=("Arial", 10),
                       command=remove_task) #Remove task button
remove_btn.pack(side=tk.LEFT, padx=5)

quit_btn = tk.Button(btn_frame, text="Quit", font=("Arial", 10), command=quit)
quit_btn.pack(side=tk.LEFT, padx=5) #Quit program button

#Listbox with scrollbar and frame
list_frame = tk.Frame(root)
list_frame.pack(pady=5, padx=5, fill=tk.BOTH)

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(list_frame, font=("Arial", 11), selectmode=tk.SINGLE,
                     yscrollcommand=scrollbar.set, activestyle="none")
listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.config(command=listbox.yview)

#Status bar
status_var = tk.StringVar(value="Ready")
status_label = tk.Label(root, textvariable=status_var, font=("Arial", 8),
                        bg="green", relief="sunken", fg="white")
status_label.pack(fill=tk.X, side=tk.BOTTOM)

#Mainloop
root.mainloop()

""" Application summery and heuristic table """
#Heuristics
"""
1 - Heuristic: Visibility of the system - Always keeps the user informed
    Application status telling the user info about the program and actions.

2 - Heuristic: constancy - each button is centred and has a padx of 5 and the same font.
    Buttons and widgets are clearly labeled, organized and coloured for the user.

3 - Heuristic: User control and freedom - Done through messagebox commands.
    The user is prompted to confirm weather to delete a task or quit the application.

4 - Heuristic: Help recognize errors - This is done by text and visually through colour.
    The program handles errors and informs the user about them in the status bar.
"""
#How my design addresses HCL
"""
My to-do list application address HCl by having a clear window title, adapting to the user 
resizing by keeping buttons centred and allowing for frame stretching.
The list of tasks has a scrollable bar to allow the user to have long task lists and maintain
program usability.
The status bar gives clear indication about the application status, informing the user of any errors,
and if an action was successful or not with a changing bar colour for added indication checking.
Overall, I prioritized simplicity with nelsons heuristics in mind.
"""