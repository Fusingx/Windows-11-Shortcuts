import os
import win32gui
import win32con
import pyautogui as p
import pygetwindow as gw
import time


CONFIG = {"images_dir": os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
}

print('Welcome')

def find(image, timeout=5.0):
    image_path = os.path.join(CONFIG["images_dir"], image)
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

screen_w, screen_h = p.size()

p.rightClick(screen_w - 30, screen_h // 2)
time.sleep(1.2)
p.press('right')
time.sleep(0.2)
p.press('up')
time.sleep(0.2)
p.press('enter')

print('Toggling Taskbar')
current_pos = p.position()      
os.system("start ms-settings:taskbar")
behaviors = find('behaviors.jpg')
if behaviors:
    p.moveTo(behaviors)
    time.sleep(0.3)
    p.click(behaviors)
time.sleep(0.6)
for i in range(2):
    p.press('tab')
    time.sleep(0.005)
time.sleep(0.25)
p.press('space')
time.sleep(0.25)
p.hotkey('alt', 'f4')
p.moveTo(current_pos)

os.startfile(r"C:\Program Files\Windhawk\Windhawk.exe", arguments="-tray-only")
os.startfile(r"C:\Users\Sweetwaters Church\AppData\Roaming\AltSnap\AltSnap.exe")
os.startfile(r"C:\Program Files\CopyQ\copyq.exe")
os.startfile('zen.exe') # open zen and spotify
os.startfile(r"C:\Users\Sweetwaters Church\AppData\Roaming\Spotify\Spotify.exe")

# for i in range(100): # welcome text on terminal
#     colour = random.randrange(31, 39)
#     print(f'\033[{colour}mWelcome !\033[0m')
#     time.sleep(0.02)

windows = gw.getAllTitles() 
while not (any('Zen' in w for w in windows) and any('Spotify' in w for w in windows)): # makes sure spotify & zen are actually open before trying to minimize them
    time.sleep(0.1)
    windows = gw.getAllTitles() 
    print(windows)
time.sleep(1)

win32gui.ShowWindow(win32gui.FindWindow(None, r'Zen Browser'), win32con.SW_MINIMIZE) # minimize zen & spotify
win32gui.ShowWindow(win32gui.FindWindow(None, r'Spotify Premium'), win32con.SW_MINIMIZE)
input()