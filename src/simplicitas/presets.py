"""
Lists of colors and effects

Planned additions:
    - table: the option to create a table
    - tree:  creates a directory tree
"""
import sys
from time import sleep

def typewriter(*args, **kwargs) -> str:
    line = kwargs.get('line', None)
    speed = kwargs.get('speed', None)
    for char in line:
        print(char, end='')
        sys.stdout.flush()
        sleep(float(speed))





PRESETS = {
    """
    Colors that can be used in the "colors" parameter without having to use a rgb/hex code
    """

#### COLORS ####
    'white': [255, 255, 255],                 # -> rgb(255, 255, 255)
    'black': [0, 0, 0],                       # -> rgb(0, 0, 0)
    'light_blue': [0, 153, 255],              # -> rgb(0, 153, 255)
    'blue': [0, 0, 153],                      # -> rgb(0, 0, 153)
    'light_green': [0, 255, 0],               # -> rgb(0, 255, 0)
    'green': [0, 153, 51],                    # -> rgb(0, 153, 51)
    'yellow': [255, 255, 0],                  # -> rgb(255, 255, 0)
    'orange': [255, 153, 0],                  # -> rgb(255, 153, 0)
    'red': [255, 0, 0],                       # -> rgb(255, 0, 0)
    'light_red': [255, 51, 51],               # -> rgb(255, 51, 51)
    'pink': [255, 51, 153],                   # -> rgb(255, 51, 153)
    'purple': [153, 51, 153],                 # -> rgb(153, 51, 153)

#### EFFECTS ####
    'typewriter': typewriter,                       #: for calling typewriter function
}


ERR_TYPES = {
    "WRONG_ORIGIN": "'origin' must be of type dict.",
    "I/O": "Given input cannot be used as an output.",
}


#   DECORATORS   #
underline:          str = '\033[4m'
bold:               str = '\033[1m'
blink:              str = '\033[5m'
framed:             str = '\033[51m'
encircled:          str = '\033[52m'