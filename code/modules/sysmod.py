import os, time

def clear():
    try:
        os.system('cls')
    except:
        os.system('clear')

def wrongInput_cls():
    clear()
    print('\n    Неизвестный ответ, попробуйте еще!')
    time.sleep(1)

def wrongInput():
    print('    Неизвестный ответ, попробуйте еще!')

def killProgram():
    raise SystemExit

def correctInput():
    true = 1
    nums = [1, 2]
    while true == 1:
        try:
            num = int(input('    Выбор --> '))
            if num in nums:
                true = 2
            else:wrongInput()
        except:wrongInput()
    return num
