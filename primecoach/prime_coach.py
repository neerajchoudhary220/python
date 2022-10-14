import os,time
from pynput.keyboard import Key, Controller
class primecoach:
    def open():
        path = r"Invoke-Expression&'D:\prime coach\prime-coach-backend'"
        os.system("code "+path)
        print("Prime Coach is opening with vs code")
    def run():
        Keyboard = Controller()
        os.startfile('cmd')
        time.sleep(2)
        Keyboard.type('cd D:\prime coach\prime-coach-backend')
        Keyboard.press(Key.enter)
        Keyboard.release(Key.enter)
        Keyboard.type('php artisan ser')
        Keyboard.press(Key.enter)
        Keyboard.release(Key.enter)

