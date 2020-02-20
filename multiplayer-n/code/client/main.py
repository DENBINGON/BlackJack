# -*- coding: utf-8 -*-

#from modules.play import start_play
from modules.sysmod import *
from modules.render import origin
from modules.settings import settings
ip = None
port = None
nick = None
class game(object):

    def __init__(self, *args, **kwargs):
        start = 1
        player_select = 0

        while start == 1:

            clear()
            origin()

            player_select = correctInput()

            if player_select == 1:
                start_find() #не начато
            elif player_select == 2:
                settings(ip, port, nick)
            else:
                clear()
                print('\n    Возвращайтесь еще!\n')
                killProgram()

start = game()
