import os
import shutil
import pyautogui as p
import pyperclip
import time
import win32gui
import win32con
import subprocess
from datetime import datetime

TIMEOUT = 7

def close_terminal():
    win32gui.ShowWindow(win32gui.FindWindow(None, 'powershell'), win32con.SW_MINIMIZE)
    win32gui.ShowWindow(win32gui.FindWindow(None, r'C:\WINDOWS\system32\cmd.exe'), win32con.SW_MINIMIZE)
    win32gui.ShowWindow(win32gui.FindWindow(None, r'C:\WINDOWS\System32\WindowsPowerShell\v1.0\powershell.exe'), win32con.SW_MINIMIZE)
    win32gui.ShowWindow(win32gui.FindWindow(None, 'Main.py - Scripts - Visual Studio Code'), win32con.SW_MINIMIZE)
    win32gui.ShowWindow(win32gui.FindWindow(None, 'Windows PowerShell'), win32con.SW_MINIMIZE)

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

def paste(text):
    pyperclip.copy(text)
    p.hotkey('ctrl', 'v')

def move_sermon():
    sermon_day = 'pass'
    sermon_month = datetime.today().strftime('%m')
    found = False
    while sermon_day.isdigit() == False:
        sermon_day = input('What day was the sermon recorded? (Numbers only)\n').zfill(2)  
        if sermon_day == 'skip':
            return found

    close_terminal()

    # Settings
    videos_folder = r"C:\Users\Sweetwaters Church\Videos"
    sermon_folder = r"C:\Users\Sweetwaters Church\Jordan\Video Editing\Sermon"
    old_folder = r"C:\Users\Sweetwaters Church\Jordan\Video Editing\Sermon\old"
    filename_prefix = datetime.today().strftime(f'%Y-{sermon_month}-{sermon_day}') # Example output: 2025-04-16

    os.makedirs(old_folder, exist_ok=True)  # create the 'old' subfolder if it doesn't exist

    for file in os.listdir(sermon_folder):  # Move all files from 'sermon' to 'old'
        file_path = os.path.join(sermon_folder, file)
        if os.path.isfile(file_path):  # skip folders
            shutil.move(file_path, os.path.join(old_folder, file))
            print(f"Archived: {file}")

    # Find the file
    for file in os.listdir(videos_folder):
        if file.startswith(filename_prefix):
            videos_path = os.path.join(videos_folder, file)
            sermon_path = os.path.join(sermon_folder, file)
            sermon = shutil.move(videos_path, sermon_path)
            print(f"Moved: {file}")
            found = True
            break
    
    if not found:
        sermon_month = str(int(sermon_month) - 1).zfill(2)  # Subtract, convert, pad to 2 digits
        filename_prefix = f"{datetime.today().year}-{sermon_month}-{sermon_day}"
        for file in os.listdir(videos_folder):
            if file.startswith(filename_prefix):
                videos_path = os.path.join(videos_folder, file)
                sermon_path = os.path.join(sermon_folder, file)
                sermon = shutil.move(videos_path, sermon_path) 
                print(f"Moved: {file}")
                found = True
                break  
        else:
            print('File not found')
            move_sermon()
    return sermon

