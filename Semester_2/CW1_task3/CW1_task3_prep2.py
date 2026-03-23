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

#Attempt 2 of task 3 prep

""" imports """
import tkinter as tk
from tkinter import messagebox

""" Program """
def to_do_list():

    #Functions

    def add_task():
        task = entry.get().strip()
        if task:
            list.insert(tk.END, task)
            entry.delete(0, tk.END)
            status_var.set(f"{task} Added successfully")
            status_label.config(bg="green")
        else:
            status_var.set("Error: No task selected")
            status_label.config(bg="red")

    def remove_task():
        selection = list.curselection()
        if not selection:
            status_var.set("Error: No task selected")
            status_label.config(bg="red")
            return
        
        if not messagebox.askyesno("confirmation", "Are you sure?"):
            return

        task = list.get(selection[0])
        list.delete(selection[0])
        status_var.set(f"{task} Removed successfully")
        status_label.config(bg="green")

    def complete_task():
        selection = list.curselection()
        if not selection:
            status_var.set("Error: No task selected")
            status_label.config(bg="red")
            return
        
        idx = selection[0]
        task = list.get(idx)

        if "[Done]" in task:
            status_var.set("Error: Task already completed")
            status_label.config(bg="red")
            return
        
        list.delete(idx)
        list.insert(idx, task + " [Done]")
        status_var.set(f" {task} Task Completed")
        status_label.config(bg="green")
        return


    def quit():
        if messagebox.askyesno("confirmation", "Quit application"):
            root.destroy()
        else:
            return


    #Window
    root = tk.Tk()
    root.title("To-Do List Application")
    root.geometry("420x400")

    #Name Label
    tk.Label(root, text=("To-Do List"), font=("Arial", 16, "bold"), 
            bg="#D4A5A5", fg="black").pack(pady=5,fill=tk.X)

    #Entry
    entry_frame = tk.Frame(root)
    entry_frame.pack(pady=5)

    tk.Label(entry_frame, text="Task Entry:", font=("Arial", 10)).pack(side=tk.LEFT)
    entry = tk.StringVar()
    entry= tk.Entry(entry_frame, width=20, relief="solid")
    entry.pack(padx=5, side=tk.LEFT)
    entry.bind("<Return>", lambda e: add_task())

    #Buttons
    btn_frame = tk.Frame(root)
    btn_frame.pack(padx=5)

    add_btn = tk.Button(btn_frame, text=("Add"), font=("Arial", 8), command=add_task)
    add_btn.pack(padx=3,side=tk.LEFT)
    remove_btn = tk.Button(btn_frame, text=("Remove"), font=("Arial", 8), command=remove_task)
    remove_btn.pack(padx=3,side=tk.LEFT)
    complete_btn = tk.Button(btn_frame, text=("Complete"), font=("Arial", 8), command=complete_task)
    complete_btn.pack(padx=3,side=tk.LEFT)
    quit_btn = tk.Button(btn_frame, text=("Quit"), font=("Arial", 8), command=quit)
    quit_btn.pack(padx=3,side=tk.LEFT)

    #Listbox and scrollbar
    list_frame = tk.Frame(root)
    list_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(list_frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    list = tk.Listbox(list_frame, font=("Arial", 10), selectmode=tk.SINGLE,
                      activestyle="none", yscrollcommand=scrollbar.set)
    list.pack(padx=5, side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.config(command=list.yview)

    #Status bar
    status_var = tk.StringVar(value="Ready")
    status_label = tk.Label(root, textvariable=status_var, font=("Arial", 10), 
                            relief="sunken")
    status_label.pack(side=tk.BOTTOM, fill=tk.X)
    status_label.config(bg="green")

    #Main loop for GUI
    root.mainloop()

if __name__ == "__main__":
    to_do_list()