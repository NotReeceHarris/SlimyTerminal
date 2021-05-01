#!/usr/bin/env python

import os
import json
import socket
import time
import getpass
from utils import errorCodes

__logs__ = []
__Version__ = '1.0'
__configPath__ = ''

def __clear__(): 
    os.system('cls' if os.name == 'nt' else 'clear')

def color(C):
    if C == 'WHITE':        return u'\u001b[37m'
    elif C == 'RED':        return u'\u001b[31m'
    elif C == 'GREEN':      return u'\u001b[32m'
    elif C == 'YELLOW':     return u'\u001b[33m'
    elif C == 'BLUE':       return u'\u001b[34m'
    elif C == 'MAGENTA':    return u'\u001b[35m'
    elif C == 'CYAN':       return u'\u001b[36m'
    elif C == 'RESET':      return u'\u001b[0m'
    else:                   return u'\u001b[0m'


def configMenu():
    __clear__()

    while True:
        config = json.load(open(__configPath__))

        a = u'\u001b[32mY\u001b[0m'     if config['clearEachCommand']   else '\u001b[31mN\u001b[0m'
        b = u'\u001b[32mY\u001b[0m'     if config['showExitCode']       else '\u001b[31mN\u001b[0m'
        c = u'\u001b[32mY\u001b[0m'     if config['errorCheck']         else '\u001b[31mN\u001b[0m'

        menu = f'''           
        ┌────{color(config["terminalColor"])}Config{color("RESET")}─{color(config["terminalColor"])}Menu{color("RESET")}─────────────────────────────────┐       
        │    1 - [{a}] Clear CLI each command.             │
        │    2 - [{b}] Show command exit code.             │
        │    3 - [{c}] Error checking.                     │
        │    4 - [-] Set terminal color.                 │
        │    5 - [-] Terminal layout.                    │
        │    0 - Exit                                    │
        └────────────────────────────────────────────────┘
        '''

        while True:
            try:
                i = int(input(f'{menu}\n        > '))
                break

            except:
                print('Invalid Option')
            finally:
                __clear__()


        if i == 0: # Exit config Menu.
            break

        elif i == 1: # Toggle clear after command.
            config['clearEachCommand'] = False if config['clearEachCommand'] else True
            json.dump(config, open("config.json", "w"))

        elif i == 2: # Toggle exit codes.
            config['showExitCode'] = False if config['showExitCode'] else True
            json.dump(config, open("config.json", "w"))

        elif i == 3: # Toggle error checking.
            config['errorCheck'] = False if config['errorCheck'] else True
            json.dump(config, open("config.json", "w"))


        elif i == 4: # Select terminal color.
            while True:
                WHITE = u'\u001b[37mY\u001b[0m'     if config['terminalColor'] == 'WHITE'   else '-'
                RED = u'\u001b[31mY\u001b[0m'       if config['terminalColor'] == 'RED'     else '-'
                GREEN = u'\u001b[32mY\u001b[0m'     if config['terminalColor'] == 'GREEN'   else '-'
                YELLOW = u'\u001b[33mY\u001b[0m'    if config['terminalColor'] == 'YELLOW'  else '-'
                BLUE = u'\u001b[34mY\u001b[0m'      if config['terminalColor'] == 'BLUE'    else '-'
                MAGENTA = u'\u001b[35mY\u001b[0m'   if config['terminalColor'] == 'MAGENTA' else '-'
                CYAN = u'\u001b[36mY\u001b[0m'      if config['terminalColor'] == 'CYAN'    else '-'

                menu = f'''           
        ┌────{color(config["terminalColor"])}Color{color("RESET")}─{color(config["terminalColor"])}Menu{color("RESET")}──────────────────────────────┐       
        │    1 - [{WHITE}] {color('WHITE') + "White" + color('RESET')}                           │
        │    2 - [{RED}] {color('RED') + "Red" + color('RESET')}                             │
        │    3 - [{GREEN}] {color('GREEN') + "Green" + color('RESET')}                           │
        │    4 - [{YELLOW}] {color('YELLOW') + "Yellow" + color('RESET')}                          │
        │    5 - [{BLUE}] {color('BLUE') + "Blue" + color('RESET')}                            │
        │    6 - [{MAGENTA}] {color('MAGENTA') + "Magenta" + color('RESET')}                         │
        │    7 - [{CYAN}] {color('CYAN') + "Cyan" + color('RESET')}                            │
        │    0 - Exit                                │
        └────────────────────────────────────────────┘
                    '''
                while True:
                    try:
                        i = int(input(f'{menu}\n        > '))
                        __clear__()
                        break

                    except:
                        __clear__()
                        print(f'Invalid Option')

                if i == 0: 
                    break

                elif i == 1: 
                    config['terminalColor'] = 'WHITE'
                    json.dump(config, open("config.json", "w"))

                elif i == 2: 
                    config['terminalColor'] = 'RED'
                    json.dump(config, open("config.json", "w"))

                elif i == 3: 
                    config['terminalColor'] = 'GREEN'
                    json.dump(config, open("config.json", "w"))

                elif i == 4: 
                    config['terminalColor'] = 'YELLOW'
                    json.dump(config, open("config.json", "w"))

                elif i == 5: 
                    config['terminalColor'] = 'BLUE'
                    json.dump(config, open("config.json", "w"))

                elif i == 6: 
                    config['terminalColor'] = 'MAGENTA'
                    json.dump(config, open("config.json", "w"))

                elif i == 7: 
                    config['terminalColor'] = 'CYAN'
                    json.dump(config, open("config.json", "w"))

                else: 
                    __clear__()
                    print('Invalid Option')

        if i == 5:
            while True:

                a = u'\u001b[32mY\u001b[0m'     if config['terminalLayout']['dir']  else u'\u001b[31mN\u001b[0m'
                b = u'\u001b[32mY\u001b[0m'     if config['terminalLayout']['user'] else u'\u001b[31mN\u001b[0m'
                c = u'\u001b[32mY\u001b[0m'     if config['terminalLayout']['ip']   else u'\u001b[31mN\u001b[0m'

                menu = f'''           
        ┌────{color(config["terminalColor"])}Terminal{color("RESET")}─{color(config["terminalColor"])}Layout{color("RESET")}─────────────────────────┐       
        │    1 - [{a}] Show Directory                  │
        │    2 - [{b}] Show User                       │
        │    3 - [{c}] Show Local-Ip                   │
        │    0 - Exit                                │
        └────────────────────────────────────────────┘
                        '''
                
                while True:
                    try:
                        i = int(input(f'{menu}\n        > '))
                        __clear__()
                        break

                    except:
                        __clear__()
                        print('Invalid Option')

                if i == 0:
                    break

                elif i == 1:
                    config['terminalLayout']['dir'] = False if config['terminalLayout']['dir'] else True
                    json.dump(config, open("config.json", "w"))

                elif i == 2:
                    config['terminalLayout']['user'] = False if config['terminalLayout']['user'] else True
                    json.dump(config, open("config.json", "w"))

                elif i == 3:
                    
                    config['terminalLayout']['ip'] = False if config['terminalLayout']['ip'] else True
                    json.dump(config, open("config.json", "w"))

                else:
                    print('Invalid Option')
            
        else:
            __clear__()
    

def helpMenu():

    config = json.load(open(__configPath__))

    print(f'''           
        ┌────{color(config["terminalColor"])}Help{color("RESET")}─{color(config["terminalColor"])}Menu{color("RESET")}───────────────────────────────────┐ 
        │    :q :quit    -   Exit                        │
        │    :h :help    -   Help menu                   │
        │    :l :logs    -   Show logs                   │
        │    :c :clear   -   Clear CLI                   │
        │    :C :config  -   Config Menu                 │
        │    :g :github  -   Github repo                 │
        │    :v :version -   Slimy Terminal Version      │
        └────────────────────────────────────────────────┘
    ''')

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
                    __tabs__ += f'─[ {color(config["terminalColor"]) + os.getcwd() + color("RESET")} ]'.replace('/', color("RESET")+'/'+color(config["terminalColor"] ))


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
                helpMenu()

            elif i.lower() == ':logs' or i.lower() == ':l': 
                logsMenu()

            elif i.lower() == ':clear' or i == ':c': 
                __clear__()

            elif i.lower() == ':config' or i == ':C': 
                configMenu()

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
                    __statusCode__ = 'Error'

            else:
                __statusCode__ = errorCodes(os.system(i), os.name)

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
    
    __clear__()
    helpMenu()
    start()
