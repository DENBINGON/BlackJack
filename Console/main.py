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
            try:
                try:
                    start = int(input('    Выбор --> '))
                except:
                    start = int(input('    Выбор --> ')[:-1])
                if start == 2:
                    clear()
                    print('\n    Возвращайтесь еще!\n')
                    input()
                else:
                    start_play()
            except:
                wrongInput()


start = startgame()
