import os
import win32gui
import win32con
import pyautogui as p
import time
import random
import pygetwindow
import random
import tkinter as tk
from tkinter import ttk, messagebox

# --- 1. FUNCTIONS ---
def on_button_click():
    # Showing a simple popup box
    messagebox.showinfo("Message", "Button was clicked!")

# --- 2. WINDOW SETUP ---
root = tk.Tk()

# Sets the title in the top bar
root.title("title") 

# Sets the size: "WidthxHeight"
root.geometry("500x750") 

# Prevents/Allows resizing (Width, Height). 0 = Fixed, 1 = Resizable
root.resizable(1, 1) 

# Sets the background color of the main window
root.configure(bg="#000000") 

# Keep window on top of everything else (1 = True, 0 = False)
root.attributes('-topmost', 0)

# Sets the window transparency (0.0 to 1.0)
root.attributes('-alpha', 1.0)

# --- 3. WIDGETS ---

# LABEL: Simple text display
# 'fg' = foreground color, 'font' = (Family, Size, Style)
label = tk.Label(root, text="label", font=("Arial", 12, "bold"), bg="#f0f0f0")
label.pack(pady=5)

# BUTTON: Triggers a function
button = tk.Button(root, text="button", command=on_button_click, width=15)
button.pack(pady=5)

# ENTRY: Single-line input
entry = tk.Entry(root, width=30)
entry.insert(0, "entry (type here)")
entry.pack(pady=5)

# CHECKBUTTON: Toggle switch
check_var = tk.BooleanVar()
checkbutton = tk.Checkbutton(root, text="checkbutton", variable=check_var)
checkbutton.pack(pady=5)

# RADIOBUTTONS: Mutually exclusive options (Pick one)
radio_var = tk.StringVar(value="A")
radio1 = tk.Radiobutton(root, text="radiobutton A", variable=radio_var, value="A")
radio2 = tk.Radiobutton(root, text="radiobutton B", variable=radio_var, value="B")
radio1.pack()
radio2.pack()

# SCALE: A slider for numbers
scale = tk.Scale(root, from_=0, to=100, orient="horizontal", label="scale")
scale.pack(pady=5)

# LISTBOX: A box of selectable items
listbox = tk.Listbox(root, height=3)
listbox.insert(1, "listbox item 1")
listbox.insert(2, "listbox item 2")
listbox.pack(pady=5)

# SPINBOX: Number selector with arrows
spinbox = tk.Spinbox(root, from_=0, to=10)
spinbox.grid_forget() # Just showing we can use grid too
spinbox.pack(pady=5)

# TEXT: Multi-line text area
text = tk.Text(root, height=4, width=40)
text.insert("1.0", "text (multi-line area)")
text.pack(pady=5)

# LABELFRAME: A box with a border and a title to group things
frame = tk.LabelFrame(root, text="frame", padx=10, pady=10)
frame.pack(pady=10)
tk.Label(frame, text="Inside the frame").pack()

# OPTIONMENU: A dropdown menu
options = ["Option 1", "Option 2", "Option 3"]
clicked = tk.StringVar(value=options[0])
drop = tk.OptionMenu(root, clicked, *options)
drop.pack(pady=5)

# PROGRESSBAR: (From the ttk library)
progress = ttk.Progressbar(root, orient="horizontal", length=200, mode='determinate')
progress.pack(pady=10)
progress['value'] = 70 # Sets progress to 70%

# --- 4. THE LOOP ---
# This keeps the window running and listening for events
root.mainloop()


