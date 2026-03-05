import pyautogui as p
import os
import time
import win32gui
import win32con
import math

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def test():
    podcastName = 'Unlocked Part 1'
    path = r"C:\Users\Sweetwaters Church\Documents\Jordan's Desktop\Documents\Podcast Editing\Unlocked Part 1"

    def find(element):
        while True:
            try:
                coord = p.locateOnScreen(f'{element}', confidence=0.8)
            except:
                p.ImageNotFoundException
            if coord:
                break
        return coord



    apics = ['aExportpath.jpg', 'aFormat.jpg', 'aStereo.jpg', 'aSamplerate.jpg', 'aBitrate.jpg', 'aQuality.jpg', 'aEntireproject.jpg', 'aMetadata.jpg',]
    locs = ['', '', '', '', '', '', '', '']

    def distanceCheck():
        input('press enter for start')

        one = p.position()
        print(f'one = {one}')


        input('press enter for end')

        two = p.position()
        print(f'two = {two}')

        print('\n \n')

        dx = two.x - one.x
        dy = two.y - one.y

        print(f'\nΔx = {dx}, Δy = {dy}') # idk

        distance = math.hypot(dx, dy) # idk
        print(f'Distance = {distance:.2f} pixels') # idk

    def find_coord(loc, jpg):
        while loc == '':
            try:
                loc = p.locateOnScreen(f'{jpg}', confidence=0.8)
            except:
                p.ImageNotFoundException
        return loc

    p.hotkey('ctrl', 'shift', 'e')
    time.sleep(0.2)
    p.typewrite(podcastName)

    for i in range(len(apics)):
        locs[i] = find_coord(locs[i], apics[i])
        print(locs[i])
        print(apics[i])

    p.click(locs[0])
    p.hotkey('ctrl', 'a')
    p.typewrite(path)
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
    p.typewrite(podcastName) # types title
    time.sleep(0.2)
    p.press('enter', presses=2)

def close_terminal(): 
    win32gui.ShowWindow(win32gui.FindWindow(None, r'C:\WINDOWS\system32\cmd.exe'), win32con.SW_MINIMIZE)
    win32gui.ShowWindow(win32gui.FindWindow(None, 'test3.py - Podcast - Visual Studio Code'), win32con.SW_MINIMIZE)


service = Service(executable_path="chromedriver.exe")

options = Options()
options.add_argument(r"--user-data-dir=C:/Users/Sweetwaters Church/AppData/Local/Google/Chrome/User Data") 
options.add_argument(r'--profile-directory=Profile 1') 

driver = webdriver.Chrome(service=service, options=options)

#driver.get('https://my.captivate.fm/dashboard/podcast/ecba26e9-60c0-4f28-8296-283396927907/episode/89556437-904c-477e-8371-8e0972d1486b')


p.typewrite('https://my.captivate.fm/dashboard/podcast/ecba26e9-60c0-4f28-8296-283396927907/episode/89556437-904c-477e-8371-8e0972d1486b')

time.sleep(5)

#while True:
#    try:
#        devo_link_element = driver.find_element(By.CSS_SELECTOR, "a[href*='devo']")
#        devo_link = devo_link_element.get_attribute('href')
#        print(devo_link)
#        break
#    except:
#        pass
input('press enter to end')

driver.quit()


driver.find_element