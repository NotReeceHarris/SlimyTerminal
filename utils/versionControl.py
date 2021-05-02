import time
import os

from utils.ui import color, __clear__

def checkUpdate(__Version__):
    try:
        import requests
        r = requests.get('https://raw.githubusercontent.com/NotReeceHarris/SlimyTerminal/main/VERSION').text
        if float(__Version__) < float(r):
            print(f'        New version SlimyTerminal({color("GREEN")+str(float(r))+color("RESET")}) is available')
    except:
        while True:
            i = str(input('Try installing dependency? [Y/n]: '))
            if i.lower() == 'y':
                os.system('pip install -r requirements.txt')
                __clear__()
                try:
                    import requests
                    __clear__()
                    print(f'[{color("GREEN") + "+" + color("RESET")}] requests, Installed!')
                    import psutil
                    print(f'[{color("GREEN") + "+" + color("RESET")}] psutil, Installed!')
                    break
                except:

                    print('Pip install failed...')
                    break

            elif i.lower() == 'n':
                __clear__()
                print('Update checking failed...')
                break

            else:
                __clear__()
                print('Update checking failed...')
        time.sleep(0.5)