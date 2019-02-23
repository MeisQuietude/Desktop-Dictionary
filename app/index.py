from db.db import Mongo
from cfg.user import User
from cfg.clear_console import cls
from cfg.valid_data import valid_pair
from cfg.color import Color

clr = Color()


class Local:
    def __init__(self):
        self.user = User()
        self.client = Mongo()

        self.client.set_user(self.user.username.lower())
        self.collections = [doc['name'] for doc in self.client.read({})]
        self.current = self.collections[0]

        self.words = self.client.read({'name': self.collections[0]})[0]['words']

        self.show_cols()

        while True:
            self.options()

    def show_cols(self):
        print(clr.cyan('Available collections:'))
        for col in self.collections:
            print("\t" + col)
        print()

    def set_col(self, col):
        if col not in self.collections:
            print('~~          This collection does not exist          ~~')
            print('~~ It is not an error if you want to create new one ~~')
        self.current = col
        self.words = self.client.read({'name': col})[0]['words']

    def get_words(self):
        return self.words

    def start_write(self):
        indent = "\t"
        print(indent + "Start write pairs like: " + clr.green('apple яблоко'))
        print(indent + "When you want to finish write just enter new line.")
        words = {}
        while True:
            pair = input(indent)
            if not pair.strip(): break
            try:
                en, ru = pair.lower().split()
                assert valid_pair(en, ru) is True
                words[en] = ru
            except ValueError:
                print('Invalid input')
            except AssertionError:
                print('Incorrect pair')
        self.client.update_user(self.current, words)

    @staticmethod
    def pretty(words: dict):
        for k, v in words.items():
            print(f"\t{k} : {v}")

    def options(self):
        """ USER OPTIONS """
        res = input("").strip().lower()
        if not res: return

        if res == 'exit':
            exit()
        elif res == 'clear':
            cls()
        elif res.startswith('set '):
            res = res[4:]
            # set to another (new) collection
            self.set_col(res.split()[0].strip())
        elif res == 'show':
            # show collections
            self.show_cols()
        elif res == 'read':
            # show word in collection
            self.pretty(self.get_words())
        elif res == 'write':
            # write word's pairs to collection
            self.start_write()
        elif res == 'test':
            # create some tests for learn
            pass


if __name__ == '__main__':
    Local()

else:
    exit(0)
