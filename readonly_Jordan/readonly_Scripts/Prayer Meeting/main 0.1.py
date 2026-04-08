import os
import pyperclip
import time
import win32gui
import win32con
import subprocess
import pygetwindow as gw
import pyautogui as p

CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe", '--profile-directory=Profile 1', "https://business.facebook.com/live/producer/2385271268563249/?entry_point=biz_web_planner"
OBS_PATH = r"C:\Program Files\obs-studio\bin\64bit\obs64.exe"
OBS_DIR = os.path.dirname(OBS_PATH)
IMAGES_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")

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
    pyperclip.copy(text)
    p.hotkey('ctrl', 'v')

def waitfor(window):
    windows = gw.getAllTitles() 
    while not (any(f'{window}' in w for w in windows)):
        time.sleep(0.1)
        windows = gw.getAllTitles() 
    time.sleep(3)

# PROPRESENTER

os.startfile(f"C:\Program Files\Renewed Vision\ProPresenter\ProPresenter.exe")
waitfor('ProPresenter')
time.sleep(5)
p.click(find('sunday.jpg'))
time.sleep(1)
p.click(find('announcements.jpg'))
time.sleep(1)
p.click(find('group1.jpg'))
time.sleep(1)
win32gui.ShowWindow(win32gui.FindWindow(None, r'ProPresenter'), win32con.SW_MINIMIZE)

# ATEM

os.startfile(f"C:\Program Files (x86)\Blackmagic Design\Blackmagic ATEM Switchers\ATEM Software Control\ATEM Software Control.exe")
waitfor('ATEM Mini Pro')
p.hotkey('ctrl', 'r')
time.sleep(1)
paste(r"C:\Users\Sweetwaters Church\Documents\Atem November 2025 Settings 2025-11-19 07-17-09.xml")
time.sleep(0.2) # not needed
p.press('enter')
time.sleep(0.2) # not needed
p.click(find('restore.jpg'))
time.sleep(0.2) # not needed
win32gui.ShowWindow(win32gui.FindWindow(None, r'ATEM Mini Pro'), win32con.SW_MINIMIZE)

# OBS

subprocess.Popen([OBS_PATH], cwd=OBS_DIR)
waitfor('OBS')
p.click(find('virtcam.jpg'))

# CHROME

# subprocess.Popen(CHROME_PATH)
# p.click(find("setup.jpg"))
# p.click(find("caption.jpg"))
# p.click(find("title.jpg"))
# paste(f"{date}] | Prayer Meeting")
# p.click(find("description.jpg"))
# paste(f"🔥🙏 Prayer with {pastor}\n\nJoin {pastor} this Wednesday at 7:30am on Facebook for a powerful time of prayer. Come ready to refocus, lift your faith, and start your day with purpose.\n\nDon’t miss it—we’re praying together.")
# p.click(find("save.jpg"))
