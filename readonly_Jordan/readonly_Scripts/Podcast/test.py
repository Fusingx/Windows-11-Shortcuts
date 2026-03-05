import os
import shutil
import pyautogui as p
import pyperclip
import time
import win32gui
import win32con
import subprocess
import requests
from datetime import datetime

# GLOBALS
CONFIG = {
    "videos_folder": r"C:\Users\Sweetwaters Church\Videos",
    "sermon_folder": r"C:\Users\Sweetwaters Church\Jordan\Video Editing\Sermon",
    "old_folder": r"C:\Users\Sweetwaters Church\Jordan\Video Editing\Sermon\old",
    "podcast_editing_dir": r"C:\Users\Sweetwaters Church\Jordan\Podcast Editing",
    "illegal_characters": ['<', '>', ':', '"', '/', '\\', '|', '?', '*', '.'],
    "images_dir": os.path.join(os.path.dirname(os.path.realpath(__file__)), "images"),
    "paths": {
        "capcut": r"C:\Users\Sweetwaters Church\AppData\Local\CapCut\Apps\CapCut.exe",
        "levelator": r"C:\Program Files (x86)\Levelator\levelator.exe",
        "audacity": r"C:\Program Files\Audacity\Audacity.exe",
        "chrome": [r"C:\Program Files\Google\Chrome\Application\chrome.exe", '--profile-directory=Profile 1', "https://my.captivate.fm/dashboard/podcast/ecba26e9-60c0-4f28-8296-283396927907/episode/c73ff28c-368b-4315-aeff-16e82688f4db"]
    },
}
TIMEOUT = 7

# HELPER FUNCTIONS

def close_terminal():
    # win32gui.ShowWindow(win32gui.FindWindow(None, 'powershell'), win32con.SW_MINIMIZE)
    # win32gui.ShowWindow(win32gui.FindWindow(None, r'C:\WINDOWS\system32\cmd.exe'), win32con.SW_MINIMIZE)
    # win32gui.ShowWindow(win32gui.FindWindow(None, r'C:\WINDOWS\System32\WindowsPowerShell\v1.0\powershell.exe'), win32con.SW_MINIMIZE)
    # win32gui.ShowWindow(win32gui.FindWindow(None, 'Main.py - Scripts - Visual Studio Code'), win32con.SW_MINIMIZE)
    win32gui.ShowWindow(win32gui.FindWindow(None, 'Windows PowerShell'), win32con.SW_MINIMIZE)

def find(image, timeout=6.0):
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
    print('timed out')
    return None

def paste(text):
    pyperclip.copy(text)
    p.hotkey('ctrl', 'v')



# --- 1. CONFIGURATION ---
USER_ID = "d6cae549-cf77-4170-b0c2-d3d6f56769a8"
API_TOKEN = "vZKJqmGOXEWScIdja21MZWY9Senl7IydMkSYdqLz"
SHOW_ID = "b68e53de-e6cb-5d71-b24a-e761c915b3b1"
MP3_FILE_PATH = r"C:\Users\Sweetwaters Church\Jordan\Podcast Editing\The Kings Move Part 1\The Kings Move Part 1.mp3"
EPISODE_TITLE = "Sunday Service - Sweetwaters Full Gospel Church"

# Use the clean API base
API_BASE = "https://api.captivate.fm"

def main():
    # --- 2. AUTHENTICATION ---
    print("Authenticating...")
    # Auth is global, not show-specific
    auth_res = requests.post(
        f"{API_BASE}/authenticate/token",
        data={"username": USER_ID, "token": API_TOKEN}
    )
    
    if auth_res.status_code != 200:
        print(f"Auth Failed: {auth_res.text}")
        return
        
    token = auth_res.json().get("token")
    headers = {"Authorization": f"Bearer {token}"}
    print("Authentication Successful.")

    # --- 3. UPLOAD MEDIA FILE ---
    print(f"Uploading {MP3_FILE_PATH}...")
    # Media upload requires the Show ID in the path
    with open(MP3_FILE_PATH, "rb") as audio:
        upload_res = requests.post(
            f"{API_BASE}/shows/{SHOW_ID}/media", 
            headers=headers,
            files={"file": audio}
        )
    
    if upload_res.status_code not in [200, 201]:
        print(f"Upload Failed: {upload_res.text}")
        return

    # Extract Media ID from the response
    media_id = upload_res.json().get("id")
    print(f"Media uploaded successfully. Media ID: {media_id}")

    # --- 4. CREATE EPISODE ---
    # NOTE: If you leave 'shownotes' out of this dictionary, 
    # Captivate will apply your default template automatically.
    episode_data = {
        "show_id": SHOW_ID,
        "title": EPISODE_TITLE,
        "media_id": media_id,
        "status": "draft" 
    }

    print("Creating episode draft...")
    publish_res = requests.post(
        f"{API_BASE}/shows/{SHOW_ID}/episodes", 
        headers=headers, 
        json=episode_data
    )

    if publish_res.status_code in [200, 201]:
        print("🎉 Success! Your episode is in your Captivate Drafts.")
    else:
        print(f"Publishing Failed: {publish_res.text}")

if __name__ == "__main__":
    main()


# def main():
#     sermon_path = move_sermon()
#     podcast_path, podcast_path_name, podcast_name, podcast_folder = edit_sermon(sermon_path)
#     edit_podcast(podcast_path, podcast_path_name, podcast_folder)
#     upload_podcast(podcast_path, podcast_name)

if __name__ == "__main__":
    main()
    input('Complete!')
    exit()
