from db import db


class User:
    def __init__(self):
        self.username = None
        self.pw = None
        self.collections = []
        self.client = db.Mongo()
        self.access = False

        self.get_access()

    def enter_data(self):
        self.username = input("Username: ").strip()
        self.pw = input("Password: ")

    def check_valid(self):
        valid = self.client.user_validate(self.username, self.pw)

        if not valid:
            print("Invalid username or password..")
            response = input("Register (reg) or Try again (anything except 'reg')?\n")
            if response == 'reg':
                if self.client.user_reg():
                    self.access = True
        else:
            self.access = True

    def get_access(self):
        while not self.access:
            self.enter_data()
            self.check_valid()
        print("Access granted!")


if __name__ == '__main__':
    User()
