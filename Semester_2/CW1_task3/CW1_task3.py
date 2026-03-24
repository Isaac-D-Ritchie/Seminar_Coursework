"""
Isaac Ritchie

CW1 - Task 3
Creating a GUI / HCL To-Do list application using tkinter
"""

""" Imports """
import tkinter as tk
from tkinter import messagebox

""" Program """
def to_de_list():

    #Callback functions
    def add_task():
        task = entry.get().strip()
        if not task:
            status_var.set("Error: No task entered")
            status_label.config(bg="red")
            return
        
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
        status_var.set(f"'{task}' Successfully Added")
        status_label.config(bg="Green")


    def remove_task():
        selection = listbox.curselection()

        if not selection:
            status_var.set("Error: No task selected")
            status_label.config(bg="red")
            return
        
        if not messagebox.askyesno("Confirm", "Remove Task"):
            return
        
        listbox.delete(selection[0])
        status_var.set("Task Successfully Removed")
        status_label.config(bg="Green")


    def complete_task():
        selection = listbox.curselection()

        if not selection:
            status_var.set("Error: No task selected")
            status_label.config(bg="red")
            return
        
        idx = selection[0]
        task_text = listbox.get(idx)
        
        if "[Completed]" in task_text:
            status_var.set("Error: Task already completed")
            status_label.config(bg="red")
            return
        
        if not messagebox.askyesno("Confirm", "Complete Task"):
            return
        
        listbox.delete(idx)
        listbox.insert(idx, task_text + " [Completed]")
        status_var.set(f"'{task_text}' Successfully Completed")
        status_label.config(bg="Green")


    def quit():
        confirm = messagebox.askyesno("Confirm", "Quit Application?")
        if confirm:
            root.destroy()
        else:
            return

    #Window
    root = tk.Tk()
    root.title("To-Do List Application")
    root.geometry("420x450")
    root.config(bg="white")

    #Main Label
    tk.Label(root, text=("Enter a task then click 'Add'"), bg="#919191",
             font=("Arial", 16, "bold")).pack(fill=tk.X)

    #Entry
    entry_frame = tk.Frame(root)
    entry_frame.pack(pady=5, fill=tk.X)

    tk.Label(entry_frame, text="Task entry:",font=("Arial", 12)).pack(
        side=tk.LEFT, padx=3)
    entry = tk.Entry(entry_frame, width=20, relief="solid",
                    font=("Arial", 12))
    entry.pack(padx=3, fill=tk.X)
    entry.bind("<Return>", lambda e: add_task())

    #Buttons
    btn_frame = tk.Frame(root)
    btn_frame.pack(pady=5)

    add_btn = tk.Button(btn_frame, text="Add", #Add
                        font=("Arial", 8), command=add_task)
    add_btn.pack(side=tk.LEFT, padx=3)

    remove_btn = tk.Button(btn_frame, text="Remove", #Remove
                           font=("Arial", 8), command=remove_task)
    remove_btn.pack(side=tk.LEFT, padx=3)

    complete_btn = tk.Button(btn_frame, text="Complete", #Complete
                             font=("Arial", 8), command=complete_task)
    complete_btn.pack(side=tk.LEFT, padx=3)

    quit_btn = tk.Button(btn_frame, text="Quit", #Quit
                         font=("Arial", 8),command=quit)
    quit_btn.pack(side=tk.LEFT, padx=3)

    #Listbox 
    list_frame = tk.Frame(root)
    list_frame.pack(pady=5, padx=6, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(list_frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    listbox = tk.Listbox(list_frame, yscrollcommand=scrollbar.set, 
                         selectmode=tk.SINGLE, activestyle="none")
    listbox.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
    scrollbar.config(command=listbox.yview)

    #Status Bar
    status_var = tk.StringVar(value="Ready")
    status_label = tk.Label(root, textvariable=status_var,
                            relief="sunken", fg="white")
    status_label.pack(side=tk.BOTTOM, fill=tk.X)
    status_label.config(bg="green")

    #Mainloop
    root.mainloop()

#Runs code when file run directly
if __name__ == "__main__":
    print("Program Started")
    to_de_list()
    print("Program Ended")