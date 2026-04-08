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

os.startfile(r"C:\Program Files (x86)\Blackmagic Design\Blackmagic ATEM Switchers\ATEM Software Control\ATEM Software Control.exe")
waitfor('ATEM Mini Pro')
p.hotkey('ctrl', 'r')
time.sleep(1.5)
paste(r"C:\Users\Sweetwaters Church\Documents\Atem November 2025 Settings 2025-11-19 07-17-09.xml")
time.sleep(0.2) # not needed
p.press('enter')
time.sleep(0.2) # not needed
p.click(find('restore.jpg'))
time.sleep(2) # not needed
win32gui.ShowWindow(win32gui.FindWindow(None, r'ATEM Mini Pro'), win32con.SW_MINIMIZE)