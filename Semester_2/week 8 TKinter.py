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
    #Creates root window and names it
    root = tk.Tk()
    root.title("First TKinter window")

    #Sets window size and stops resizing
    root.geometry("400x300")
    root.resizable(False,False)

    #Sets background colour
    root.configure(bg="#f0f0f0")

    #Window loop
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


""" 7 Listbox and Scrollbar """
def listbox_and_scrollbar():

    #Functions
    def add_item():
        item = entry.get().strip()
        if item:
            listbox.insert(tk.END, item)
            entry.delete(0, tk.END)
            status_var.set(f"{item} has been added to the list")

    def remove_item():
        selection = listbox.curselection()
        if selection:
            item = listbox.get(selection[0])
            listbox.delete(selection[0])
            status_var.set(f"{item} removed from the list")
        else:
            status_var.set("No item selected")

    def clear_all():
        listbox.delete(0, tk.END)
        status_var.set("All items cleared from list")
    
    #Window
    root = tk.Tk()
    root.title("Listbox tutorial")
    root.geometry("400x400")

    #Input frame
    input_frame = tk.Frame(root)
    input_frame.pack(pady=10, padx=10, fill=tk.X)

    entry = tk.Entry(input_frame, font=("Arial", 11))
    entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0,5))
    entry.bind("<Return>", lambda e: add_item())

    tk.Button(input_frame, text="Add", command=add_item, bg="#5B2C8E").pack(side=tk.LEFT)

    #Listbox with scrollbar
    list_frame = tk.Frame(root)
    list_frame.pack(pady=5, padx=10, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(list_frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    listbox = tk.Listbox(list_frame, font=("Arial", 11), selectmode=tk.SINGLE,
                         yscrollcommand=scrollbar.set, activestyle="none")
    listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.config(command=listbox.yview)

    #Sample data
    for item in ["Python", "Java", "C++", "Go", "Rust", "Swift",
                 "JavaScript", "Kotlin", "Ruby", "TypeScript"]:
        listbox.insert(tk.END, item)

    #Actions buttons
    btn_frame = tk.Frame(root)
    btn_frame.pack(pady=5)

    tk.Button(btn_frame, text="Remove Selected", command=remove_item).pack(
        side=tk.LEFT, padx=5)
    tk.Button(btn_frame, text="Clear all", command=clear_all).pack(
        side=tk.LEFT, padx=5)
    
    #Status bar
    status_var = tk.StringVar(value="Ready")
    tk.Label(root, textvariable=status_var, relief="sunken", anchor="w", font=("Arial", 10)).pack(
        fill=tk.X, padx=10, pady=(5, 10))

    root.mainloop()

""" 8 Menus and Message Boxes """
def menus_and_messege_boxes():
    from tkinter import messagebox #message box needs to be imported

    #Functions
    def new_file():
        text_area.delete("1.0", tk.END)
        root.title("UNTITLED - Simple Editor")

    def about():
        messagebox.showinfo("About", "Simple Text Editor\nCIS1703 Tutorial\nVersion 1.0")

    def quit_app():
        if messagebox.askyesno("Quit", "Are you sure you want to quit?"):
            root.destroy()

    def show_warning():
        messagebox.showwarning("Warning", "This action cannot be undone!")

    def show_error():
        messagebox.showerror("Error", "Something went wrong!")

    #Window
    root = tk.Tk()
    root.title("Simple Text Editor")
    root.geometry("500x400")

    #Create menu bar
    menu_bar = tk.Menu(root)
    root.config(menu=menu_bar)

    #File menu
    file_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="New", command=new_file)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=quit_app)

    #Help menu
    help_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Help", menu=help_menu)
    help_menu.add_command(label="About", command=about)
    help_menu.add_command(label="Test Warning", command=show_warning)
    help_menu.add_command(label="Test Error", command=show_error)

    #Text area
    text_area = tk.Text(root, font=("Arial", 12), wrap="word")
    text_area.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

    root.mainloop()

""" 9 Frames and Organizing Your Interface """
def frames_tutorial():

    #Window
    root = tk.Tk()
    root.title("Frames Demo -- Contact Card")
    root.geometry("450x350")
    root.configure(bg="#b2b2b2")

    #Header frame (using pack)
    header = tk.Frame(root, bg="#5B2C8E", height=60)
    header.pack(fill=tk.X)
    header.pack_propagate(False)
    tk.Label(header, text="Contact Manager", font=("Arial", 16, "bold"), bg="#744E9C", fg="white").pack(expand=True)

    #Form frame (using grid)
    form = tk.Frame(root, bg="#f0f0f0")
    form.pack(pady=15, padx=15, fill=tk.X)

    fields = ["First Name", "Last Name", "Email", "Phone"]
    entries = {}

    for i, field in enumerate(fields):
        tk.Label(form, text=field + ":", font=("Arial", 11), bg="#f0f0f0").grid(
            row=i, column=0, pady=5, padx=5, sticky="e")
        entry = tk.Entry(form, font=("Arial", 11), width=30)
        entry.grid(row=i, column=1, pady=5, padx=5, sticky="w")
        entries[field] = entry

    #Button frame
    btn_frame = tk.Frame(root, bg="#f0f0f0")
    btn_frame.pack(pady=10)

    for text, colour in [("Save","#5B2C8E"), ("Clear", "#666"), ("Cancel", "#CC3333")]:
        tk.Button(btn_frame, text=text, bg=colour, font=("Arial", 10, "bold"), width=10).pack(
            side=tk.LEFT, padx=5)
        
    #Status bar frame
    status_frame = tk.Frame(root, bg="#ddd", height=25)
    status_frame.pack(fill=tk.X, side=tk.BOTTOM)
    status_frame.pack_propagate(False)
    tk.Label(status_frame, text="Ready", font=("Arial", 9), bg="#ddd", anchor="w").pack(
        fill=tk.X, padx=5)

    root.mainloop()

""" Main program loop for calling task """
def main():
    frames_tutorial()

main()