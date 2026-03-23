"""
Exercise 1 - Hello GUI

Difficulty: Beginner

Create a GUI application with the following requirements:

    1. A window titled "Hello GUI" with a size of 400x200 pixels.

    2. A Label that displays "Welcome to CIS1703!" in 16pt bold Arial, coloured purple.

    3. An Entry widget where the user can type their name.

    4. A Button labelled "Say Hello" that, when clicked, changes the label text to 
       "Hello, [name]!" using the name from the Entry.

    5. A "Clear" button that resets the label and clears the Entry.
"""

""" Imports """
import tkinter as tk

#Functions
def update_label():
    name = name_entry.get()
    text_var.set(f"Hello, {name}")
    
def clear_label():
    text_var.set("Welcome to CIS1703!")
    name_entry.delete(0, tk.END)

#Window
root = tk.Tk()
root.title("Hello GUI")
root.geometry("400x200")

#Label
text_var = tk.StringVar()
text_var.set("Welcome to CIS1703!")
tk.Label(root, textvariable=text_var, bg="purple",font=("Arial", 16, "bold")).pack(
        pady=10, fill=tk.X)

#Entry frame and widget
entry_frame = tk.Frame(root)
entry_frame.pack(pady=5)
tk.Label(entry_frame, text="Name:").grid(row=1, column=0)
name_entry = tk.Entry(entry_frame, bg="#727171", width=20, font=("Arial", 10))
name_entry.grid(row=1, column=1)

#Button frame and buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=5)

hello_btn = tk.Button(btn_frame, text="Say Hello", command=update_label)
hello_btn.pack(side=tk.LEFT, padx=5)

clear_btn = tk.Button(btn_frame, text="Clear", command=clear_label)
clear_btn.pack(side=tk.LEFT, padx=5)


#Mainloop
root.mainloop()