import tkinter as tk
import json
import os
import pyautogui as p
from datetime import datetime


# --- CONFIG ---
DATA_FILE = os.path.join(os.path.dirname(os.path.realpath(__file__)), "task_data.json")
today_date = datetime.now().strftime("%Y-%m-%d") # ex. "2026-03-11"
day_name = datetime.now().strftime("%A")        # ex. "Wednesday"

tasks = {
    "Monday": [
        "Move Offering Bags From Rodwins Office to Church before 8:30am",
        "Attend weekly staff meeting at 9am (1 to 1.5 hours)",
        "Select, Edit and Post (after approval) 11+ Photos (Including Quote) (2-3 Hours)",
        "Send photos onto the church media content group for approval",
        "Edit and Post Podcast (30 Minutes)",
        "Edit and Post YouTube Video of Sermon (30 Minutes)",
        "Edit Prayer Image and send to Chris (10 Minutes)",
        "Copy photos onto external and Clear SD cards (10 Minutes)"
    ],
    "Tuesday": [
        "Prepare songs and Mics (x2) for Hope Service",
        "Do sound and projection for Hope service (1 Hour)",
        "Move Prayer Meeting Banner",
        "Select, Edit and Post Photos of Saturday or other events (1-2 Hours)",
        "Send photos onto the church media content group for approval",
        "Create Recap Video (1-2 Hours)",
        "Submit Recap video for approval by 2pm on Church Media Group",
        "Get approval and edit if necessary by 2:45pm",
        "Setup camera and sound for Discipleship (15 Minutes)",
        "Do sound and projection for Discipleship (Every 2nd Week) (2.5 Hours)"
    ],
    "Wednesday": [
        "Do sound and projection for Prayer Meeting (Every 2nd week) (1 Hour)",
        "Packup after Prayer Meeting (20 Minutes)",
        "Rotate Posters (10 Minutes)",
        "Edit Kids Church Powerpoint Video (15 Minutes)",
        "Edit Kids Church Powerpoint Presentation (30 Minutes)",
        "Edit Kids Church AD Image (15 Minutes)",
        "Get announcement information & recordings for Sunday (1 Hour)",    
        "Edit Announcement Video for Main & CITM Service (1 Hour)",
        "Ensure batteries are charged (Mic, Camera etc...) (10 Minutes)"
    ],
    "Thursday": [
        "Load CITM Worship Songs & Announcement Video (15 Minutes)",
        "Load Main Service Worship Lyrics (IO Minutes)",
        "Create 'Look Forward' Video (filming / recording & editing) (2-3 Hours)",
        "Do sound and projection for Ladies Meeting (Every 2nd & 4th week) (2 Hour)",
        "Ensure sound desk and work area is neat and tidy (15 Minutes)",
        "Meet with Chris about Youth Prep (30 Minutes)"
    ],
    "Friday": [
        "Make stage neat and tidy and ready for Sunday service (15 Minutes)",
        "Projects (Discipleship Slides, youth centre stuff etc...) (1-2 Hours)",
        "Confirm with Venessa if CITM box is packed, then put the box in Ps Rodwin's car boot (10 Minutes)",
        "Set Up for Youth (30 Minutes)",
        "Do sound and projection for Youth (2.5 Hours)"
    ]
}

def load_data():
    """loads states and checks if its a new day"""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                data = json.load(f)
                if data.get("date") == today_date:
                    return data.get("tasks", {})
        except (json.JSONDecodeError, KeyError):
            pass 
    return {}

def save_data():
    """saves date and checkbox states"""
    data_to_save = {
        "date": today_date,
        "tasks": {task: var.get() for task, var in checkbox_vars.items()}
    }
    with open(DATA_FILE, "w") as f:
        json.dump(data_to_save, f)

def on_key_press(event):
    # event.char -> the character (e.g., 'a', 'b', '1')
    # event.keysym -> the name of the key (e.g., 'Escape', 'Return', 'space')
    
    print(f"Key Pressed: {event.keysym}")
    
    # Example: Close the app if 'Escape' is pressed
    if event.keysym == "Escape":
        root.destroy()

# --- GUI ---
root = tk.Tk()
root.overrideredirect(True)
root.configure(bg="#89b4fa") # border

root.bind("<Key>", on_key_press)

# geometry
win_w, win_h = 630, 700
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (win_w // 2)
y = (screen_height // 2) - (win_h // 2)
root.geometry(f'{win_w}x{win_h}+{x}+{y}')

main_container = tk.Frame(root, bg="#1e1e2e")
main_container.pack(fill="both", expand=True, padx=1, pady=1)

checkbox_vars = {}
saved_states = load_data()

def toggle_strike(cb, var, task_text):
    if var.get():
        cb.config(font=("JetBrainsMono Nerd Font", 12, "overstrike"), fg="#888888")
    else:
        cb.config(font=("JetBrainsMono Nerd Font", 12), fg="#cdd6f4")
    save_data()

# header
tk.Label(main_container, text=f"{day_name} Checklist", font=("JetBrainsMono Nerd Font", 20, "bold"), 
         bg="#1e1e2e", fg="#cdd6f4").pack(pady=20)

# task list
current_tasks = tasks.get(day_name, ["Enjoy your day off!"])

for task_text in current_tasks:
    var = tk.BooleanVar(value=saved_states.get(task_text, False))
    checkbox_vars[task_text] = var
    
    cb = tk.Checkbutton(
        main_container, text=task_text, variable=var,
        bg="#1e1e2e", fg="#cdd6f4", activebackground="#1e1e2e",
        selectcolor="#1e1e2e", font=("JetBrainsMono Nerd Font", 12)
    )
    
    cb.config(command=lambda c=cb, v=var, t=task_text: toggle_strike(c, v, t))
    toggle_strike(cb, var, task_text) 
    cb.pack(pady=5, anchor="w", padx=30)

center_x = screen_width / 2
center_y = screen_height / 2.5
p.moveTo(center_x, center_y, duration=0.1)
root.mainloop()