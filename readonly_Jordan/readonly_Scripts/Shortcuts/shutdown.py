import os
import time

timeout = 1
time.sleep(0.5)
start = time.time()
while time.time() - start < timeout:
    print('Shutting Down in: 5 Seconds')
    time.sleep(0.05)
start = time.time()
while time.time() - start < timeout:
    print('Shutting Down in: 4 Seconds')
    time.sleep(0.05)
start = time.time()
while time.time() - start < timeout:
    print('Shutting Down in: 3 Seconds')
    time.sleep(0.05)
start = time.time()
while time.time() - start < timeout:
    print('Shutting Down in: 2 Seconds')
    time.sleep(0.05)
start = time.time()
while time.time() - start < timeout:
    print('Shutting Down in: 1 Seconds')
    time.sleep(0.05)
start = time.time()
while time.time() - start < timeout:
    print(f'\033[{31}mSHUTTING DOWN\033[0m') # red
    time.sleep(0.05)
os.system("shutdown /s /f /t 0")