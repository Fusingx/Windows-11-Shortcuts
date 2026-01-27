import pyautogui as p
import time
import win32gui
import win32con

def close_terminal():
    win32gui.ShowWindow(win32gui.FindWindow(None, r'C:\WINDOWS\system32\cmd.exe'), win32con.SW_MINIMIZE)
    win32gui.ShowWindow(win32gui.FindWindow(None, r'C:\WINDOWS\System32\WindowsPowerShell\v1.0\powershell.exe'), win32con.SW_MINIMIZE)
    win32gui.ShowWindow(win32gui.FindWindow(None, 'Main.py - Scripts - Visual Studio Code'), win32con.SW_MINIMIZE)

def find(element, timeout=0):
    if timeout != 0:
        TIMEOUT = timeout
        START_TIME = time.time()
    print(f'Attempting to locate "{element}"')
    while True:
        try:
            coord = p.locateOnScreen(f'{element}', confidence=0.8)
            if coord:
                print(f'"{element}" Located')
                return coord
        except:
            p.ImageNotFoundException
        
        if timeout != 0:
            if time.time() - START_TIME > TIMEOUT:
                print(f'Failed to locate "{element}"')
                p.press('right')
                return False
            

close_terminal()

name = 1

while True:
    hd = find('hd.jpg')
    # if hd == False:
    #     print('ending')
    #     break
    p.click(hd)

    conf = find('conf.jpg')
    # if conf == False:
    #     print('ending')
    #     break
    p.click(conf)

    time.sleep(0.5)
    str_name = str(name)
    p.typewrite(f'{str_name}')
    p.press('enter')
    time.sleep(0.5)
    p.press('right') 
    name += 1