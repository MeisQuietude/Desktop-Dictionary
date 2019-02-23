from db.db import Mongo
from cfg.user import User
from cfg.color import Color
clr = Color()


class Local:
    def __init__(self):
        self.user = User()
        self.client = Mongo()

        self.client.set_user(self.user.username.lower())
        self.collections = [doc['name'] for doc in self.client.read({})]

        self.show_cols()

    def show_cols(self):
        print(clr.cyan('Available collections:'))
        for col in self.collections:
            print("\t" + col)
        print()


    def options(self):
        """ USER OPTIONS """
        res = input("").strip().lower()
        if not res: return

        if res == 'exit':
            exit()
        elif res.startswith('set '):
            res = res[4:]
            # set to another (new) collection
            pass
        elif res == 'show':
            # show collections
            pass
        elif res == 'read':
            # show word in collection
            pass
        elif res == 'write':
            # write word's pairs to collection
            pass




if __name__ == '__main__':
    Local()
else:
    exit(0)
