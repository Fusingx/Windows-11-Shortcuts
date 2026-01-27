import os
import win32gui
import win32con
import time
import pygetwindow as gw
from pynput import keyboard
import subprocess

# --- GLOBALS ---
windows = gw.getAllTitles()
active_window = win32gui.GetForegroundWindow()
title = win32gui.GetWindowText(active_window)
alt_mode = False
current_modifiers = set()
button_signal = None
listener_running = True

alt_combos = {
    'ctrl+p': 'pause'
}

# --- Keyboard handlers ---
def on_key_press(key):
    global alt_mode, button_signal, listener_running

    # Track modifier
    if key in (keyboard.Key.ctrl, keyboard.Key.ctrl_l, keyboard.Key.ctrl_r):
            current_modifiers.add('ctrl')
    elif key in (keyboard.Key.alt, keyboard.Key.alt_l, keyboard.Key.alt_r):
        alt_mode = True
        return

    # Check Alt-mode combos
    elif alt_mode:
        combo = ''
        if 'ctrl' in current_modifiers:
            combo += 'ctrl+'

        try:
            # Use vk to get the raw character even if Ctrl/Alt are held
            if hasattr(key, 'vk') and key.vk is not None:
                # Standardize to lowercase character
                char = chr(key.vk).lower() if 65 <= key.vk <= 90 else key.char.lower()
                combo += char
            else:
                combo += key.char.lower()
        except AttributeError:
            if key == keyboard.Key.enter:
                combo += 'enter'
            else:
                combo += str(key).replace('Key.', '')

        if combo in alt_combos:
            button_signal = alt_combos[combo]
            listener_running = False
            print(f"Alt-Ctrl combo triggered: {button_signal}")


def on_key_release(key):
    global alt_mode
    if key in (keyboard.Key.ctrl, keyboard.Key.ctrl_l, keyboard.Key.ctrl_r):
        current_modifiers.discard('ctrl')
    if key in (keyboard.Key.alt, keyboard.Key.alt_l, keyboard.Key.alt_r):
        alt_mode = False

# --- Listener starter ---
def startListener():
    global button_signal, listener_running

    button_signal = None
    listener_running = True

    # Start keyboard listener
    keyboard_listener = keyboard.Listener(
        on_press=on_key_press,
        on_release=on_key_release
    )
    keyboard_listener.start()

    print("Listening (Alt-mode)...")
    while listener_running:
        time.sleep(0.01)

    keyboard_listener.stop()
    keyboard_listener.join()

    print(f"Listener stopped, returning signal: {button_signal}")
    return button_signal

# --- 7. MAIN LOOP ---

def main():
    while True:
        signal = startListener()
        if signal == 'pause': # alt ctrl p
            win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, r"C:\Users\Sweetwaters Church\Pictures\wallpaper2.png", 1+2)
            subprocess.Popen(
            ["pythonw", "main.py"],
            cwd=r"C:\Users\Sweetwaters Church\Jordan\Scripts\Shortcuts"
            )
            exit()


if __name__ == "__main__":
    main()