# -*- coding: utf-8 -*-

from modules.play import start_play
from modules.sysmod import clear
from modules.render import origin

class startgame(object):

    def __init__(self, *args, **kwargs):
        start = 1
        while start == 1:
            clear()
            origin()
            start = int(input('    Выбор --> '))
            if start == 2:
                clear()
                print('\n    Возвращайтесь еще!\n')
                input()
            else:
                start_play()

start = startgame()
