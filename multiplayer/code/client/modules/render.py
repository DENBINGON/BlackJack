# -*- coding: utf-8 -*-

from .sysmod import *

def origin():
    print('''
    Добро пожаловать в консольный BLACKJACK - MULTIPLAYER (beta)
    Раз - раб : DENBINGON
    GiT : https://github.com/denbingon/
    VK : https://vk.com/denbingon

    Начать - 1
    Настройки - 2
    Выход - 3

    ''')

def black_win():
    clear()
    print('''
    ██████████████████████████████████████████████████████
    █────███─████────██────██─██─████──██────██────██─██─█
    █─██──██─████─██─██─██─██─█─██████─██─██─██─██─██─█─██
    █────███─████────██─█████──███████─██────██─█████──███
    █─██──██─████─██─██─██─██─█─███─██─██─██─██─██─██─█─██
    █────███───██─██─██────██─██─██────██─██─██────██─██─█
    ██████████████████████████████████████████████████████
    ''')
    input('''
Нажмите Enter для новой игры
    ''')

def win():
    clear()
    print('\n    ВЫ ПОБЕДИЛИ')
    print('''
Нажмите Enter для новой игры
    ''')
    input()

def notwin():
    clear()
    print('\n    НИЧЬЯ')
    print(f'''
Нажмите Enter для новой игры
    ''')
    input()

def lose(cardp, cardd, nump, numd, stat):
    clear()
    print('''
    ВЫ ПРОИГРАЛИ''')
    views_card(cardp, cardd, nump, numd, stat)
    print('''
Нажмите Enter для новой игры''')
    input()

def views_card(cardp, cardd, nump, numd, stat):
    print(f'''
+-------------------------------------+
    КАРТЫ ДИЛЕРА:                                                ''')

    if stat != 1:
        for card in cardd:
            print('    ' + card)
    else:
        print('    ' + cardd[0] + '\n    СКРЫТО')

    print(f'''
    СУММА ОЧКОВ:    {numd}
+-------------------------------------+

+-------------------------------------+
    ВАШИ КАРТЫ:                                                  ''')
    for card in cardp:
        print('    ' + card)
    print(f'''
   СУММА ОЧКОВ:    {nump}                                                ''')
    print(f'''+-------------------------------------+''')

def begin():
    print('''
              +----------+
              | Начинаем |
              +----------+''')

def questionAddCard():
    print('''   Взять еще?
   1 - Да 2 - Нет
''')

def viewSettings(ip, port, nick):
    print(f"""
    ###--->     НАСТРОЙКИ     <---###

    Адресс сервера -> {ip}:{port}
    Ваше имя       -> {nick}

    ###--->     =========     <---###

    Изменить адресс      -> 1
    Изменить имя         -> 2
    Выход в главное меню -> 3

    ###--->     =========     <---###
    """)
