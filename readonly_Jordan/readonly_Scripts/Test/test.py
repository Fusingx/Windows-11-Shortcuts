import os
import time
import subprocess
import threading
import queue
import win32gui
import win32con
import win32api
import random
import pyperclip
import pyautogui as p
import pygetwindow as gw
from pynput import mouse, keyboard
import keyboard as key
import winreg
import ctypes

# messages = ["_kayleigh_", "*kayleigh*", "`kayleigh`", "```kayleigh```", "~kayleigh~", "kayleigh"]

# def paste(text):
#     pyperclip.copy(text)
#     p.hotkey('ctrl', 'v')

# time.sleep(5)

# while True:
#     paste(messages[random.randint(0, len(messages) - 1)])
#     p.press('space')

import tkinter as tk

def add_task():
    task_text = task_entry.get()  # Get text from input field
    if task_text.strip():         # Only add if it's not empty
        var = tk.BooleanVar()
        
        # Create the new checkbox
        new_cb = tk.Checkbutton(
            list_frame, 
            text=task_text, 
            variable=var, 
            bg="#FFFFFF",
            # Reusing the strikethrough logic from before
            command=lambda: toggle_strike(new_cb, var)
        )
        new_cb.pack(pady=2, anchor="w", padx=10)
        
        # Clear the entry field for the next task
        task_entry.delete(0, tk.END)

def toggle_strike(cb, var):
    if var.get():
        cb.config(font=("JetBrainsMono Nerd Font", 10, "overstrike"), fg="#888888")
    else:
        cb.config(font=("JetBrainsMono Nerd Font", 10), fg="#000000")

root = tk.Tk()
root.geometry("400x600")
root.configure(bg="#FFFFFF")

# --- INPUT SECTION ---
input_frame = tk.Frame(root, bg="#FFFFFF")
input_frame.pack(pady=20)

task_entry = tk.Entry(input_frame, font=("JetBrainsMono Nerd Font", 10), width=30)
task_entry.pack(side="left", padx=5)

# Bind 'Enter' key to the add_task function for speed
task_entry.bind("<Return>", lambda e: add_task())

add_btn = tk.Button(input_frame, text="Add Task", command=add_task)
add_btn.pack(side="left")

# --- LIST SECTION ---
# This frame acts as a container for all dynamically added checkboxes
list_frame = tk.Frame(root, bg="#FFFFFF")
list_frame.pack(fill="both", expand=True)

root.mainloop()