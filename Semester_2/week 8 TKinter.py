"""
Isaac Ritchie

Week 8 - Graphical User Interfaces with Python tkinter

exercises have been separated into function which can be called

1 Your First tkinter Window
2 Labels and Text Display
3 Buttons and Event Handling
4 Entry Widgets and User Input
5 Layout Managers: pack, grid, place
6 Checkbuttons, Radiobuttons and Variables
7 Listbox and Scrollbar
8 Menus and Message Boxes
9 Frames and Organizing Your Interface
10 Building a Complete Application: Student Record Manager
"""


""" Imports """
import tkinter as tk


""" 1 First tkinter window """
def first_tkinter_window():
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



""" 2 Labels and Text Display """
def labels_and_text():
    root = tk.Tk()
    root.title("Labels Tutorial")
    root.geometry("450x350")
    root.resizable(False, False)

    #Labels for 1.2
    label1 = tk.Label(root, text="Hello!") #Basic label
    label1.pack(pady=10)

    label2 = tk.Label(root, #Custom label
                      text="Welcome to my first tkinter window!",
                      font=("Arial", 18, "bold"),
                      fg="#000000",
                      bg="#F4F4F4")
    label2.pack(pady=10)

    label3 = tk.Label(root, text="This text is purposely a long paragraph to display " \
                                "control of how text warps to the next line", #Long label
                                wraplength=350,
                                justify="left",
                                font=("Arial", 11))
    label3.pack(pady=10)

    #Label that updates dynamically
    status_text = tk.StringVar()
    status_text.set("Dynamic label")
    status_label = tk.Label(root,
                    textvariable=status_text,
                    font=("Courier", 12),
                    fg="green",
                    relief="sunken",
                    width=30)
    status_label.pack(pady=10)

    #Window loop
    root.mainloop()



""" 3 Buttons and Event Handling """
def btn_tutorial():
    #Functions for 1.3
    def on_greet():
        """Callback function for the Green button."""
        output_label.config(text="Hello, " + name_entry.get() + "!")

    def on_clear():
        """Callback function for Clear button"""
        name_entry.delete(0, tk.END)
        output_label.config(text="")

    def on_exit():
        """Callback function for End button"""
        root.destroy()

    #Window
    root = tk.Tk()
    root.title("Buttons Tutorial")
    root.geometry("400x250")
    root.resizable(False,False)

    #Input selection
    tk.Label(root, text="Enter your name", font=("Arial", 12)).pack(pady=(20,5))
    name_entry = tk.Entry(root, font=("Arial", 12), width=25)
    name_entry.pack(pady=5)

    #Button frames
    btn_frame = tk.Frame(root)
    btn_frame.pack(pady=10)

    #Buttons for 1.3
    green_btn = tk.Button(
        btn_frame,
        text="Green",
        command=on_greet,
        bg="#0D7B5D",
        fg="#037824",
        font=("Arial", 11, "bold"),
        width=10)
    green_btn.pack(side=tk.LEFT, padx=5)

    clear_btn = tk.Button(
        btn_frame,
        text="Clear",
        command=on_clear,
        font=("Arial", 11),
        width=10)
    clear_btn.pack(side=tk.LEFT, padx=5)

    exit_btn = tk.Button(
        btn_frame,
        text="Exit",
        command=on_exit,
        fg="red",
        font=("Arial", 11),
        width=10)
    exit_btn.pack(side=tk.LEFT, padx=5)

    #Output label
    output_label = tk.Label(root, text="", font=("Arial", 14), fg="#5B2C8E")
    output_label.pack(pady=20)

    #Mainloop
    root.mainloop()



""" 4 Entry Widgets and User Input (Calculate BMI)"""
def widget_tutorial():

    #BMI function
    def calculate_bmi():
        """ Calculate BMI from input """
        try:
            #get inputs
            weight = float(weight_entry.get())
            height = float(height_entry.get())
            if height <= 0 or weight <= 0:
                raise ValueError
            bmi = weight / (height ** 2)
            result.set(f"Your BMI is {bmi:.1f}")

            #Change colour based on BMI
            if bmi < 18.5:
                result_label.configure(fg="blue")
            elif bmi < 25:
                result_label.configure(fg="green")
            elif bmi < 30:
                result_label.configure(fg="orange")
            else:
                result_label.configure(fg="red")

        except ValueError:
            result.set("Invalid input, please try again")
            result_label.configure(fg="red")

    #handles placeholder text
    def clear_weight():
        if weight_entry.get() == "e.g. 70":
            weight_entry.delete(0, tk.END)
    
    def clear_height():
        if height_entry.get() == "e.g. 1.25":
            height_entry.delete(0, tk.END)


    #Window
    root = tk.Tk()
    root.title("BMI Calculator")
    root.geometry("350x250")
    root.resizable(False,False)
    root.configure(bg="#84cb6c")

    #Weight Input
    tk.Label(root, text="Weight (KG)", font=("Arial", 11), bg="#000000").pack(pady=(15, 2))
    weight_entry = tk.Entry(root, font=("Arial", 12), width=20, justify="center", fg="#545050")
    weight_entry.insert(0, "e.g. 70")
    weight_entry.pack()
    print(weight_entry)
    weight_entry.bind("<FocusIn>", clear_weight)

    #Height Input
    tk.Label(root, text="Height (m)", font=("Arial", 11), bg="#000000").pack(pady=(25, 2))
    height_entry = tk.Entry(root, font=("Arial", 12), width=20, justify="center", fg="#545050")
    height_entry.insert(0, "e.g. 1.25")
    height_entry.pack()
    height_entry.bind("<FocusIn>", clear_height)

    #Calculate button
    tk.Button(root, text="Calculate BMI", command=calculate_bmi, bg="#507b41", 
              font=("Aial", 12, "bold")).pack(pady=15)
    
    #Result
    result = tk.StringVar()
    result_label = tk.Label(root, textvariable=result, font=("Arial", 13), bg="#424141")
    result_label.pack()

    #Mainloop
    root.mainloop()

