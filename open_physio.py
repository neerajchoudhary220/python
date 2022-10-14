import os,time
from pynput.keyboard import Key, Controller
Keyboard = Controller()
# os.system('cd D:\physio-backend')
os.startfile('cmd')
time.sleep(2)
Keyboard.type('cd D:\physio-backend')
Keyboard.press(Key.enter)
Keyboard.release(Key.enter)
Keyboard.type('php artisan ser')
Keyboard.press(Key.enter)
Keyboard.release(Key.enter)

print("Physio is opened")