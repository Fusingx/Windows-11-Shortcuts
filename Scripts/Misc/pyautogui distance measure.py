import pyautogui as p
import math

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


while True:
    distanceCheck()