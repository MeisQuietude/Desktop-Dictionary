import random
from cfg.color import Color
clr = Color()


def play_en(words: dict):
    print("I ask you only english words now.")
    print(clr.cyan("Start to play :>"))
    pass


def play_ru(words: dict):
    print("I ask you only russian words now.")
    print(clr.cyan("Start to play :>"))
    pass


def play_mix(words: dict):
    print("I ask you only both english and russian words now.")
    print(clr.cyan("Start to play :>"))
    pass
