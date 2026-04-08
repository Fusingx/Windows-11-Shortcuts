import tkinter as tk
import json
import os
import pyautogui as p
from datetime import datetime

# --- CONFIG & STYLING ---
DATA_FILE = os.path.join(os.path.dirname(os.path.realpath(__file__)), "task_data.json")
TODAY_DATE = datetime.now().strftime("%Y-%m-%d")
DAY_NAME = datetime.now().strftime("%A")

# colours (catppuccin mocha)
BG_MAIN = "#1e1e2e"
BG_BORDER = "#89b4fa"
FG_TEXT = "#cdd6f4"
FG_DONE = "#6c7086"
BG_ENTRY = "#313244"
FONT_PRIMARY = ("JetBrainsMono Nerd Font", 12)
FONT_HEADER = ("JetBrainsMono Nerd Font", 20, "bold")

# tasks
ROUTINE_TASKS = {
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
        "Confirm if CITM box is packed, then put the box in car (10 Minutes)",
        "Set Up for Youth (30 Minutes)",
        "Do sound and projection for Youth (2.5 Hours)"
    ]
}

# --- DATA MANAGEMENT ---
checkbox_vars = {}
current_entry = None

def load_data():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f: # with closes the file, open opens data files in "read only mode", f is a temp var that represents the file
                data = json.load(f) 
                saved_date = data.get("date")
                saved_routine = data.get("routine_tasks", {})
                saved_custom = data.get("custom_tasks", {})

                if saved_date == TODAY_DATE:
                    all_states = {**saved_routine, **saved_custom}
                    return all_states, saved_custom
                
                else:
                    rolled_over_custom = {
                        task: status for task, status in saved_custom.items() 
                        if status is False
                    }
                    
                    rolled_over_routine = {
                        task: status for task, status in saved_routine.items() 
                        if status is False
                    }

                    merged_rollover = {**rolled_over_routine, **rolled_over_custom}
                    return merged_rollover, rolled_over_custom
                    
        except (json.JSONDecodeError, KeyError):
            pass
    return {}, {}

def save_data():
    daily_routine = ROUTINE_TASKS.get(DAY_NAME, [])
    routine_states = {}
    custom_states = {}

    for task, var in checkbox_vars.items():
        if task in daily_routine:
            routine_states[task] = var.get()
        else:
            custom_states[task] = var.get()

    data_to_save = {
        "date": TODAY_DATE,
        "routine_tasks": routine_states,
        "custom_tasks": custom_states
    }
    with open(DATA_FILE, "w") as f:
        json.dump(data_to_save, f, indent=4)

# --- UI LOGIC ---
def toggle_strike(cb, var, task_text):
    if var.get():
        cb.config(font=(FONT_PRIMARY[0], FONT_PRIMARY[1], "overstrike"), fg=FG_DONE)
    else:
        cb.config(font=FONT_PRIMARY, fg=FG_TEXT)
    save_data()


def delete_task(cb, task_text):
    if task_text in checkbox_vars:
        del checkbox_vars[task_text] # tracking dictionary
    cb.destroy()
    save_data()

def create_checkbox(task_text, is_checked=False):
    if task_text in checkbox_vars: return 
    
    var = tk.BooleanVar(value=is_checked)
    checkbox_vars[task_text] = var
    
    cb = tk.Checkbutton(
        main_container, text=task_text, variable=var,
        bg=BG_MAIN, fg=FG_TEXT, activebackground=BG_MAIN,
        selectcolor=BG_MAIN, font=FONT_PRIMARY,
        padx=10, pady=2
    )

    cb.config(command=lambda c=cb, v=var, t=task_text: toggle_strike(c, v, t))
    
    cb.bind("<Button-2>", lambda event, c=cb, t=task_text: delete_task(c, t))
    
    cb.pack(pady=2, anchor="w", padx=30) # pady - between cbs // anchor = west // padx - left margin
    toggle_strike(cb, var, task_text)

def on_key_press(event):
    global current_entry
    
    if event.keysym == "Escape":
        root.destroy()
        return

    if event.keysym == "Return" and current_entry:
        new_task = current_entry.get().strip()
        if new_task:
            create_checkbox(new_task)
            save_data()
        current_entry.destroy()
        current_entry = None
        return

    if event.char and event.char.isprintable() and not current_entry:
        current_entry = tk.Entry(
            main_container, bg=BG_ENTRY, fg=FG_TEXT,
            insertbackground=FG_TEXT, font=FONT_PRIMARY,
            borderwidth=0, highlightthickness=1, highlightbackground=BG_BORDER
        )
        current_entry.pack(pady=10, padx=30, fill="x")
        current_entry.focus_set()
        current_entry.insert(0, event.char)

# --- MAIN GUI SETUP ---
root = tk.Tk()
root.overrideredirect(True)
root.configure(bg=BG_BORDER)

# center window
win_w, win_h = 650, 750
x = (root.winfo_screenwidth() // 2) - (win_w // 2)
y = (root.winfo_screenheight() // 2) - (win_h // 2)
root.geometry(f'{win_w}x{win_h}+{x}+{y}')

main_container = tk.Frame(root, bg=BG_MAIN)
main_container.pack(fill="both", expand=True, padx=1, pady=1)

root.bind("<Key>", on_key_press)

# header
tk.Label(
    main_container, text=f"{DAY_NAME} Checklist", 
    font=FONT_HEADER, bg=BG_MAIN, fg=FG_TEXT
).pack(pady=20)

# load tasks
saved_states, custom_tasks_only = load_data()

# routine
for task in ROUTINE_TASKS.get(DAY_NAME, ["Enjoy your day off!"]):
    create_checkbox(task, is_checked=saved_states.get(task, False))

# custom
for task, status in custom_tasks_only.items():
    create_checkbox(task, is_checked=status)

# move cursor
p.moveTo(x + (win_w // 2), y + (win_h // 3), duration=0.1)

root.mainloop()