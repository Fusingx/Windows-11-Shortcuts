import pyautogui as p
import time
import win32con
import win32gui
import os
import subprocess
import yt_dlp
import ffmpeg

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

print('s')

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
                return False

def test():
    p.press('esc')
    p.hotkey('ctrl', 'e') # export

    time.sleep(0.5)
    p.click(p.locateOnScreen('cName.jpg', confidence=0.8)) # click name
    p.hotkey('ctrl', 'a') # select all
    p.typewrite('podcast_name') # type podcasts name
    time.sleep(0.5)

    cVideoChecked = p.locateOnScreen('cVideoChecked.jpg', confidence=0.8)
    x1, y1 = int(cVideoChecked[0] + 8), int(cVideoChecked[1] + 8)
    if p.pixel(x1, y1) == (0, 193, 205):
        p.click(x1, y1)

    cAudioUnchecked = p.locateOnScreen('cAudioUnchecked.jpg', confidence=0.8)
    x1, y1 = int(cAudioUnchecked[0] + 8), int(cAudioUnchecked[1] + 8)
    if p.pixel(x1, y1) == (81, 81, 81):
        p.click(x1, y1)
    
    p.click(p.locateOnScreen('cExportpath.jpg', confidence=0.8)) # click export to
    time.sleep(1)
    p.typewrite(r"C:\Users\Sweetwaters Church\Documents\Jordan's Desktop\command\Podcast") # type export path
    time.sleep(1)
    p.press('enter')       # confirm path
    time.sleep(1)
    p.press('enter')       # confirm path
    time.sleep(1)
    p.press('enter')       # export
    print('waiting for audio file to export...')

def test3():
    podcast_name = 'Unlocked Part 1'
    podcast_path = r"C:\Users\Sweetwaters Church\Documents\Jordan's Desktop\Documents\Podcast Editing\Unlocked Part 1"

    return podcast_name, podcast_path

def test2(podcast_name, podcast_path):
    apics = ['aExportpath.jpg', 'aFormat.jpg', 'aStereo.jpg', 'aSamplerate.jpg', 'aBitrate.jpg', 'aQuality.jpg', 'aEntireproject.jpg', 'aMetadata.jpg',]
    locs = ['', '', '', '', '', '', '', '']

    def find_coord(loc, jpg):
        while loc == '':
            try:
                loc = p.locateOnScreen(f'{jpg}', confidence=0.8)
            except:
                p.ImageNotFoundException
        return loc

    p.press('esc')
    p.hotkey('ctrl', 'shift', 'e')

    for i in range(len(apics)):
        locs[i] = find_coord(locs[i], apics[i])
        print(locs[i])
        print(apics[i])

    p.typewrite(podcast_name)

    p.click(locs[0]) # clicks path
    p.hotkey('ctrl', 'a') 
    p.typewrite(podcast_path)
    time.sleep(0.4)

    p.click(locs[1][0] + 100, locs[1][1]) # format
    for i in range(12):
        p.press('up')
    p.press(['down', 'down', 'enter']) # enter format

    p.click(locs[2]) # click stereo

    p.click(locs[3][0] + 150, locs[3][1] + 15) # click sample rate
    p.press('down', presses=8) # set sample rate
    p.press('enter') # confirm

    p.click(locs[4][0] + 150, locs[4][1] + 15) # click bitrate mode
    p.press(['up', 'up', 'up', 'enter']) # set bitrate mode

    p.click(locs[5][0] + 150, locs[5][1] + 15) # click quality
    p.press(['up', 'up', 'up', 'down', 'enter']) # set quality

    p.click(locs[6]) # click entire project

    p.click(locs[7]) # click meta data
    p.click(find('aLoad.jpg')) # clicks load
    p.typewrite('Tags.xml') # types path to tags
    time.sleep(0.2) 
    p.press('enter') # enters tags
    p.click(find('aTitle.jpg')) # click title
    p.typewrite(podcast_name) # types title
    time.sleep(0.2)
    p.press('enter', presses=2)

    input('Press "Enter" when ready to upload')

def test4():
    while True:
        hwndCapcutUpdate = win32gui.FindWindow(None, 'Version update')           # gets the handle for the version update window
        if hwndCapcutUpdate:                                                     # if the handle exists
            win32gui.PostMessage(hwndCapcutUpdate, win32con.WM_CLOSE, 0, 0)      # sends a close request

        cSermon = (find('cSermon.jpg'))
        p.click(cSermon[0] + 20, cSermon[1] - 20) # clicks using x + 20 (20px right) and y -20 (20px up)
        break

def test5():
    p.hotkey('ctrl', 's')
    time.sleep(0.5)
    p.typewrite(r"C:\Users\Sweetwaters Church\Documents\Jordan's Desktop\Documents\Podcast Editing\Unlocked The Door of Boldness\Unlocked The Door of Boldness.WAV")
    time.sleep(0.5)
    p.press('enter')

    while True:
        if hwndAudacity:
            win32gui.PostMessage(hwndAudacity, win32con.WM_CLOSE, 0, 0) # closes audacity
            break

    while True:
        hwndAudacity = win32gui.FindWindow(None, 'Audacity')
        if hwndAudacity:
            print('hwnd found')
            break
    input('enter to continue')

    win32gui.ShowWindow(hwndAudacity, win32con.SW_RESTORE)

    time.sleep(5)

    win32gui.PostMessage(hwndAudacity, win32con.WM_CLOSE, 0, 0) # closes audacity

def test6():
    # audacity
    print('Starting Audacity')
    os.startfile(r"C:\Program Files\Audacity\Audacity.exe") # open audacity 

    while True:
        hwndAudacity = win32gui.FindWindow(None, 'Audacity')
        if hwndAudacity:
            win32gui.ShowWindow(hwndAudacity, win32con.SW_MAXIMIZE) # maximizes audacity
            break

    p.hotkey('ctrl', 'shift', '1') # import intro

    p.hotkey('ctrl', 'shift', '2') # import sermon
    time.sleep(0.1)
    p.typewrite(f'path')
    time.sleep(0.1)
    p.press('enter')
    time.sleep(1)

    p.hotkey('ctrl', 'shift', '3') # import outro

def test7():
    print('Starting Audacity')
    os.startfile(r"C:\Program Files\Audacity\Audacity.exe") # open audacity 

    while True:
        hwndAudacity = win32gui.FindWindow(None, 'Audacity')
        if hwndAudacity:
            win32gui.ShowWindow(hwndAudacity, win32con.SW_MAXIMIZE) # maximizes audacity
            break

    p.hotkey('ctrl', 'shift', '1') # import intro

    p.hotkey('ctrl', 'shift', '2') # import sermon
    time.sleep(0.1)
    p.typewrite(r"C:\Users\Sweetwaters Church\Documents\Jordan's Desktop\Documents\Podcast Editing\Unlocked The Sound of the Spirit\Unlocked The Sound of the Spirit.output.WAV")
    time.sleep(0.1)
    p.press('enter')
    

    p.hotkey('ctrl', 'shift', '3') # import outro

def test8():
    cName = find('cName.jpg')
    p.click(cName[0] + 100, cName[1]) # click name

time.sleep(1)

media = find('cMedia.jpg', 4)
if media:
    print('good')
else:
    print('not good')