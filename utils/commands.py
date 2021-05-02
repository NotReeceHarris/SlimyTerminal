import os

from utils.ui import color, __clear__
from utils.exitCodes import exitCodes
from utils.otherMenus import helpMenu, logsMenu
from utils.configMenu import configMenu
from utils.versionControl import checkUpdate

__commandPath__ = ''
__commandVersion__ = ''
__commandlogs__ = ''

def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

# --------------------------------------------------------- Custom Command

def command_help(i):
    page = ''

    for x in ['1', '2', '3', '4', '5']:
        if i.endswith(x): page = x

    if i.lower() == ':help' or i.lower() == ':h':
        helpMenu(__commandPath__, 1)
    
    elif page != '':
        helpMenu(__commandPath__, int(page))

    else:
        print('Invalid help page...')

def command_version(__Version__):
    checkUpdate(__Version__)
    print(f'\n        Slimy Terminal{color("GREEN") + __Version__ + color("RESET")}')

def command_time():
    from datetime import datetime
    import json

    config = json.load(open(__commandPath__))
    time = datetime.now().astimezone()

    print(f'''
        {time.tzname()} 
        {color(config["terminalColor"]) + "Date" + color("RESET")} : {time.strftime("%d/%m/%Y")}
        {color(config["terminalColor"]) + "Time" + color("RESET")} : {time.strftime("%H:%M:%S")}'''.replace('/', color(config["terminalColor"]) + "/" + color("RESET")).replace(':', color(config["terminalColor"]) + ":" + color("RESET")))

def command_network():
    try:
        import psutil
        import platform
        from datetime import datetime
        import json

        config = json.load(open(__commandPath__))
        names = ''
        addrs = '{"Details":['
        a = psutil.net_if_addrs()

        count = 1
        for x in a:
            addrs += str( '{ \'Details\':[{' + str(dict(a)[x])[10:-2]+'}]},').replace('=',':').replace('snicaddr(', '{').replace(')','}').replace('family:', '\'family\':').replace('>,', '>\',').replace(': ','').replace('<A', '\'<A').replace('None','\'None\'').replace('ptp','\'ptp\'').replace('broadcast','\'broadcast\'').replace('netmask','\'netmask\'').replace('address','\'address\'').replace('\'','"')
            count += 1
        count = 1

        addrs = addrs[:-1]+']}'

        ftemp = open('temp', 'w')
        ftemp.write(addrs)
        ftemp.close()

        jload = json.load(open('temp', 'r'))
        os.remove('temp')

        count = 1
        for x in a:
            names += f'        │    {count} {color(config["terminalColor"]) + x + color("RESET")}\n        │      ├─{jload["Details"][count-1]["Details"][0]["family"]}\n        │      │ ├─{jload["Details"][count-1]["Details"][0]["address"]}\n        │      │ └─{jload["Details"][count-1]["Details"][0]["netmask"]}\n        │      └─{jload["Details"][count-1]["Details"][1]["family"]}\n        │        ├─{jload["Details"][count-1]["Details"][1]["address"]}\n        │        └─{jload["Details"][count-1]["Details"][1]["netmask"]}\n'
            count += 1
        count = 1

        print(f'''
        ┌────{color(config["terminalColor"])}Network{color("RESET")}─{color(config["terminalColor"])}Info{color("RESET")}───────────────────────────────── 
{names[:-1]}
        └─────────────────────────────────────────────────''')
    except ImportError:
        print('Error loading psutil try installing all dependency... ')

def command_ping(i):
    import json
    import os

    config = json.load(open(__commandPath__))
    print(f'''
        ┌────{color(config["terminalColor"])}Ping{color("RESET")}─{color(config["terminalColor"])}Module{color("RESET")}─────────────────────────────────┐
        │    Please wait while ping is executing...      │
        └────────────────────────────────────────────────┘''')
    ping = os.popen(f"ping {i[6:]}")
    printPing = ''
    for x in ping.readlines(): printPing += str(f'        │   {x}')
    if config['clearEachCommand']: 
        __clear__()
    print(f'''
        ┌────{color(config["terminalColor"])}Ping{color("RESET")}─{color(config["terminalColor"])}Module{color("RESET")}────────────────────────────────── ''')
    print(printPing, end="")

    print('        └─────────────────────────────────────────────────')


# --------------------------------------------------------- System Command handler

def commandHandle(i, __configPath__, __Version__, __logs__):

    global __commandPath__, __commandVersion__, __commandlogs__
    __commandPath__ = __configPath__
    __commandVersion__ = __Version__
    __commandlogs__ =  __logs__

    if i.lower() == ':quit' or i.lower() == ':q': 
        exit()

    elif i.lower()[:5] == ':help' or i.lower()[:2] == ':h':
        command_help(i)

    elif i.lower() == ':logs' or i.lower() == ':l': 
        logsMenu(__configPath__, __logs__)

    elif i.lower() == ':clear' or i == ':c': 
        __clear__()

    elif i.lower() == ':config' or i == ':C': 
        configMenu(__configPath__)

    elif i.lower() == ':github' or i.lower() == ':g': 
        print('https://github.com/NotReeceHarris/SlimyTerminal')

    elif i.lower() == ':version' or i.lower() == ':v': 
        command_version(__Version__)
    
# --------------------------------------------------------- Custom Command handler
    
    elif i.lower() == ':time': 
        command_time()
    
    elif i.lower() == ':network': 
        command_network()

    elif i.lower().startswith(':ping'): 
        command_ping(i)
    

# --------------------------------------------------------- System Command handler

    else:
        __statusRaw__ = os.system(i)
        __statusCode__ = exitCodes(__statusRaw__, os.name)
    