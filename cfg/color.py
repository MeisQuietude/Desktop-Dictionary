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
        return Fore.RED + text + self.reset()

    def green(self, text):
        return Fore.GREEN + text + self.reset()

    def yellow(self, text):
        return Fore.YELLOW + text + self.reset()

    def yel_light(self, text):
        return Fore.LIGHTYELLOW_EX + text + self.reset()

    def cyan(self, text):
        return Fore.CYAN + text + self.reset()

    def magenta(self, text):
        return Fore.MAGENTA + text + self.reset()

    def pw(self):
        return Fore.BLACK + Back.BLACK

    @staticmethod
    def reset():
        return Style.RESET_ALL


if __name__ == '__main__':
    clr = Color()
    print(clr.red('text'))
    print(clr.green('text') + ' text')
    print('text')
    clr.red('text')