def edit_sermon(sermon):
    ILLEGAL_CHARACTERS = ['<', '>', ':', '"', '/', '\\', '|', '?', '*', '.']
    os.startfile(r"C:\Users\Sweetwaters Church\AppData\Local\CapCut\Apps\CapCut.exe")

    while True:
        hwndCapcutUpdate = win32gui.FindWindow(None, 'Version update')           # gets the handle for the version update window
        if hwndCapcutUpdate:                                                     # if the handle exists
            win32gui.PostMessage(hwndCapcutUpdate, win32con.WM_CLOSE, 0, 0)      # sends a close request
            print('CapCut Update Window Closed')
        cSermon = (find('cSermon.jpg', timeout=15))

        if cSermon == False:
            p.click(find('cSearch.jpg'))
            paste('sermon')
            cSermon = (find('cSermon.jpg'))

        if cSermon != False:
            p.click(cSermon[0] + 20, cSermon[1] - 20) # clicks using x + 20 (20px right) and y -20 (20px up)
            break
        else:
            input('WHERE IS THE SERMON </3\nCreate a Project titled "Sermon" and open it, then press enter')
            close_terminal()
            break

    START_TIME = time.time()

    while True:
        hwndLinkMedia = win32gui.FindWindow(None, 'Link media') # gets handle of link media window
        if hwndLinkMedia:
            win32gui.PostMessage(hwndLinkMedia, win32con.WM_CLOSE, 0, 0) # posts msg to handle (hwndLinkMedia) to close
            p.keyDown('ctrl')
            p.click(find('cMedia.jpg', timeout=5)) # click on missing media 
            p.keyUp('ctrl')
            time.sleep(0.3)
            p.press('backspace')
            p.press('enter')
            break

        if time.time() - START_TIME > TIMEOUT:
            print('Link media window not found, timed out')
            break
        time.sleep(0.25)

    time.sleep(0.5)
    print('Importing Sermon to CapCut')
    p.hotkey('ctrl', 'f') # fullscreen capcut 

    cImport = find('cImport.jpg', 8)
    if cImport:
        p.click(cImport)
    
    #p.hotkey('ctrl', 'i') # import
    if sermon != False: # checks if there is a sermon path to type
        time.sleep(0.8)
        paste(sermon) # sermon = "C:\\Users\\Sweetwaters Church\\Documents\\Jordan's Desktop\\Documents\\Video Editing\\Sermon\\2025-05-21 07-27-41.mp4"
        p.press('enter')
        print('Import Successful')

    podcast_name = input('What is the name of this weeks podcast? (Enter when ready to export, with CapCut maximized)\n')
    podcast_path_name = podcast_name

    for char in ILLEGAL_CHARACTERS:
        podcast_path_name = podcast_path_name.replace(char, '')

    close_terminal()

    base_path = r"C:\Users\Sweetwaters Church\Jordan\Podcast Editing"
    podcast_folder = os.path.join(base_path, podcast_path_name)          # base_path = "C:\\Users\\Sweetwaters Church\\Documents\\Jordan's Desktop\\Documents\\Podcast Editing", podcast_name = 'test 5'
    os.makedirs(podcast_folder, exist_ok=True)                              # make the "C:\Users\Sweetwaters Church\Documents\Jordan's Desktop\Documents\Podcast Editing\Podcast Name" folder from the variable podcast_folder
    print(f"Folder created at: {podcast_folder}")                   # podcast_folder = "C:\\Users\\Sweetwaters Church\\Documents\\Jordan's Desktop\\Documents\\Podcast Editing\\test 5"

    p.press('esc')
    p.hotkey('ctrl', 'e') # export

    time.sleep(0.5)
    cName = find('cName.jpg')
    p.click(cName[0] + 100, cName[1]) # click name
    time.sleep(0.5)
    p.hotkey('ctrl', 'a') # select all
    paste(podcast_path_name) # type podcasts name
    time.sleep(1.5)

    cVideoChecked = find('cVideoChecked.jpg')
    x1, y1 = int(cVideoChecked[0] + 8), int(cVideoChecked[1] + 8)
    if p.pixel(x1, y1) == (0, 193, 205):
        p.click(x1, y1)

    cAudioUnchecked = find('cAudioUnchecked.jpg')
    x1, y1 = int(cAudioUnchecked[0] + 8), int(cAudioUnchecked[1] + 8)
    if p.pixel(x1, y1) == (81, 81, 81):
        p.click(x1, y1)
    
    p.click(find('cExportpath.jpg')) # click export to
    time.sleep(4)
    paste(podcast_folder) # type export path
    time.sleep(3)
    p.press('enter')       # confirm path
    time.sleep(1.5)
    p.press('enter')       # confirm path
    time.sleep(1.5)
    p.press('enter')       # export

    podcast_path = os.path.join(podcast_folder, f'{podcast_path_name}.WAV')
    print('waiting for audio file to export...')
    find('cAudioExported.jpg') # pauses the script till it sees capcuts 'audio exported' message
    p.press('esc')
    
    hwndCapcut = win32gui.FindWindow(None, 'CapCut')      # gets handle of link media window
    while hwndCapcut:                                            # while the handle exists 
        hwndCapcut = win32gui.FindWindow(None, 'CapCut')         # checks to see if the window still exists                
        win32gui.PostMessage(hwndCapcut, win32con.WM_CLOSE, 0, 0) # posts close req to handle
        time.sleep(0.25)                                     # delay

    return podcast_path, podcast_path_name, podcast_name, podcast_folder

