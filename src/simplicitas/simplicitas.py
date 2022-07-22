"""
    simplicitas
    -=-=-=-=-=-=-=-
    by Just5MoreMinutes

    simplicitas allows you to easily create command-line-interfaces for windows and linux
"""
#‾‾‾‾‾‾‾‾‾‾‾‾‾‾#
#    IMPORTS   #
#______________#
import sys
import os
import time

#‾‾‾‾‾‾‾‾‾‾‾‾‾‾#
#   DEFAULTS   #
#______________#
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

#‾‾‾‾‾‾‾‾‾‾‾‾#
#   ERRORS   #
#____________#
default_error_tag = rgb(192,192,192) + "[" + rgb(255,0,0) + "ERROR" + rgb(192,192,192) + "]: " + reset
default_warn_tag  = rgb(192,192,192) + "[" + rgb(255,165,0) + "WARN" + rgb(192,192,192) + "]: " + reset
default_info_tag  = rgb(192,192,192) + "[" + rgb(255,255,0) + "INFO" + rgb(192,192,192) + "]: " + reset
default_success_tag=rgb(192,192,192) + "[" + rgb(0,255,0) + "SUCCESS" + rgb(192,192,192) + "]: " + reset

#‾‾‾‾‾‾‾‾‾‾‾‾#
#    SETUP   #
#____________#
class simplicitas_cli:
    def __init__(self, header: str, text: str, seperator: str, table=False, interactable=True):
        self.header = header    #: requires header definition in given dict
        self.text = text        #: requires text definition in given dict
        self.table = table      #: if True it will be passed to class table
        self.interactable = interactable    #: if False CLI will work with manual commands

    def setup(self, origin: dict, selection_color, status=False, **kwargs) -> str:
        """
        This is required for simplicitas to work. It gets the origin dictionary
        and through there it will recieve all attributes used for the creation of the
        CLI.
        - - -
        Parameters:
            - `origin`: `origin` gets the default dictionary in which all data displayed
            in the final CLI should be stored. Can ONLY be of type dict!

            - `status`: `status` is used for displaying info messages. By default it is 
            set to `False`, though this can be easily changed through passing `status=True`
            into setup. Highly recommended for testing purposes.
        - - -
        Usage:

            - For testing: simplicitas_cli.setup(origin=<dict>, status=True)

            - For final CLI: simplicitas_cli.setup(origin=<dict>, status=False) OR
            simplicitas_cli.setup(origin=<dict>)
        """
        #: check for type of origin
        if type(origin) is not dict:
            #: raise exception when origin isn't a dictionary
            print(default_error_tag + "'origin' must be of type dict.")

        else:   # -> origin is a dictionary

            #: list setup, will be used in CLI creation later
            ELEMENTS = ['header','text']

            __headers = []
            __texts   = []
            __finals  = {"header": __headers, "text": __texts}

            #: iterates through list ELEMENTS
            for elem in ELEMENTS:

                #: checks if item from list (ELEMENTS) is in 'origin' dict
                if elem in list(origin.keys()):

                    #: print found elements if status is set to True (False by default)
                    print(default_info_tag + "Element '"+origin[elem]+"' found under key '"+elem+"'.") if status == True else None

                    #: appends item to corresponding list (id in dict is "header" -> appends to "__headers" list)
                    __finals[elem].append(origin[elem])

                #: checks if iteration reached list end
                if ELEMENTS.index(elem) == len(ELEMENTS)-1:
                    #: print success info if status is set to True (False by default)
                    print("\n"+default_success_tag+"Found all elements!") if status == True else None

            #: set header and text elements to corresponding lists for later use
            self.header = __headers     
            self.text   = __texts

            try:
                from presets import PRESETS
                if selection_color in PRESETS:
                    return rgb(PRESETS[selection_color[0],PRESETS[selection_color[1]],PRESETS[selection_color[2]]])
                elif selection_color not in PRESETS:
                    if 'rgb' or 'hex' in selection_color:
                        return selection_color
                    else:
                        print(default_error_tag + "Please use a default color or the rgb/hex format for custom selection colors!")
                        exit()

            except ImportError:

                selection_color = rgb(0, 153, 51)

    
    def extra(self, multiple_origin=False, **kwargs):

        if multiple_origin == True:
            origins = [str]             # -> simplicitas_cli.extra(multiple_origin=True, origins=[<dict>,<dict>])       //      sorted chronologically

            #: run through setup() again with the new dicts
            for i in origins:

                #: pass dicts into self.setup()
                self.setup(origin=i, status=False)


#: initialize class
simplicitas_cli = simplicitas_cli('','')



class create(simplicitas_cli):
    def __init__(self, header: str, text: str, seperator: str, table=False, interactable=True):
        super().__init__(header, text, seperator, table, interactable)

    def backend(self):

        up      = '\033[A'       #: Arrow key up
        down    = '\033[B'       #: Arrow key down
        right   = '\033[C'       #: Arrow key right
        left    = '\033[D'       #: Arrow key left

        try: from pynput import keyboard
        except ImportError: print(default_error_tag + "Fatal import failed (pynput/keyboard).")

        def on_press(key):

            if key == keyboard.Key.up:
                return up
            
            if key == keyboard.Key.down:
                return down

            if key == keyboard.Key.right:
                return right

            if key == keyboard.Key.left:
                return left

            if key == keyboard.Key.esc:
                return exit(default_info_tag + "Program exited!")
            
            if key == keyboard.Key.enter:
                pass            #: supposed to get next view/execute function

        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()

            sys.stdout.write(simplicitas_cli.setup.selection_color + self.text)
            sys.stdout.flush()
        



class table(simplicitas_cli):
    def __init__(self, header, text: str, table=False, interactable=True):
        super().__init__(header, text, table, interactable)


sample = {
    'header': 'this is a header',
    'text': 'this is some text'
}

simplicitas_cli.setup(origin=sample, status=True)