import pyautogui as p
import time
import win32con
import win32gui
import os

time.sleep(6)

def count_up_to(n):
    i = 0
    while i < n:
        yield i
        i += 1

# Using the generator
for num in count_up_to(5000000):
    print(num)