import os
from cfg.color import Color
from cfg.config import __version__

clr = Color()


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Program : ' + clr.yel_light('Language Dictionary'))
    print('Author  : ' + clr.yel_light('Mr. Quietude'))
    print('Version : ' + clr.yel_light(__version__))
    print()


if __name__ == '__main__':
    cls()

