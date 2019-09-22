import os, time

def clear():
    try:
        os.system('cls')
    except:
        os.system('clear')

def wrongInput():
    clear()
    print('\n    Please, try again!')
    time.sleep(3)

def killProgram():
    raise SystemExit
