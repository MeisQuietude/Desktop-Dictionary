import colorama
from colorama import Style, Fore, Back


class Color:
    """
    Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
    Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
    Style: DIM, NORMAL, BRIGHT, RESET_ALL
    """
    def __init__(self):
        colorama.init()

    def __del__(self):
        colorama.deinit()

    def red(self, text):
        return Fore.RED + text + Fore.RESET

    def green(self, text):
        return Fore.GREEN + text + Fore.RESET

    def yellow(self, text):
        return Fore.YELLOW + text + Fore.RESET

    def cyan(self, text):
        return Fore.CYAN + text + Fore.RESET


if __name__ == '__main__':
    clr = Color()
    print(clr.red('text'))
    print(clr.green('text') + ' text')
    print('text')
    clr.red('text')
