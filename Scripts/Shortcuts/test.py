import os
import win32gui
import win32con
import pyautogui as p
import time
import random
import pygetwindow
import random

path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "wallpapers")

# for file in os.listdir(path):
#                        print(file)

wallpapers = os.listdir(path)


wallpaper = os.path.join(os.path.dirname(os.path.realpath(__file__)), "wallpapers", wallpapers[random.randint(1, len(wallpapers))])
win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, wallpaper, 1+2)



