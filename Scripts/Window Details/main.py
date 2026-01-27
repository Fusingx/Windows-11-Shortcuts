import win32gui
import win32process
import psutil
import time

def inspect_active_window():
    hwnd = win32gui.GetForegroundWindow()
    title = win32gui.GetWindowText(hwnd)
    class_name = win32gui.GetClassName(hwnd)

    _, pid = win32process.GetWindowThreadProcessId(hwnd)
    process = psutil.Process(pid).name()

    print("Process:", process.replace(".exe", "").upper())
    print("Window class:", class_name)
    print("Window title:", title)

time.sleep(4)
inspect_active_window()
