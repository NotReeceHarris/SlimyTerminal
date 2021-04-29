#!/usr/bin/env python

import os
import json
import socket
import time

__logs__ = []
__Version__ = '1.0'

def __clear__(): 
    os.system('cls' if os.name == 'nt' else 'clear')

def color(ColorName):

    if ColorName == 'WHITE':
        return u'\u001b[37m'
    elif ColorName == 'RED':
        return u'\u001b[31m'
    elif ColorName == 'GREEN':
        return u'\u001b[32m'
    elif ColorName == 'YELLOW':
        return u'\u001b[33m'
    elif ColorName == 'BLUE':
        return u'\u001b[34m'
    elif ColorName == 'MAGENTA':
        return u'\u001b[35m'
    elif ColorName == 'CYAN':
        return u'\u001b[36m'
    elif ColorName == 'RESET':
        return u'\u001b[0m'

def configMenu():

    __clear__()

    while True:
        config = json.load(open("config.json"))

        a = color('RED') + "X" + color('RESET')
        b = color('RED') + "X" + color('RESET')
        c = color('RED') + "X" + color('RESET')

        if config['clearEachCommand']:  a = color('GREEN') + "✓" + color('RESET')
        if config['showExitCode']:  b = color('GREEN') + "✓" + color('RESET')
        if config['errorCheck']:  c = color('GREEN') + "✓" + color('RESET')

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
                print(menu)
                i = int(input('        > '))
                __clear__()
                break

            except:
                __clear__()
                print('Invalid Option')
        
        if i == 0: 
            break

        elif i == 1:
            t = True
            if config['clearEachCommand']: t = False
            config['clearEachCommand'] = t
            json.dump(config, open("config.json", "w"))

        elif i == 2:
            t = True
            if config['showExitCode']: t = False
            config['showExitCode'] = t
            json.dump(config, open("config.json", "w"))

        elif i == 3:
            t = True
            if config['errorCheck']: t = False
            config['errorCheck'] = t
            json.dump(config, open("config.json", "w"))

        elif i == 4:
            while True:

                a = '-'
                b = '-'
                c = '-'
                d = '-'
                e = '-'
                f = '-'
                g = '-'

                if config['terminalColor'] == 'WHITE':  a = u'\u001b[37m✓\u001b[0m'
                elif config['terminalColor'] == 'RED':  b = u'\u001b[31m✓\u001b[0m'
                elif config['terminalColor'] == 'GREEN':  c = u'\u001b[32m✓\u001b[0m'
                elif config['terminalColor'] == 'YELLOW':  d = u'\u001b[33m✓\u001b[0m'
                elif config['terminalColor'] == 'BLUE':  e = u'\u001b[34m✓\u001b[0m'
                elif config['terminalColor'] == 'MAGENTA':  f = u'\u001b[35m✓\u001b[0m'
                elif config['terminalColor'] == 'CYAN':  g = u'\u001b[36m✓\u001b[0m'

                __clear__()
                menu = f'''           
        ┌────{color(config["terminalColor"])}Color{color("RESET")}─{color(config["terminalColor"])}Menu{color("RESET")}──────────────────────────────┐       
        │    1 - [{a}] {color('WHITE') + "White" + color('RESET')}                           │
        │    2 - [{b}] {color('RED') + "Red" + color('RESET')}                             │
        │    3 - [{c}] {color('GREEN') + "Green" + color('RESET')}                           │
        │    4 - [{d}] {color('YELLOW') + "Yellow" + color('RESET')}                          │
        │    5 - [{e}] {color('BLUE') + "Blue" + color('RESET')}                            │
        │    6 - [{f}] {color('MAGENTA') + "Magenta" + color('RESET')}                         │
        │    7 - [{g}] {color('CYAN') + "Cyan" + color('RESET')}                            │
        │    0 - Exit                                │
        └────────────────────────────────────────────┘
                    '''
                while True:
                    try:
                        print(menu)
                        i = int(input('        > '))
                        __clear__()
                        break

                    except:
                        __clear__()
                        print('Invalid Option')
                        print(menu)

                if i == 0: break
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
                    print('Invalid Option')

        if i == 5:
            while True:

                a = color('RED') + "X" + color('RESET')
                b = color('RED') + "X" + color('RESET')
                c = color('RED') + "X" + color('RESET')

                if config['terminalLayout']['dir']: a = color('GREEN') + "✓" + color('RESET')
                if config['terminalLayout']['user']: b = color('GREEN') + "✓" + color('RESET')
                if config['terminalLayout']['ip']: c = color('GREEN') + "✓" + color('RESET')

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
                        print(menu)
                        i = int(input('        > '))
                        __clear__()
                        break

                    except:
                        __clear__()
                        print('Invalid Option')

                if i == 0:
                    break

                elif i == 1:
                    t = True
                    if config['terminalLayout']['dir']: t = False
                    config['terminalLayout']['dir'] = t
                    json.dump(config, open("config.json", "w"))

                elif i == 2:
                    t = True
                    if config['terminalLayout']['user']: t = False
                    config['terminalLayout']['user'] = t
                    json.dump(config, open("config.json", "w"))

                elif i == 3:
                    t = True
                    if config['terminalLayout']['ip']: t = False
                    config['terminalLayout']['ip'] = t
                    json.dump(config, open("config.json", "w"))

                else:
                    print('Invalid Option')
            
        else:
            __clear__()
    

def helpMenu():

    config = json.load(open("config.json"))

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

    config = json.load(open("config.json"))

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

        config = json.load(open("config.json"))
        
        try:

            if config['terminalLayout']['dir']: 
                __tabs__ += f'─[ {color("RESET") + os.getcwd()[:3]}{color(config["terminalColor"]) + os.getcwd()[3:] + color("RESET")} ]'.replace('\\',color("RESET")+"\\"+color(config["terminalColor"]))
            
            if config['terminalLayout']['user']: 
                __tabs__ += f'─[ {color(config["terminalColor"]) +  os.getlogin().lower().replace(" ",color("RESET")+"-"+color(config["terminalColor"])) + color("RESET")}@{color(config["terminalColor"]) +  os.environ["COMPUTERNAME"].replace("-",color("RESET")+"-"+color(config["terminalColor"])) + color("RESET")} ]'
            
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

            else:
                StatusNom = os.system(i)

                if StatusNom == 0:
                    __statusCode__ = 'Success'
                elif StatusNom == 1:
                    __statusCode__ = 'Error'

        except ValueError:
            pass

if __name__ == '__main__':
    os.system(f'TITLE Slimy Terminal{__Version__} [{os.getlogin()}] (https://github.com/NotReeceHarris/SlimyTerminal)')

    try: # Creates the config file on first loadup
        f = open('config.json')
    except IOError:
        print('No config file found! Creating one.')
        time.sleep(0.5)
        f = open('config.json', 'w')
        f.write('{"clearEachCommand": true,"showExitCode":true,"terminalColor":"GREEN","terminalLayout":{"dir":true,"user":false,"ip":false},"errorCheck":true}')
    finally:
        f.close()
    
    __clear__()

    helpMenu()
    start()