""" 5 Layout Managers """
def layout_tutorial():

    #Pack window
    place_root = tk.Tk()
    place_root.title("pack() Demo")
    place_root.geometry("400x300")

    #Widgets stack vertically by default
    tk.Label(place_root, text="Top", bg="lightblue", fg="#000000", width=30).pack(pady=10)
    tk.Label(place_root, text="Middle", bg="lightgreen", fg="#000000", width=30).pack(pady=10)
    tk.Label(place_root, text="Bottom", bg="yellow", fg="#000000" , width=30).pack(pady=10)

    #Using side= to arrange horizontally
    frame = tk.Frame(place_root)
    frame.pack(pady=20)
    tk.Button(frame, text="Left").pack(side=tk.LEFT, padx=5)
    tk.Button(frame, text="Center").pack(side=tk.LEFT, padx=5)
    tk.Button(frame, text="Right").pack(side=tk.LEFT, padx=5)

    #Fill and expand options
    tk.Label(place_root, text="Expanded", bg="salmon").pack(fill=tk.X, expand=True)

    place_root.mainloop()


    #Grid window
    grid_root = tk.Tk()
    grid_root.title(".grid() Demo -- Registration form")

    #Configure column weights for responsive resizing
    grid_root.columnconfigure(1, weight=1)

    #Row 0 - Name
    tk.Label(grid_root, text="Full Name:", font=("Arial", 11)).grid(
        row=0, column=0, padx=10, pady=8, sticky="e")
    tk.Entry(grid_root, font=("Arial", 11)).grid(
        row=0, column=1, padx= 5, pady=8, sticky="ew")
    
    #Row 1 - Email
    tk.Label(grid_root, text="Email:", font=("Arial", 11)).grid(
        row=1, column=0, padx=10, pady=8, sticky="e")
    tk.Entry(grid_root, font=("Arial", 11)).grid(
        row=1, column=1, padx=5, pady=8, sticky="ew")
    
    #Row 2 - Password
    tk.Label(grid_root, text="Password:", font=("Arial", 11)).grid(
        row=2, column=0, padx=10, pady=8, sticky="e")
    tk.Entry(grid_root, font=("Arial", 11)).grid(
        row=2, column=1, padx=5, pady=8, sticky="ew")
    
    #Row 3 - Button spanning 2 columns
    tk.Button(grid_root, text="Register", bg="#5B2C8E", font=("Arial", 11,"bold")).grid(
        row=3, column=0, columnspan=2, pady=15)

    grid_root.mainloop()


    #Place window
    place_root = tk.Tk()
    place_root.title(".Place() Demo")
    place_root.geometry("400x300")

    #Absolute positioning with x, y
    tk.Label(place_root, text=("Positioned at (50, 30)"), bg="lightblue").place(x=50, y=30)
    tk.Label(place_root, text=("Positioned at (150, 100)"), bg="lightgreen").place(x=150, y=100)
    
    #Relative positioning
    tk.Button(place_root, text="Centre").place(relx=0.5, rely=0.5, anchor="center")

    place_root.mainloop()

""" 6 Checkbuttons, Radiobuttons and Variables """
def check_radio_buttons():
    
    #Selection function
    def show_selection():
        selected = []
        if python_var.get(): 
            selected.append("Python")
        if java_var.get(): 
            selected.append("Java")
        if js_var.get(): 
            selected.append("JavaScript")
        if csharp_var.get(): 
            selected.append("C#")

        if selected:
            result_var.set("Selected: " + ", ".join(selected))
        else:
            result_var.set("No languages selected")

    #Window
    root = tk.Tk()
    root.title("Checkbuttons and Radiobuttons")
    root.geometry("400x420")

    #Checkbuttons
    tk.Label(root, text="Which languages do you know?", font=("Arial", 12, "bold")).pack(pady=(15,5))
    python_var = tk.BooleanVar()
    java_var = tk.BooleanVar()
    js_var = tk.BooleanVar()
    csharp_var = tk.BooleanVar()

    tk.Checkbutton(root, text="Python", variable=python_var, font=("Arial", 11)).pack(anchor="w", padx=40)
    tk.Checkbutton(root, text="Java", variable=java_var, font=("Arial", 11)).pack(anchor="w", padx=40)
    tk.Checkbutton(root, text="JavaScript", variable=js_var, font=("Arial", 11)).pack(anchor="w", padx=40)
    tk.Checkbutton(root, text="C#", variable=csharp_var, font=("Arial", 11)).pack(anchor="w", padx=40)

    tk.Button(root, text="Show Selection", command=show_selection, bg="#5B2C8E").pack(pady=10)
    result_var = tk.StringVar()
    tk.Label(root, textvariable=result_var, font=("Arial", 11), fg="#5B2C8E", wraplength=350).pack(pady=5)


    #Radiobuttons
    tk.Label(root, text="\npreferred label", font=("Arial", 12)).pack(pady=(10,5))

    difficulty_var = tk.StringVar(value="medium")

    for text, value in [("Easy","easy"),("Medium","medium"),("Hard","hard")]:
        tk.Radiobutton(root, text=text, variable=difficulty_var, value=value, font=("Arial", 11)).pack(anchor="w", pady=10)



    root.mainloop()




""" Main program loop for calling task """
def main():
    check_radio_buttons()

main()