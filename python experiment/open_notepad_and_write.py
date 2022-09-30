import os
import time
from pynput.keyboard import Key, Controller
keyboard = Controller()
print("notepad opening...")
time.sleep(2)
os.startfile('notepad.exe')
time.sleep(2)
keyboard.type('Welcome mr neeraj choudhary')






