#Lenesis
import random
import time

ph1 = '1'
ph2 = '2'
ph3 = '3'
ph4 = '4'
ph5 = '5'
ph6 = '6'
ph7 = '7'
ph8 = '8'
ph9 = '9'
cnt = 0

#* Winning Conditions
def winConditions():
    if ph1 == 'O' and ph2 == 'O' and ph3 == 'O':
        raise ArithmeticError
    if ph1 == 'O' and ph4 == 'O' and ph7 == 'O':
        raise ArithmeticError
    if ph1 == 'O' and ph5 == 'O' and ph9 == 'O':
        raise ArithmeticError
    if ph2 == 'O' and ph5 == 'O' and ph8 == 'O':
        raise ArithmeticError
    if ph3 == 'O' and ph5 == 'O' and ph7 == 'O':
        raise ArithmeticError
    if ph3 == 'O' and ph6 == 'O' and ph9 == 'O':
        raise ArithmeticError
    if ph4 == 'O' and ph5 == 'O' and ph6 == 'O':
        raise ArithmeticError
    if ph7 == 'O' and ph8 == 'O' and ph9 == 'O':
        raise ArithmeticError
    #!Opponent
    if ph1 == 'X' and ph2 == 'X' and ph3 == 'X':
        raise AttributeError
    if ph1 == 'X' and ph4 == 'X' and ph7 == 'X':
        raise AttributeError
    if ph1 == 'X' and ph5 == 'X' and ph9 == 'X':
        raise AttributeError
    if ph2 == 'X' and ph5 == 'X' and ph8 == 'X':
        raise AttributeError
    if ph3 == 'X' and ph5 == 'X' and ph7 == 'X':
        raise AttributeError
    if ph3 == 'X' and ph6 == 'X' and ph9 == 'X':
        raise AttributeError
    if ph4 == 'X' and ph5 == 'X' and ph6 == 'X':
        raise AttributeError
    if ph7 == 'X' and ph8 == 'X' and ph9 == 'X':
        raise AttributeError
    

def gamePlayer(inp):
    playerController(inp)
    time.sleep(.5)
    #!GameOver
    if cnt >= 9:
        raise OverflowError
    else:
        opponentController()
        
def playerController(inp):
    global ph1
    global ph2
    global ph3
    global ph4
    global ph5
    global ph6
    global ph7
    global ph8
    global ph9
    global cnt
    if inp == 1:
        if ph1 == '1':
            ph1 = 'O'
            cnt += 1
        else:
            raise BrokenPipeError
    elif inp == 2:
        if ph2 == '2':
            ph2 = 'O'
            cnt += 1
        else:
            raise BrokenPipeError
    elif inp == 3:
        if ph3 == '3':
            ph3 = 'O'
            cnt += 1
        else:
            raise BrokenPipeError
    elif inp == 4:
        if ph4 == '4':
            ph4 = 'O'
            cnt += 1
        else:
            raise BrokenPipeError
    elif inp == 5:
        if ph5 == '5':
            ph5 = 'O'
            cnt += 1
        else:
            raise BrokenPipeError
    elif inp == 6:
        if ph6 == '6':
            ph6 = 'O'
            cnt += 1
        else:
            raise BrokenPipeError
    elif inp == 7:
        if ph7 == '7':
            ph7 = 'O'
            cnt += 1
        else:
            raise BrokenPipeError
    elif inp == 8:
        if ph8 == '8':
            ph8 = 'O'
            cnt += 1
        else:
            raise BrokenPipeError
    elif inp == 9:
        if ph9 == '9':
            ph9 = 'O'
            cnt += 1
        else:
            raise BrokenPipeError
    else:
        raise ValueError

def opponentController():
    global ph1
    global ph2
    global ph3
    global ph4
    global ph5
    global ph6
    global ph7
    global ph8
    global ph9
    global cnt
    inp = random.randrange(1, 10)
    if inp == 1:
        if ph1 == '1':
            ph1 = 'X'
            cnt += 1
        else:
            opponentController()
    elif inp == 2:
        if ph2 == '2':
            ph2 = 'X'
            cnt += 1
        else:
            opponentController()
    elif inp == 3:
        if ph3 == '3':
            ph3 = 'X'
            cnt += 1
        else:
            opponentController()
    elif inp == 4:
        if ph4 == '4':
            ph4 = 'X'
            cnt += 1
        else:
            opponentController()
    elif inp == 5:
        if ph5 == '5':
            ph5 = 'X'
            cnt += 1
        else:
            opponentController()
    elif inp == 6:
        if ph6 == '6':
            ph6 = 'X'
        else:
            opponentController()
    elif inp == 7:
        if ph7 == '7':
            ph7 = 'X'
            cnt += 1
        else:
            opponentController()
    elif inp == 8:
        if ph8 == '8':
            ph8 = 'X'
            cnt += 1
        else:
            opponentController()
    elif inp == 9:
        if ph9 == '9':
            ph9 = 'X'
            cnt += 1
        else:
            opponentController()

