import os
import json
import socket
import getpass

from utils.ui import color, __clear__

def configMenu(__configPath__):
    __clear__()

    if True:
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