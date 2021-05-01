import requests
import time
import os

from utils.ui import color, __clear__

def checkUpdate(__Version__):
    try:
        r = requests.get('https://raw.githubusercontent.com/NotReeceHarris/SlimyTerminal/main/VERSION').text
        if float(__Version__) < float(r):
            while True:
                i = input(str(f'New version SlimyTerminal({color("GREEN")+str(float(r))+color("RESET")}) is available, Update? [Y/n]: '))
                if i.lower() == 'y' or i.lower() == 'yes':
                    update()
                    break
                elif i.lower() == 'n' or i.lower() == 'no':
                    break
                else:
                    __clear__()
                    print('Invalid option..')
    except:
        print('Update checking failed...')
        time.sleep(0.5)

def update():
    __clear__()
    print('Updating...')
    os.system('git fetch https://github.com/NotReeceHarris/SlimyTerminal.git')