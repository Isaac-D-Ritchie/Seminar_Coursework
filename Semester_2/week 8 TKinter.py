"""
Isaac Ritchie

Week 8 - Graphical User Interfaces with Python tkinter

1.1 Your First tkinter Window
1.2 Labels and Text Display
1.3 Buttons and Event Handling
1.4 Entry Widgets and User Input
1.5 Layout Managers: pack, grid, place
1.6 Checkbuttons, Radiobuttons and Variables
1.7 Listbox and Scrollbar
1.8 Menus and Message Boxes
1.9 Frames and Organizing Your Interface
1.10 Building a Complete Application: Student Record Manager
"""


""" Imports """
import tkinter as tk


""" 1.1 First tkinter window """

# Creates root window and names it
root = tk.Tk()
root.title("First TKinter window")

# Sets window size and stops resizing
root.geometry("400x300")
root.resizable(False,False)

# Sets background colour
root.configure(bg="#f0f0f0")

# Window loop
root.mainloop()
