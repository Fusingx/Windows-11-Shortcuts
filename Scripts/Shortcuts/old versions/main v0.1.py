import os
import win32gui
import win32con
import time
import pygetwindow as gw
from pynput import mouse
from pynput import keyboard
import pyautogui as p

windows = gw.getAllTitles()
active_window = win32gui.GetForegroundWindow()
title = win32gui.GetWindowText(active_window)
button_signal = None
listener_running = True
paused = False

# find

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
            
# pynput stuff

def on_click(x, y, button, pressed):
    global button_signal, listener_running
    if pressed:
        #print(f'{button}')
        if button == mouse.Button.x1:  # Mouse 4
            print(f"Mouse Button 4 clicked at ({x}, {y})")
            button_signal = "x1"
            listener_running = False
            return False  # stop listener
        elif button == mouse.Button.x2:  # Mouse 5
            print(f"Mouse Button 5 clicked at ({x}, {y})")
            button_signal = "x2"
            listener_running = False
            return False  # stop listener

def on_activate(hotkey):
    global button_signal, listener_running
    if hotkey == '<ctrl>+<alt>+q':
        button_signal = "exit"
        
    elif hotkey == '<ctrl>+<alt>+m':
        button_signal = "shutdown"

    elif hotkey == '<ctrl>+<alt>+r':
        button_signal = "reload"

    elif hotkey == '<ctrl>+<alt>+p':
        button_signal = "pause"

    listener_running = False
    return False  # stop listener

def startListener():
    global button_signal, listener_running
    
    # Reset variables
    button_signal = None
    listener_running = True
    
    # Create listeners
    mouse_listener = mouse.Listener(on_click=on_click)
    keyboard_listener = keyboard.GlobalHotKeys({
        '<ctrl>+<alt>+q': lambda: on_activate('<ctrl>+<alt>+q'),
        '<ctrl>+<alt>+m': lambda: on_activate('<ctrl>+<alt>+m'),
        '<ctrl>+<alt>+r': lambda: on_activate('<ctrl>+<alt>+r'),
        '<ctrl>+<alt>+p': lambda: on_activate('<ctrl>+<alt>+p')
    })
    
    # Start listeners
    mouse_listener.start()
    keyboard_listener.start()
    
    print("Listening...")
    
    # Wait until a signal is received
    while listener_running:
        time.sleep(0.01)
    
    # Stop both listeners
    mouse_listener.stop()
    keyboard_listener.stop()
    
    # Wait for listeners to actually stop
    mouse_listener.join()
    keyboard_listener.join()
    
    print(f"Listener stopped, returning signal: {button_signal}")
    return button_signal

# SCRIPTS #

# powerpoint

def x1_powerpoint():
    p.click()
    mouse_pos = p.position()
    coord = find('colour.jpg', 2)
    if not coord:
        return
    p.click(coord)
    p.moveTo(mouse_pos)
    p.hotkey('ctrl', 'b')
    p.hotkey('ctrl', 'u')
    main()

def x2_powerpoint():
    p.click()
    p.hotkey('ctrl', 'a')
    mouse_pos = p.position()
    coord = find('paste.jpg', 2)
    if not coord:
        return
    p.click(coord)
    p.moveTo(mouse_pos)
    main()

# propresenter
def x1_propresenter():
    p.rightClick()
    mouse_pos = p.position()
    p.click(find('edit.jpg'))
    p.moveTo(mouse_pos)
    main()

def x2_propresenter():
    p.click()
    p.hotkey('ctrl', 'a')
    p.hotkey('alt', 'v')
    main()

# lightroom

def x1_lightroom():
    #pos = p.position()
    #notcrop = find('notcrop.jpg')
    #p.moveTo(notcrop)
    #p.click(notcrop)
    #p.moveTo(pos)
    p.press('r')

