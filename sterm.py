#!/usr/bin/env python

import os
import json

from utils.ui import color, __clear__, tabBroker, spacerBroker
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
        __tabs__ = tabBroker(__configPath__)
        __spacer__ = spacerBroker(__configPath__, __statusCode__)[0]
        __cursor__ = spacerBroker(__configPath__, __statusCode__)[1]
        config = json.load(open(__configPath__))
        

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
            checkUpdate(__Version__)
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
    helpMenu(__configPath__)
    start()
