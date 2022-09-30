import subprocess,os
from datetime import datetime
now = datetime.now()
current_time = now.strftime('%d-%m-%y_%H_%M_%S')
os.system('color 0a')
def restart():
        os.system('cls')
        os.system('python scan_wifi.py')
def exit():
    os.system('exit')

def scanwifi():
    output = subprocess.getoutput('netsh wlan show networks interface=Wi-Fi')
    print(output)
    inpt = input('Do you want to export into .txt ?\n y or n for scan again press r\n')
    try:
        if inpt == 'y':
            f = open(current_time+'.txt','w')
            f.write(output)
            print("Export successfull\n"+current_time+".txt")
            f.close()
        elif inpt =='r':
            restart()
        elif inpt=='n':
            exit()
            
    except:
        print('something went wrong')
        input()
        exit()
    finally:
            y = input("Do you want to restart for it press 'r':\n")
            if y=='r':
                restart()
            else:
                exit()


scanwifi()

   
