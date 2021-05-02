#!/usr/bin/env python

import os
import json

from utils.ui import color, __clear__, tabBroker, spacerBroker
from utils.exitCodes import exitCodes
from utils.otherMenus import helpMenu, logsMenu
from utils.configMenu import configMenu
from utils.versionControl import checkUpdate
from utils.commands import commandHandle

__logs__ = []
__Version__ = '1.0'
__configPath__ = ''

def start():

    __statusCode__ = ''

    while True:
        __tabs__ = tabBroker(__configPath__)
        __spacer__ = spacerBroker(__configPath__, __statusCode__)[0]
        __cursor__ = spacerBroker(__configPath__, __statusCode__)[1]
        config = json.load(open(__configPath__))
        

        if __statusCode__ == '' or config['showExitCode'] == False:
            i = str(input(f'''\n    {__spacer__}{__tabs__}\n    {__cursor__} '''))

        elif __statusCode__ != '' and config['showExitCode'] == True:
            i = str(input(f'''\n    ┌───[ {color(config["terminalColor"]) + __statusCode__ + color('RESET')} ]\n    {__spacer__}{__tabs__}\n    └─> '''))

        __statusCode__ = ''
        __statusRaw__ = ''

        if config['clearEachCommand']: 
            __clear__()
        else:
            print(' ')

        if i.startswith(':'):
            commandHandle(i, __configPath__, __Version__)
            
        elif i.startswith('cd'):
            try:
                os.chdir(i[3:])
                __statusCode__ = 'Success'
            except:
                print(f'Unknown Directory "{color(config["terminalColor"]) + i[3:] + color("RESET")}"')

                __statusCode__ = 'Path not found (1)'

        else:
            __statusRaw__ = os.system(i)
            __statusCode__ = exitCodes(__statusRaw__, os.name)

        __logs__.append((str(i), __statusRaw__))

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

    __clear__()
    checkUpdate(__Version__)
    helpMenu(__configPath__, 1)
    start()
