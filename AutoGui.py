import pyautogui
import time
time.sleep(4)
minValue = 1
maxValue = 10000
count = 0

while count <= maxValue:
    pyautogui.typewrite("Is there bread?")
    pyautogui.press("enter")
    count += 1

"""
AutoGui is includes mouse control,keyboard control,message box and screenshot functions.
Read the docs https://pyautogui.readthedocs.io/en/latest/quickstart.html#
installition
python
node
npm
npm install pyautogui
"""
