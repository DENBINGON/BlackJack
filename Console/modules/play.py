from .cards import *
from .sysmod import *
import time

def win():
    clear()
    print('    ВЫ ПОБЕДИЛИ')
    print(f'''
Нажмите Enter для новой игры
    ''')
    input()

def notwin():
    clear()
    print('    НИЧЬЯ')
    print(f'''
Нажмите Enter для новой игры
    ''')
    input()

def lose(player, nump):
    clear()
    print(f'''
    ВЫ ПРОИГРАЛИ''')
    print(f'''
Нажмите Enter для новой игры''')

    input()

def dealer_part(dealer, player):
    clear()
    dealer_time = 1
    numd = 0
    nump = 0
    print(f'''-------------------------
    Карты дилера:''')
    for card in dealer:
        numd += get_value(card)
        print(f'    {card}')
    print(f'''    Количество очков - {numd}

-------------------------
    Ваши карты:''')
    for card in player:
        nump += get_value(card)
        print(f'    {card}')
    print(f'    Количество очков - {nump}')

    time.sleep(5)
    while dealer_time == 1:
        if numd >= 17:
            if nump > numd:
                dealer_time = 2
                win()
            elif nump == numd:
                dealer_time = 2
                notwin()
            elif nump < numd:
                dealer_time = 2
                lose(dealer, player)
        elif numd > 21:
            dealer_time = 2
            win()
        else:
            dealer.append(get_cards())
            numd = 0
            for card in dealer:
                numd += get_value(card)

def start_play():
    clear()
    print('''
              +----------+
              | Начинаем |
              +----------+''')
    dealer = []
    player = []
    numd = 0
    nump = 0
    player_select = 1
    for i in range(2):
        dealer.append(get_cards())
        player.append(get_cards())
    for card in player:
        nump += get_value(card)
    numd = get_value(dealer[0])
    print(f'''
----------------------------------------
    Карты дилера:
    {dealer[0]}
    Скрыта
    Сумма очков = {numd}

    Ваши карты:
    {player[0]}
    {player[1]}
    Сумма очков = {nump}
----------------------------------------
''')
    if nump == 21:
        print('    BLACKJACK')
        dealer_part(dealer, player)
    else:
        print('''   Взять еще?
   1 - Да 2 - Нет
''')
        while player_select == 1:
            player_select = int(input('   Выбор --> '))
            if player_select == 1:
                clear()
                player.append(get_cards())
                print(f'''
----------------------------------------
    Карты дилера:
    {dealer[0]}
    Скрыта
    Сумма очков = {numd}

    Ваши карты:''')
                nump = 0
                for cardp in player:
                    print(f'    {cardp}')
                    nump += get_value(cardp)
                print(f'''    Сумма очков = {nump}
----------------------------------------
''')
            else:
                dealer_part(dealer, player)
            if nump < 21:
                print('''   Взять еще?
    1 - Да 2 - Нет
        ''')
            elif nump == 21:
                player_select = 2
            else:
                player_select = 2
                lose(player, nump)
