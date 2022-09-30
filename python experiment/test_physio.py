import webbrowser
import time
from pynput.keyboard import Key, Controller
keyboard = Controller()

webbrowser.open('http://127.0.0.1:8000/admin/login')
time.sleep(3)
keyboard.press(Key.tab)
time.sleep(3)
keyboard.type('admin@physio.com')
keyboard.press(Key.tab)
keyboard.type('12345678')
time.sleep(2)
keyboard.press(Key.enter)
time.sleep(3)
input("Press Enter to continue...")
# keyboard.press(Key.tab)
# keyboard.release(Key.tab)



