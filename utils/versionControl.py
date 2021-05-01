import requests
import time
import os

from utils.ui import color, __clear__

def checkUpdate(__Version__):
    try:
        r = requests.get('https://raw.githubusercontent.com/NotReeceHarris/SlimyTerminal/main/VERSION').text
        if float(__Version__) < float(r):
            print(f'        New version SlimyTerminal({color("GREEN")+str(float(r))+color("RESET")}) is available')
    except:
        print('Update checking failed...')
        time.sleep(0.5)