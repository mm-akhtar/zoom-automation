import time
from datetime import datetime
from pynput.keyboard import Controller, Key
from data import lst
import webbrowser

import keyboard

isStarted=False

for i in lst:
    while True:
        if isStarted == False:
            if datetime.now().hour == int(i[1].split(':')[0]) and datetime.now().minute == int(i[1].split(':')[1]):
                webbrowser.open(i[0])
                isStarted = True
        elif isStarted == True:
            if datetime.now().hour == int(i[2].split(':')[0]) and datetime.now().minute == int(i[2].split(':')[1]):
                keyboard.press_and_release('shift+w, space')
                time.sleep(1)
                keyboard.press(enter)
                isStarted = False
                break


smds