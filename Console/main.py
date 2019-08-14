from modules.play import *
from modules.sysmod import clear

start = 1

while start == 1:
    clear()
    print('''
    Добро пожаловать в консольный BLACKJACK
    Раз - раб : DENBINGON
    GiT : https://github.com/denbingon/
    VK : https://vk.com/denbingon
    Новая игра - 1 Выход - 2
    ''')

    start = int(input('    Выбор --> '))

    if start == 2:
        clear()
        print('\n    Возвращайтесь еще!\n')
    else:
        start_play()
