import random
from cfg.color import Color

clr = Color()


def play_kv(words: dict):
    print(clr.cyan("Choose game mode now:"))
    print("~ 1: only first word in pair")
    print("~ 2: only second word in pair")
    print("~ 3: all words in pair")
    print(clr.cyan("~ 3 is default."))
    try:
        ans = int(input("Game mod: "))
        assert 0 < ans < 4
    except ValueError:
        ans = 3
    except AssertionError:
        ans = 3
    print(clr.cyan(f"Start to play game mode {ans} :>"))
    play(words, ans)


def play(words: dict, rule: int):
    indent = '\t'
    ask = [x for x in words]
    print(random.choice([x for x in words]))


if __name__ == '__main__':
    d = {'apple': 'яблоко', 'orange': 'апельсин'}
    play_kv(d)
