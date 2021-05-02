import os

from utils.ui import color, __clear__
from utils.exitCodes import exitCodes
from utils.otherMenus import helpMenu, logsMenu
from utils.configMenu import configMenu
from utils.versionControl import checkUpdate


def commandHandle(i, __configPath__, __Version__, __logs__):
    if i.lower() == ':quit' or i.lower() == ':q': 
        exit()

    elif i.lower()[:5] == ':help' or i.lower()[:2] == ':h':
        if i.lower() == ':help' or i.lower() == ':h':
            helpMenu(__configPath__, 1)
        elif  i.endswith('1'):
            helpMenu(__configPath__, 1)
        elif  i.endswith('2'):
            helpMenu(__configPath__, 2)
        elif  i.endswith('3'):
            helpMenu(__configPath__, 3)
        elif  i.endswith('4'):
            helpMenu(__configPath__, 4)
        elif  i.endswith('5'):
            helpMenu(__configPath__, 5)
        else:
            print('Invalid help page...')

    elif i.lower() == ':logs' or i.lower() == ':l': 
        logsMenu(__configPath__, __logs__)

    elif i.lower() == ':clear' or i == ':c': 
        __clear__()

    elif i.lower() == ':config' or i == ':C': 
        configMenu(__configPath__)

    elif i.lower() == ':github' or i.lower() == ':g': 
        print('https://github.com/NotReeceHarris/SlimyTerminal')

    elif i.lower() == ':version' or i.lower() == ':v': 
        checkUpdate(__Version__)
        print(f'Slimy Terminal: {__Version__}')
    
    else:
        __statusRaw__ = os.system(i)
        __statusCode__ = exitCodes(__statusRaw__, os.name)
    