import random
import pyautogui
import time

pyautogui.FAILSAFE = True
print("To exit, move mouse to top left corner of screen")
# print(pyautogui.size())
counter = 0
num = int(input("Movement Time (10 is roughly 1 minute of movement -> set to 500):"))
while counter != num:
    x = random.randint(0, 1920)
    y = random.randint(0, 1080)
    time.sleep(5)
    pyautogui.moveTo(x, y, duration=1)
    pyautogui.scroll(10)
    counter += 1
    print(counter)
