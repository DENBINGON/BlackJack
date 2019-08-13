from .cards import *
from .sysmod import clear

def lose():
    clear()
    print('''
    ВЫ ПРОИГРАЛИ
    нажмите Enter для новой игры
    ''')
    input()
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
    else:
        print('''   Взять еще?
    1 - Да 2 - Нет
''')
        while player_select == 1:
            player_select = int(input('    Выбор --> '))
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
            if nump < 21:
                print('''   Взять еще?
    1 - Да 2 - Нет
        ''')
            elif nump == 21:
                player_select = 2
            else:
                player_select = 2
                lose()
