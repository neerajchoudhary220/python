import os,time
from pynput.keyboard import Key, Controller
class physio:
    def open():
        os.system("code D:\physio-backend")
        print("Physio is opened with VS Code")
    def run():
        Keyboard = Controller()
        os.startfile('cmd')
        time.sleep(2)
        Keyboard.type('cd D:\physio-backend')
        Keyboard.press(Key.enter)
        Keyboard.release(Key.enter)
        Keyboard.type('php artisan ser')
        Keyboard.press(Key.enter)
        Keyboard.release(Key.enter)
