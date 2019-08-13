import os

def clear():
    try:
        os.system('cls')
    except:
        os.system('clear')
