from cmath import e
import os
import time
import json
import webbrowser
from tkinter import E
from pynput.keyboard import Key, Controller
Keyboard = Controller()
print("1.   Check The Php Version")
print("2.   Run Physio")
print("3.   Change System Php version with 8.1.6")
print("4.   Change System Php version with 7.4.0")
print("5.   Open Physio")
print("6.   Run Prime Coach")
print("7.   Open Prime Coach")
print("8.   Run Laravel Project")

with open('my.json') as f:
    data = json.load(f)
def get_url(name):
    return data['url'][name]

def get_folderPath(name):
   return data['folder_path'][name].replace('/','\\')

def open_vs_with(path):
    os.startfile('cmd')
    time.sleep(3)
    Keyboard.type(path)
    time.sleep(2)
    Keyboard.press(Key.enter)
    Keyboard.release(Key.enter)
    Keyboard.type('cls')
    Keyboard.press(Key.enter)
    Keyboard.release(Key.enter)
    Keyboard.type('code .')
    Keyboard.press(Key.enter)
    Keyboard.release(Key.enter)

def run_laravel_project(folder_path, home_page):
    os.startfile('cmd')
    time.sleep(2)
    Keyboard.type('cd '+folder_path)
    Keyboard.press(Key.enter)
    Keyboard.release(Key.enter)
    Keyboard.type('cls')
    Keyboard.press(Key.enter)
    Keyboard.release(Key.enter)
    Keyboard.type('php artisan ser')
    Keyboard.press(Key.enter)
    Keyboard.release(Key.enter)
    path = data['chrome']+' %s'
    url = home_page
    webbrowser.get(path).open(url)



n = input()
if n == '1':
    os.system('php -v')

#Run physio
if n == '2':
    run_laravel_project('D:\My_laravel\physio-backend','http://127.0.0.1:8000/admin/login')
if n == '3':
    os.startfile('cmd')
    time.sleep(2)
    Keyboard.type('rundll32.exe sysdm.cpl,EditEnvironmentVariables')
    Keyboard.press(Key.enter)
    Keyboard.release(Key.enter)
    time.sleep(2)
    Keyboard.press('p')
    Keyboard.release('p')
    time.sleep(2)
    with Keyboard.pressed(Key.alt):
        Keyboard.press('e')
        Keyboard.release('e')
    time.sleep(2)
    with Keyboard.pressed(Key.alt):
        Keyboard.press('e')
        Keyboard.release('e')
    Keyboard.type(r'C:\xampp\php')
    time.sleep(2)
    Keyboard.press(Key.enter)
    Keyboard.release(Key.enter)
    Keyboard.press(Key.enter)
    Keyboard.release(Key.enter)
    Keyboard.press(Key.enter)
    Keyboard.release(Key.enter)
    time.sleep(2)
    print('Now you system php version is 8.1.6 You can check by "php -v" command also')


if n == '4':
    os.startfile('cmd')
    time.sleep(2)
    Keyboard.type('rundll32.exe sysdm.cpl,EditEnvironmentVariables')
    Keyboard.press(Key.enter)
    Keyboard.release(Key.enter)
    time.sleep(2)
    Keyboard.press('p')
    Keyboard.release('p')
    time.sleep(2)
    with Keyboard.pressed(Key.alt):
        Keyboard.press('e')
        Keyboard.release('e')
    time.sleep(2)
    with Keyboard.pressed(Key.alt):
        Keyboard.press('e')
        Keyboard.release('e')
    Keyboard.type(r'C:\wamp64\bin\php\php7.4.0')
    time.sleep(2)
    Keyboard.press(Key.enter)
    Keyboard.release(Key.enter)
    Keyboard.press(Key.enter)
    Keyboard.release(Key.enter)
    Keyboard.press(Key.enter)
    Keyboard.release(Key.enter)
    time.sleep(2)
    print('Now you system php version is 7.4.0 You can check by "php -v" command also')
#open physio
if n=='5':
   open_vs_with("D:\My_laravel\physio-backend")
#run prime coach
if n=='6':
    run_laravel_project('D:\prime coach\prime-coach-backend','http://127.0.0.1:8000/')
#open prime coach
if n=='7':
    folder = get_folderPath('prime_coach')
    open_vs_with(folder)
if n=='8':
    print('\r Project List:\r')
    print('\r physio')
    print('\r prime_coach')
    print('\n Enter Your Project Name...')
    project = input()
    folder_path = get_folderPath(project)
    home_page = get_url(project)
    run_laravel_project(folder_path,home_page)


    