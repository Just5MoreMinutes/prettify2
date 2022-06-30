"""
    prettify
    -=-=-=-=-=-=-=-
    by Just5MoreMinutes

    prettify allows you to modify colors in the windows & linux
    terminal.
"""

class prettify_cli:

    def setup(self, interactable=False, colors_ok=True):
        pass


class prettify:

    def println(self, text, multi_color=False, *args, **kwargs) -> str:
        color = kwargs.get('color', None)                   #: sets up optional parameter color
        import src.prettify_cli.presets as presets
        effects = kwargs.get('effects', None)




reset = '\033[0m'               #: resets color
def rgb(r,g,b,bg=False):
    """
    Can set text to any color on the rgb spectrum.

    USAGE:
        print("Hello" + rgb(255, 128, 0) + "World!")
    """
    return '\033[{};2;{};{};{}m'.format(48 if bg else 38,r,g,b)         #: returns given color. checks if bg is True (48 if bg) and sets value depending on that. if false it will be skipped
                                                                        # and only the foreground color will be used

def hex(code,bg=False):
    """
    Can set text to any color.

    USAGE:
        print(hex(code='#ff66cc') + "Hello, World!")
    """
    tmp = tuple(int(code.strip('#')[i:i+2], 16) for i in (0, 2, 4))              # try to understand this bs sometime  
    return '\033[{};2;{};{};{}m'.format(48 if bg else 38, tmp[0],tmp[1],tmp[2])



#   DECORATORS   #
underline:          str = '\033[4m'
bold:               str = '\033[1m'
blink:              str = '\033[5m'
framed:             str = '\033[51m'
encircled:          str = '\033[52m'


print(hex(code='#ff6678') + encircled + "this is a test" +reset)