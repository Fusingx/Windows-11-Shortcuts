import os
import pyperclip
import time
import win32gui
import win32con
import subprocess
import threading
import pygetwindow as gw
import pyautogui as p
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from urllib.parse import quote

# VARIABLES

CHROME_PATH = [r"C:\Program Files\Google\Chrome\Application\chrome.exe", '--profile-directory=Profile 1', "https://business.facebook.com/live/producer/?source=STREAM_KEYS&entry_point=biz_web_planner&target_id=191940727680414"]
OBS_PATH = r"C:\Program Files\obs-studio\bin\64bit\obs64.exe"
OBS_DIR = os.path.dirname(OBS_PATH)
IMAGES_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")

now = datetime.now()
date = now.strftime(f"%A {now.day} %B %Y")
is_paused = True

# HELPER FUNCTIONS

def find(image, timeout=600.0):
    image_path = os.path.join(IMAGES_DIR, image)
    start = time.time()
    print(f"Looking for {image}...")
    while time.time() - start < timeout:
        try:
            loc = p.locateOnScreen(image_path, grayscale=True, confidence=0.8) 
            if loc: return loc
        except p.ImageNotFoundException:
            pass
        time.sleep(0.1)
    return None

def paste(text):
    print(f"pasting {text}")
    pyperclip.copy(text)
    p.hotkey('ctrl', 'v')

def waitfor(window):
    windows = gw.getAllTitles() 
    while not (any(f'{window}' in w for w in windows)):
        time.sleep(0.1)
        windows = gw.getAllTitles() 
        print('waiting...')
    print('done waiting!')
    time.sleep(4)

# - MAIN FUNCTIONS -

def automation_sequence(pastor):
    # PROPRESENTER

    os.startfile(r"C:\Program Files\Renewed Vision\ProPresenter\ProPresenter.exe")
    waitfor('ProPresenter')
    time.sleep(3)
    p.click(find('sunday.jpg'))
    time.sleep(1)
    p.click(find('announcements.jpg'))
    time.sleep(1)
    p.click(find('group1.jpg'))
    time.sleep(1)
    win32gui.ShowWindow(win32gui.FindWindow(None, r'ProPresenter'), win32con.SW_MINIMIZE)

    # ATEM

    os.startfile(r"C:\Program Files (x86)\Blackmagic Design\Blackmagic ATEM Switchers\ATEM Software Control\ATEM Software Control.exe")
    waitfor('ATEM Mini Pro')
    p.hotkey('ctrl', 'r')
    time.sleep(1.5)
    paste(r"C:\Users\Sweetwaters Church\Documents\Atem November 2025 Settings 2025-11-19 07-17-09.xml")
    time.sleep(0.2) # not needed
    p.press('enter')
    time.sleep(0.2) # not needed
    p.click(find('restore.jpg'))
    time.sleep(1) # not needed
    win32gui.ShowWindow(win32gui.FindWindow(None, r'ATEM Mini Pro'), win32con.SW_MINIMIZE)

    # OBS

    subprocess.Popen([OBS_PATH], cwd=OBS_DIR)
    waitfor('OBS')
    p.click(find('virtcam.jpg'))
    time.sleep(0.5)

    # CHROME - FACEBOOK

    subprocess.Popen(CHROME_PATH)
    p.click(find("setup.jpg"))
    p.click(find("caption.jpg"))
    p.click(find("title.jpg"))
    paste(f"{date}] | Prayer Meeting")
    p.click(find("description.jpg"))
    paste(f"🔥🙏 Prayer with {pastor}\n\nJoin {pastor} this Wednesday at 7:30am on Facebook for a powerful time of prayer. Come ready to refocus, lift your faith, and start your day with purpose.\n\nDon’t miss it—we’re praying together.")
    p.click(find("save.jpg"))
    time.sleep(2)

    # CHROME - WHATSAPP

    message_text = f"🌿🙏 Prayer with {pastor}\n\nJoin us this Wednesday at 7:30am on Facebook for a calm, focused time of prayer led by {pastor}. Step away from the rush, centre your heart, and start your day grounded in faith.\n\nWatch here: https://www.facebook.com/swchurchtoti/live"
    encoded_message = quote(message_text)
    url = f"https://web.whatsapp.com/send?phone=27646690439&text={encoded_message}"
    subprocess.Popen([r"C:\Program Files\Google\Chrome\Application\chrome.exe", '--profile-directory=Profile 1', url])
    time.sleep(15)

    # LIKING SCRIPT

    root.deiconify()
    threading.Thread(target=automation_loop, daemon=True).start()
    messagebox.showinfo("Reminder", "Make sure everything you DON'T want liked is hidden\n(for ex. the pinned comment)")

def automation_loop():
    global is_paused
    while True:
        if not is_paused:
            loc = find('like.jpg', timeout=2.0)
            if loc:
                p.click(loc)
        
        time.sleep(1)

def on_pause_click(button):
    global is_paused
    is_paused = not is_paused
    
    if is_paused:
        button.config(text="Resume liking Comments", bg="#e1f5fe")
        print("Automation Paused")
    else:
        button.config(text="Pause Liking Comments", bg="#f0f0f0")
        print("Automation Resumed")

def on_start_click():
    selection = radio_var.get()
    pastor = "Ps Callie" if selection == "A" else "Ps Rodwin"

    for widget in root.winfo_children():
        widget.destroy()

    label = tk.Label(root, text="Prayer Meeting", font=("Arial", 12, "bold"), bg="#ffffff")
    label.pack(pady=15)

    pause_button = tk.Button(root, text="Start Liking Comments", width=20, height=2)
    pause_button.config(command=lambda: on_pause_click(pause_button))
    pause_button.pack(pady=5)

    end_button = tk.Button(root, text="Exit", command=root.destroy, width=20, height=2)
    end_button.pack(pady=5)

    root.iconify() # minimize

    threading.Thread(target=automation_sequence, args=(pastor,), daemon=True).start()

root = tk.Tk()
root.title("Prayer Meeting Script") 

win_w, win_h = 300, 300
x = (root.winfo_screenwidth() // 2) - (win_w // 2)
y = (root.winfo_screenheight() // 2) - (win_h // 2) - 50
root.geometry(f'{win_w}x{win_h}+{x}+{y}')
root.resizable(0, 0) 
root.configure(bg="#FFFFFF") 
root.attributes('-topmost', 1)
root.attributes('-alpha', 1.0)

label = tk.Label(root, text="Who's Doing Prayer Meeting?", font=("Arial", 12, "bold"), bg="#ffffff")
label.pack(pady=15)

radio_var = tk.StringVar(value="A")
radio1 = tk.Radiobutton(root, text="Ps. Callie", variable=radio_var, value="A")
radio2 = tk.Radiobutton(root, text="Ps. Rodwin", variable=radio_var, value="B")
radio1.pack()
radio2.pack(pady=10)

button = tk.Button(root, text="start", command=on_start_click, width=15)
button.pack(pady=5)

messagebox.showinfo("Before you start", "Make sure all everything is setup, power / camera is on etc")

root.mainloop()