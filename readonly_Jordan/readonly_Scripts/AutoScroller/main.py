import pyautogui as p
import time
import win32gui
import win32con

print(r'''    _         _       ____                 _ _           
   / \  _   _| |_ ___/ ___|  ___ _ __ ___ | | | ___ _ __ 
  / _ \| | | | __/ _ \___ \ / __| '__/ _ \| | |/ _ \ '__|
 / ___ \ |_| | || (_) |__) | (__| | | (_) | | |  __/ |   
/_/   \_\__,_|\__\___/____/ \___|_|  \___/|_|_|\___|_|   

''')

speed = input('Select Speed (leave blank for default=15): ')
if not speed:
    speed = 15
speed = int(speed)
print()
print(f'speed = {-speed}')
print()
print('Starting in 5 Seconds...')
time.sleep(1)
print('(reminder: move cursor to screen corner to end script)')
time.sleep(3)
win32gui.ShowWindow(win32gui.FindWindow(None, 'Windows PowerShell'), win32con.SW_MINIMIZE)
time.sleep(1)

while True:
    p.scroll(-speed)