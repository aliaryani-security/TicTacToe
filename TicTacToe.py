#!/usr/bin/env python3
import os
import random

while True:
    os.system('clear')
    from api import *
    print (f'''
           {ph1} | {ph2} | {ph3}
           ----------
           {ph4} | {ph5} | {ph6}
           ----------
           {ph7} | {ph8} | {ph9}
           ''')
    try:
        winConditions()
        inp = int(input('choose a number: '))
        gamePlayer(inp)
    except ValueError:
        print('wrong choice! choose between 1-9')
        input('press any key to continue...')
    except BrokenPipeError:
        print ('already taken! try again')
        input('press any key to continue...')
    except OverflowError:
        print('Game Over!')
        break
    except RecursionError:
        print('Game Over!')
        break
    except ArithmeticError:
        print('You win!', 2)
        break
    except AttributeError:
        print('You lost!', 5)
        break