def edit_podcast(podcast_path, podcast_path_name, podcast_folder):
    # levelator
    print('Starting Levelator')
    os.startfile(r"C:\Program Files (x86)\Levelator\levelator.exe")
    p.doubleClick(find('lLogo.jpg'))

    time.sleep(0.4)
    paste(podcast_path)
    time.sleep(2.5)
    p.press('enter')

    base, ext = os.path.splitext(podcast_path)  # distiguishes between the path and .WAV extention
    output_path = base + ".output" + ext        # determines the levelators outputs path

    print("waiting for Levelator to finish...") 
    while not os.path.exists(output_path):      # while the output path doesnt exist, wait
        time.sleep(1)
    time.sleep(5) # i just added this to check if it needs some delay after export ##############
    print(f"Levelator done: {output_path}")

    START_TIME = time.time()
    print('Attempting to close Levelator')
    while True:
        hwndLevelator = win32gui.FindWindow(None, 'Levelator')
        if hwndLevelator:
            win32gui.PostMessage(hwndLevelator, win32con.WM_CLOSE, 0, 0)
            print('Levelator Closed')
            break

        if time.time() - START_TIME > TIMEOUT:
            print('Levelator Already Closed (timed out)')
            break

    # audacity
    print('Starting Audacity')
    os.startfile(r"C:\Program Files\Audacity\Audacity.exe") # open audacity 

    while True:
        hwndAudacity = win32gui.FindWindow(None, 'Audacity')
        if hwndAudacity:
            win32gui.ShowWindow(hwndAudacity, win32con.SW_MAXIMIZE) # maximizes audacity
            break


    p.click(find('aSkip.jpg', 5.5))

    p.hotkey('ctrl', 'shift', '1') # import intro

    p.hotkey('ctrl', 'shift', '2') # import sermon
    time.sleep(0.1)
    paste(f'{output_path}')
    time.sleep(0.1)
    p.press('enter')
    find('aImported.jpg')

    p.hotkey('ctrl', 'shift', '3') # import outro
    print(f'{output_path}')

    input('Press "Enter" when ready to export...')
    close_terminal()

    # AUDACITY EXPORT 

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

    paste(podcast_path_name)

    p.click(locs[0]) # clicks path
    p.hotkey('ctrl', 'a') 
    paste(podcast_folder)
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
    time.sleep(0.5)
    paste('Tags.xml') # types path to tags
    time.sleep(1) 
    p.press('enter') # enters tags
    p.click(find('aTitle.jpg')) # click title
    paste(podcast_path_name) # types title
    time.sleep(0.2)
    p.press('enter', presses=2)

    input('Press "Enter" as soon as export is finished\n(Make sure audacity is still maximized :)')
    close_terminal()

    p.hotkey('ctrl', 's')
    time.sleep(0.5)
    paste(f'{podcast_path}')
    time.sleep(0.5)
    p.press('enter')
    time.sleep(1)

    win32gui.PostMessage(hwndAudacity, win32con.WM_CLOSE, 0, 0) # closes audacity (hopefully)
    
def upload_podcast(podcast_path, podcast_name):
    podcast_path = podcast_path.replace('.WAV', '.mp3')
    subprocess.Popen([r"C:\Program Files\Google\Chrome\Application\chrome.exe", '--profile-directory=Profile 1', "https://my.captivate.fm/dashboard/podcast/ecba26e9-60c0-4f28-8296-283396927907/episode/c73ff28c-368b-4315-aeff-16e82688f4db"])

    p.click(find('bDetails.jpg'))
    p.hotkey('ctrl', 'a')
    p.hotkey('ctrl', 'c')
    p.click(find('bCreate.jpg'))
    p.click(find('bUpload.jpg'))
    time.sleep(1.5)
    paste(f"{podcast_path}")
    time.sleep(2.5)
    p.press('enter')
    time.sleep(0.5)
    p.click(find('bTitle.jpg'))
    paste(f'{podcast_name}')
    time.sleep(1)
    p.scroll(-200)
    p.click(find('bDetailArea.jpg'))
    p.hotkey('ctrl', 'v')
    p.scroll(-10000)


def main():
    sermon_path = move_sermon()
    podcast_path, podcast_path_name, podcast_name, podcast_folder = edit_sermon(sermon_path)
    edit_podcast(podcast_path, podcast_path_name, podcast_folder)
    upload_podcast(podcast_path, podcast_name)
    
main()

input('enter to end')
print('Complete!')
