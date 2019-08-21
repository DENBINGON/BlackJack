from .cards import *
from .sysmod import *
from .render import *
import time

def dealer_part(dealer, player):
    clear()
    dealer_time = 1
    numd = 0
    nump = 0

    for card in dealer:
        numd += get_value(card)

    for card in player:
        nump += get_value(card)

    views_card(player, dealer, nump, numd, 2)

    while dealer_time == 1:
        time.sleep(0.7)
        if numd > 21:
            dealer_time = 2
            win()
        elif numd >= 17:
            if nump > numd:
                dealer_time = 2
                win()
            elif nump == numd:
                dealer_time = 2
                notwin()
            elif nump < numd:
                dealer_time = 2
                lose(player, dealer, nump, numd, 2)
        else:
            dealer.append(get_cards())
            numd = 0
            for card in dealer:
                numd += get_value(card)
            clear()
            views_card(player, dealer, nump, numd, 2)

def start_play():
    # block hello
    clear()
    begin()
    time.sleep(1.5)
    clear()
    #block memories
    dealer = []
    player = []
    numd = 0
    nump = 0
    player_select = 1
    #block game #1
    for i in range(2):
        dealer.append(get_cards())
        player.append(get_cards())
    for card in player:
        nump += get_value(card)
    numd = get_value(dealer[0])
    views_card(player, dealer, nump, numd, 1)
    if nump == 21:
        print('    BLACKJACK')
        dealer_part(dealer, player)
    else:
        questionAddCard()
        while player_select == 1:
            player_select = int(input('   Выбор --> '))
            if player_select == 1:
                clear()
                player.append(get_cards())
                nump = 0
                for card in player:
                    nump += get_value(card)
                views_card(player, dealer, nump, numd, 1)

            else:
                dealer_part(dealer, player)

            if nump < 21:
                questionAddCard()
            elif nump == 21:
                player_select = 2
            else:
                player_select = 2
                lose(player, dealer, nump, numd, 2)
