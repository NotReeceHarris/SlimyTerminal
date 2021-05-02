from utils.ui import color, __clear__
import json

def helpMenu(__configPath__, n):

    config = json.load(open(__configPath__))
    
    if n == 1:
        print(f'''           
        ┌────{color(config["terminalColor"])}Help{color("RESET")}─{color(config["terminalColor"])}Menu{color("RESET")}─[1/5]─────────────────────────────┐ 
        │    :q :quit    -   Exit slimyTerminal          │
        │    :C :config  -   Config Menu                 │
        │    :c :clear   -   Clear CLI                   │
        │    :l :logs    -   Show logs                   │
        │    :h :help 1  -   Help menu [1/5]             │
        └────────────────────────────────────────────────┘
        ''')

    elif n == 2:
        print(f'''           
        ┌────{color(config["terminalColor"])}Help{color("RESET")}─{color(config["terminalColor"])}Menu{color("RESET")}─[2/5]─────────────────────────────┐ 
        │    :g :github  -   Github repo                 │
        │    :v :version -   Slimy Terminal Version      │
        └────────────────────────────────────────────────┘
        ''')

def logsMenu(__configPath__, __logs__):

    config = json.load(open(__configPath__))

    print(f'        ┌────{color(config["terminalColor"])}Log{color("RESET")}─{color(config["terminalColor"])}Menu{color("RESET")}─────────────────────────────────────\n        │')
    for x in __logs__:
        print(f'        │ {x[1]} | {x[0]}')
    print('        │\n        └─────────────────────────────────────────────────')