def x2_lightroom():
    pos = p.position()
    notcrop = find('notcrop.jpg')
    p.moveTo(notcrop)
    p.click(notcrop)
    p.press('r')
    original = find('original.jpg', timeout=1)
    if original == False:
        p.moveTo(pos)
        return
    p.click(original)
    p.click(find('1x1.jpg'))
    p.moveTo(pos)

# spotify
def x1_spotify():
    p.press('playpause')
    main()

def x2_spotify():
    p.press('nexttrack')
    main()

# kill all
def kill_all():
    print('Terminating Windows')

    def check_windows():
        windows = gw.getAllTitles()
        active_window = win32gui.GetForegroundWindow()
        title = win32gui.GetWindowText(active_window)

        # list of what not to close
        sys_windows = [
        'Settings',
        'Windows Input Experience',
        'Windows Shell Experience Host',
        'Program Manager'
        ]

        # filter windows
        filtered_windows = []
        for window in windows:
            if window not in sys_windows and len(window) > 0:
                filtered_windows.append(window)
        
        print('windows checked')
        return filtered_windows

    def close_windows(filtered_windows): 
        for window in filtered_windows:
            while True:
                hwnd = win32gui.FindWindow(None, f'{window}') # gets handle of link media window
                if hwnd:
                    win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0) # posts msg to handle (hwnd) to close
                    print(f'{window} closed')
                    break

    def force_close_windows(filtered_windows):
        for window in filtered_windows:
            hwnd = win32gui.FindWindow(None, f'{window}')      # gets handle of link media window
            while hwnd:                                            # while the handle exists 
                hwnd = win32gui.FindWindow(None, f'{window}')         # checks to see if the window still exists                
                win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0) # posts close req to handle
                print(f'{window} closed')
                time.sleep(0.25) 

    def main():
        while True:
            filtered_windows = check_windows()
            if filtered_windows:
                close_windows(filtered_windows)
            else:
                break
            force_close_windows(filtered_windows)

    main()

# MAIN #

def main():
    ignore = ['Zen', 'Explorer', 'CapCut', 'Chrome']
    global paused
    while True:
        signal = startListener()
        #print(f"Signal received: {signal}")
        if signal == 'pause':
            if paused == False:
                paused = True
            else:
                paused = False
        elif paused == True:
            main()
        elif signal == "exit":
            print('Quitting')
            exit()
        elif signal == "shutdown":
            print('Shutting Down')
            if 'GlazeWM' in windows:
                os.startfile(r"C:\Users\Sweetwaters Church\Jordan\Scripts\WM-Exit\WM-Exit.cmd")
                while 'GlazeWM' in windows:
                    time.sleep(0.1)
            else:
                p.hotkey('win', 'd')
                time.sleep(1)
                p.rightClick(x=1823, y=66) # hide desktop icons
                #p.click(x=1704, y=86)
                p.click(find('view.jpg'))
                time.sleep(0.4)
                #p.click(x=1470, y=258)
                p.click(find('icons.jpg'))
            kill_all()
            exit()
        elif signal == 'reload':
            print('reloading config')
            os.system('start pyw main.py')
            exit()
            
        active_window = win32gui.GetForegroundWindow()
        title = win32gui.GetWindowText(active_window)
        
        if signal == "x1":
            print(f"Mouse 4 action triggered for {title}.")
            if any(ignore_string in title for ignore_string in ignore):
                continue
            if 'PowerPoint' in title:
                x1_powerpoint()
            elif 'ProPresenter' in title:
                x1_propresenter()
            elif 'Lightroom' in title:
                x1_lightroom()
            else:
                x1_spotify()

        elif signal == "x2":
            print("Mouse 5 action triggered.")
            if title in ignore:
                continue
            if 'PowerPoint' in title:
                x2_powerpoint()
            elif 'ProPresenter' in title:
                x2_propresenter
            elif 'Lightroom' in title:
                x2_lightroom()
            else:
                x2_spotify()

if __name__ == "__main__":
    main()