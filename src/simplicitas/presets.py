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
    'white': list([255, 255, 255]),                 # -> rgb(255, 255, 255)
    'black': list([0, 0, 0]),                       # -> rgb(0, 0, 0)
    'light_blue': list([0, 153, 255]),              # -> rgb(0, 153, 255)
    'blue': list([0, 0, 153]),                      # -> rgb(0, 0, 153)
    'light_green': list([0, 255, 0]),               # -> rgb(0, 255, 0)
    'green': list([0, 153, 51]),                    # -> rgb(0, 153, 51)
    'yellow': list([255, 255, 0]),                  # -> rgb(255, 255, 0)
    'orange': list([255, 153, 0]),                  # -> rgb(255, 153, 0)
    'red': list([255, 0, 0]),                       # -> rgb(255, 0, 0)
    'light_red': list([255, 51, 51]),               # -> rgb(255, 51, 51)
    'pink': list([255, 51, 153]),                   # -> rgb(255, 51, 153)
    'purple': list([153, 51, 153]),                 # -> rgb(153, 51, 153)

#### EFFECTS ####
    'typewriter': typewriter,                       #: for calling typewriter function
}
