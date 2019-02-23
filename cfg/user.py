from db import db
from time import sleep

from cfg.clear_console import cls
from cfg.color import Color
clr = Color()


class User:
    def __init__(self):
        self.username = None
        self.pw = None
        self.collection = []
        self.client = db.Mongo()
        self.access = False

        self.get_access()

    def add_to_collection(self, data):
        self.collection.append(data)

    def get_collection(self):
        return self.collection

    def enter_data(self):
        while not self.username:
            self.username = input(clr.yellow("Username: ")).strip()
        while not self.pw:
            self.pw = input(clr.yellow("Password: "))

    def check_valid(self):
        valid = self.client.user_validate(self.username, self.pw)

        if not valid:
            self.username = None
            self.pw = None
            print(clr.red("Invalid username or password..."))
            response = input("Register new account (reg) or Try again (anything except 'reg')?\n")
            if response == 'reg':
                if self.client.user_reg():
                    self.access = True
        else:
            self.access = True

    def get_access(self):
        while not self.access:
            self.enter_data()
            self.check_valid()
        print(clr.green("Access granted!"))
        sleep(1)
        cls()


if __name__ == '__main__':
    User()
