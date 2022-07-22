

reset = '\033[0m'               #: resets color
def rgb(r,g,b,bg=False):
    """
    Can set text to any color on the rgb spectrum.

    USAGE:
        print("Hello" + rgb(255, 128, 0) + "World!")
    """
    return '\033[{};2;{};{};{}m'.format(48 if bg else 38,r,g,b)


class error_wrapper:
    def __init__(self, ERROR_TYPE):
        self.ERROR_TYPE = ERROR_TYPE

    def err_out(self,**kwargs):
        m = rgb(192,192,192) + "[" + rgb(255,0,0) + "ERROR" + rgb(192,192,192) + "]"
        from presets import ERR_TYPES
        msg = ERR_TYPES.get(self.ERROR_TYPE); unknown = 'An unkown error occured'
        return str(m, msg) if msg != None else print(unknown)

error_wrapper = error_wrapper('')

class WRONG_ORIGN(Exception):
    def __init__(self, message, *args: object):
        super().__init__(*args)
        self.message = message
        



default_error_tag = rgb(192,192,192) + "[" + rgb(255,0,0) + "ERROR" + rgb(192,192,192) + "]: " + reset
default_warn_tag  = rgb(192,192,192) + "[" + rgb(255,165,0) + "WARN" + rgb(192,192,192) + "]: " + reset
default_info_tag  = rgb(192,192,192) + "[" + rgb(255,255,0) + "INFO" + rgb(192,192,192) + "]: " + reset
default_success_tag=rgb(192,192,192) + "[" + rgb(0,255,0) + "SUCCESS" + rgb(192,192,192) + "]: " + reset


print(default_error_tag + "<insert error message here>")
print(default_warn_tag + "<insert warning message here>")
print(default_info_tag + "<insert info message here>")
print(default_success_tag + "<insert success message here>")



var = 1

print(type(var))
print("------------------")
var = str(var)
print(type(var))