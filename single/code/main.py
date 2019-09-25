# -*- coding: utf-8 -*-

from modules.play import start_play
from modules.sysmod import *
from modules.render import origin

class startgame(object):

    def __init__(self, *args, **kwargs):
        start = 1
        player_select = 0
        while start == 1:
            clear()
            origin()
            player_select = correctInput()
            if player_select == 1:
                start_play()
            else:
                clear()
                print('\n    Возвращайтесь еще!\n')
                killProgram()

start = startgame()
