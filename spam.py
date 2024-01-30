import pyautogui as py
import time as t


for i in range(1000):
    py.hotkey('ctrl', 'v') 
    py.press('Enter')

    t.sleep(0.1)

