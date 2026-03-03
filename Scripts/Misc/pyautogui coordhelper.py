import pyautogui as p
import time

while True:
    pos = p.position()
    x, y = pos     
    print(f'({x}, {y}) is {p.pixel(x, y)}')

# (1095, 350) is (255, 255, 255) NAME
# (1055, 364) is (255, 255, 255) EXPORT PATH
# (1095, 415) is (229, 241, 251) FORMAT
# DOWN DOWN ENTER
# (947, 471) is (255, 255, 255) STEREO
# (1055, 502) is (229, 241, 251) SAMPLE RATE
# PRESS DOWN 8 TIMES THEN ENTER
# (1055, 535) is (224, 235, 245) BIT RATE MODE
# UP 3 TIMES ENTER
# (1055, 567) is (225, 236, 246) QUALITY
# 3 UP 1 DOWN ENTER
# (884, 617) is (255, 255, 255) ENTIRE PROJECT
# (773, 741) is (90, 0, 56) META DATA
# (964, 630) is (224, 238, 249) LOAD
# TYPE 'Tags.xml' ENTER
# (1095, 430) is (255, 255, 255) TRACK TITLE
# TYPERIGHT {PODCAST TITLE} ENTER ENTER
# ENTER

# (0, 193, 205) capcut blue
# (81, 81, 81) capcut unchecked grey