import os
import time
import subprocess
import threading
import queue
import win32gui
import win32con
import win32api
import pyautogui as p
import pygetwindow as gw
from pynput import mouse, keyboard
import keyboard as key
import winreg
import ctypes

def toggle_cursor(colour):
    # Path to the black cursor
    black_cursor_path = r"C:\Windows\Cursors\arrow_r.cur"
    default_cursor_path = r"C:\Windows\Cursors\aero_arrow.cur"
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Control Panel\Cursors", 0, winreg.KEY_SET_VALUE) # Update the Registry
    winreg.SetValueEx(key, "Arrow", 0, winreg.REG_SZ, colour)
    winreg.CloseKey(key)
    ctypes.windll.user32.SystemParametersInfoW(0x0057, 0, None, 0) # Tell Windows to update the UI (SystemParametersInfo)


