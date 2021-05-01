import os
import json
import getpass
import socket

def __clear__():        # Terminal wipe module
    os.system('cls' if os.name == 'nt' else 'clear')

def color(C):           # Color selection module
    if C == 'WHITE':        return u'\u001b[37m'
    elif C == 'RED':        return u'\u001b[31m'
    elif C == 'GREEN':      return u'\u001b[32m'
    elif C == 'YELLOW':     return u'\u001b[33m'
    elif C == 'BLUE':       return u'\u001b[34m'
    elif C == 'MAGENTA':    return u'\u001b[35m'
    elif C == 'CYAN':       return u'\u001b[36m'
    elif C == 'RESET':      return u'\u001b[0m'
    else:                   return u'\u001b[0m'

def tabBroker(__configPath__):
    __tabs__ = ''
    config = json.load(open(__configPath__))

    if config['terminalLayout']['dir']: 
        activeDir = '-----'
        try:
            activeDir = os.getcwd()
            if os.name == 'nt':
                __tabs__ += f'─[ {color("RESET") + activeDir[:3]}{color(config["terminalColor"]) + activeDir[3:] + color("RESET")} ]'.replace('\\',color("RESET") + "\\" + color(config["terminalColor"]))
            else:
                __tabs__ += f'─[ ~{color(config["terminalColor"]) + activeDir + color("RESET")} ]'.replace('/', color("RESET") + '/' + color(config["terminalColor"] ))
        except:
            __tabs__ += f'─[ {color(config["terminalColor"]) + activeDir + color("RESET")} ]'


    if config['terminalLayout']['user']: 
        user = '-----'
        try:
            user = getpass.getuser()
            __tabs__ += f'─[ {color(config["terminalColor"]) +  user.lower().replace(" ",color("RESET") + "-" + color(config["terminalColor"])) + color("RESET")}@{color(config["terminalColor"]) +  socket.gethostname().replace("-",color("RESET") + "-" + color(config["terminalColor"])) + color("RESET")} ]'
        except:
            __tabs__ += f'─[ {color(config["terminalColor"]) + user + color("RESET")} ]'


    if config['terminalLayout']['ip']:
        locIp = '-----'
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            locIp = s.getsockname()[0]
            s.close()

            __tabs__ += f'─[ {color(config["terminalColor"]) + locIp + color("RESET")} ]'.replace('.',color("RESET") + "." + color(config["terminalColor"]))
        except:
            __tabs__ += f'─[ {color(config["terminalColor"]) + locIp + color("RESET")} ]'
    
    return __tabs__

def spacerBroker(__configPath__, __statusCode__):

    __spacer__ = ''
    __cursor__ = ''
    config = json.load(open(__configPath__))

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

    return (__spacer__, __cursor__)