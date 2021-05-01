from utils.ui import color, __clear__
import json

def helpMenu(__configPath__):

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