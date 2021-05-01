import os

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
