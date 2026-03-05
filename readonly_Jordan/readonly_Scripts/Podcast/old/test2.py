import os
import pyautogui as p
import time
import win32gui
import win32con

# Get a handle to the foreground window (the active window)
#window_handle = win32gui.GetForegroundWindow()

# Minimize the window
#win32gui.ShowWindow(window_handle, win32con.SW_MINIMIZE)

def close_terminal():
    win32gui.ShowWindow(win32gui.FindWindow(None, r'C:\WINDOWS\system32\cmd.exe'), win32con.SW_MINIMIZE)
    win32gui.ShowWindow(win32gui.FindWindow(None, 'test2.py - Command - Visual Studio Code'), win32con.SW_MINIMIZE)


close_terminal()

time.sleep(5)
p.press('esc') # exit out of any tabs
time.sleep(2)
p.hotkey('ctrl', 'shift', 'e') # export hotkey
time.sleep(2)
p.typewrite('Name') # type podcast name
time.sleep(2)
p.click(1055, 364) # click path
time.sleep(2)
p.hotkey('ctlr', 'a') # select all
time.sleep(2) 
p.typewrite(r"C:\Users\Sweetwaters Church\Desktop\Jordan's Desktop\Documents\Podcast Editing\Ripple Effect Part 2") # type path
time.sleep(2)
p.click(1095, 415) # format
time.sleep(2)
p.press(['down', 'down', 'enter']) # enter format
time.sleep(2)
p.click(947, 471) # click stereo
time.sleep(2)
p.click(1055, 502) # click sample rate
time.sleep(2)
p.press('down', presses=8) # set sample rate
time.sleep(2)
p.press('enter') # confirm
time.sleep(2)
p.click(1055, 535) # click bitrate mode
time.sleep(2)
p.press(['up', 'up', 'up', 'enter']) # set bitrate mode
time.sleep(2)
p.click(1055, 567) # click quality
time.sleep(2)
p.press(['up', 'up', 'up', 'down', 'enter']) # set quality
time.sleep(2)
p.click(884, 617) # click entire project
time.sleep(2)
p.click(773, 741) # click meta data
time.sleep(2)
p.click(964, 630) # click load
time.sleep(2)
p.typewrite('Tags.xml') # type path of tags
time.sleep(2)
p.press('enter') # confirm
time.sleep(2)
p.click(1095, 430) # click track title
time.sleep(2)
p.typewrite(f'Ripple Effect Part 2') # type podcast name
time.sleep(2)
p.press(['enter', 'enter', 'enter']) # confirm and export



# (1095, 350) is (255, 255, 255) NAME
# (1055, 364) is (255, 255, 255) EXPORT PATH
# (1095, 415) is (229, 241, 251) FORMAT
# DOWN DOWN ENTER
# (947, 471) is (255, 255, 255) STEREO
# (1055, 502) is (229, 241, 251) SAMPLE RATE
# PRESS DOWN 8 TIMES THEN ENTER
# (1055, 535) is (224, 235, 245) BIT RATE MODE
# UP 3 TIMES ENTER
# (1055, 567) is (225, 236, 246) QUALITY
# 3 UP 1 DOWN ENTER
# (884, 617) is (255, 255, 255) ENTIRE PROJECT

# (773, 741) is (90, 0, 56) META DATA
# (964, 630) is (224, 238, 249) LOAD
# TYPE 'Tags.xml' ENTER
# (1095, 430) is (255, 255, 255) TRACK TITLE
# TYPERIGHT {PODCAST TITLE} ENTER ENTER
# ENTER