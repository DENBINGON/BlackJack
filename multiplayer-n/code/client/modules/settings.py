from .sysmod import *
from .render import *
def settings(ip, port, nick):
    clear()
    viewSettings(ip, port, nick)
    select = correctInput()
