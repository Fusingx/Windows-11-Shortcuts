import pyautogui as p
import time

def find(element):
    while True:
        try:
            coord = p.locateOnScreen(f'{element}', confidence=0.8)
            if coord:
                return coord
        except:
            p.ImageNotFoundException

time.sleep(5)

for i in range(31):
    p.click(find('target.jpg'))
