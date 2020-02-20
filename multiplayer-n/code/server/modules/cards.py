from random import choice

def set_cards():
    name = ['ТУЗ', 'КОРОЛЬ', 'ДАМА', 'ВАЛЕТ', '10', '9',
            '8', '7', '6', '5', '4', '3', '2']
    mast = ['ПИКА', 'БУБА', 'КРЕСТА', 'ЧЕРВА']
    cards = []
    for card_ in name:
        for card in mast:
            _card = card_ + ' | ' + card
            cards.append(_card)
    return cards

def get_cards():
    cards = set_cards()
    return choice(cards)

def get_value(card):
    mas = card.split(' | ')
    mas1 = mas[0]
    if mas1 == 'ТУЗ':
        res = 11
    elif mas1 == 'КОРОЛЬ':
        res = 10
    elif mas1 == 'ДАМА':
        res = 10
    elif mas1 == 'ВАЛЕТ':
        res = 10
    else:
        res = int(mas1)
    return res
