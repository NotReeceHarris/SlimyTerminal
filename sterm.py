#!/usr/bin/env python

import os
import json
import socket
import getpass
import random

from utils.ui import color, __clear__
from utils.exitCodes import exitCodes
from utils.helpMenu import helpMenu
from utils.configMenu import configMenu
from utils.versionControl import checkUpdate

__logs__ = []
__Version__ = '1.0'
__configPath__ = ''

def logsMenu():

    config = json.load(open(__configPath__))

    print(f'        ┌────{color(config["terminalColor"])}Log{color("RESET")}─{color(config["terminalColor"])}Menu{color("RESET")}─────────────────────────────────────\n        │')
    for x in __logs__:
        print(f'        │ {x}')
    print('        │\n        └─────────────────────────────────────────────────')

def start():

    __statusCode__ = ''

    while True:

        __tabs__ = f''
        __spacer__ = ''
        __cursor__ = ''

        config = json.load(open(__configPath__))
        
        try:

            if config['terminalLayout']['dir']: 
                if os.name == 'nt':
                    __tabs__ += f'─[ {color("RESET") + os.getcwd()[:3]}{color(config["terminalColor"]) + os.getcwd()[3:] + color("RESET")} ]'.replace('\\',color("RESET")+"\\"+color(config["terminalColor"]))
                else:
                    __tabs__ += f'─[ ~{color(config["terminalColor"]) + os.getcwd() + color("RESET")} ]'.replace('/', color("RESET")+'/'+color(config["terminalColor"] ))


            if config['terminalLayout']['user']: 
                __tabs__ += f'─[ {color(config["terminalColor"]) +  getpass.getuser().lower().replace(" ",color("RESET")+"-"+color(config["terminalColor"])) + color("RESET")}@{color(config["terminalColor"]) +  socket.gethostname().replace("-",color("RESET")+"-"+color(config["terminalColor"])) + color("RESET")} ]'
            
            if config['terminalLayout']['ip']:
                
                LocIp = '-----'

                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    s.connect(("8.8.8.8", 80))
                    LocIp = s.getsockname()[0]
                    s.close()

                except:
                    pass

                __tabs__ += f'─[ {color(config["terminalColor"]) + LocIp + color("RESET")} ]'.replace('.',color("RESET")+"."+color(config["terminalColor"]))

            if not config['terminalLayout']['dir'] and not config['terminalLayout']['user'] and not config['terminalLayout']['ip']:
                __spacer__ = u'\033[F'
                __cursor__ = '──>'

            elif config['terminalLayout']['dir'] or config['terminalLayout']['user'] or config['terminalLayout']['ip']:

                if config['showExitCode'] and __statusCode__ != '':
                    __spacer__ = '├──'
                    __cursor__ = '└─>'

                else:
                    __spacer__ = '┌──'
                    __cursor__ = '└─>'

            elif not config['terminalLayout']['dir'] and not config['terminalLayout']['user'] and not config['terminalLayout']['ip'] and config['showExitCode']:
                __spacer__ = u'\033[F'
                __cursor__ = '└─>'

            if __statusCode__ == '' or config['showExitCode'] == False:
                i = str(input(f'''
    {__spacer__}{__tabs__}
    {__cursor__} '''))

            elif __statusCode__ != '' and config['showExitCode'] == True:
                i = str(input(f'''
    ┌───[ {color(config["terminalColor"]) + __statusCode__ + color('RESET')} ]
    {__spacer__}{__tabs__}
    └─> '''))

            print(' ')

            __logs__.append(str(i))
            __statusCode__ = ''

            if config['clearEachCommand']: __clear__()

            if i.lower() == ':quit' or i.lower() == ':q': 
                break

            elif i.lower() == ':help' or i.lower() == ':h': 
                helpMenu(__configPath__)

            elif i.lower() == ':logs' or i.lower() == ':l': 
                logsMenu()

            elif i.lower() == ':clear' or i == ':c': 
                __clear__()

            elif i.lower() == ':config' or i == ':C': 
                configMenu(__configPath__)

            elif i.lower() == ':github' or i.lower() == ':g': 
                print('https://github.com/NotReeceHarris/SlimyTerminal')

            elif i.lower() == ':version' or i.lower() == ':v': 
                print(f'Slimy Terminal: {__Version__}')
            
            elif i.startswith('cd'):
                try:
                    os.chdir(i[3:])
                    __statusCode__ = 'Success'
                except:
                    print(f'Unknown Directory "{color(config["terminalColor"]) + i[3:] + color("RESET")}"')

                    __statusCode__ = 'Path not found (1)'


            else:
                __statusCode__ = exitCodes(os.system(i), os.name)

        except ValueError:
            pass

if __name__ == '__main__':
    if os.name == 'nt':
        os.system(f'TITLE Slimy Terminal{__Version__} [{os.getlogin()}] (https://github.com/NotReeceHarris/SlimyTerminal)')

    else:
        if not os.geteuid() == 0: # Tests for root if not authenticated exits with code '5'
            print(f'Please run as {color("RED") + "root" + color("RESET")}!')
            os._exit(5)

    try: # Creates the config file on first loadup
        f = open('config.json')

    except IOError:
        print('No config file found! Creating one.')
        f = open('config.json', 'w')
        f.write('{"clearEachCommand": true,"showExitCode":true,"terminalColor":"GREEN","terminalLayout":{"dir":true,"user":false,"ip":false},"errorCheck":true}')
    
    finally:
        __configPath__ = os.path.dirname(os.path.abspath('config.json')).replace('\\','/') + '/config.json'
        f.close()
    
    checkUpdate(__Version__)
    __clear__()
    helpMenu(__configPath__)
    start()
