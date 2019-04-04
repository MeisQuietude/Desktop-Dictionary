import os

import pymongo
from pymongo import MongoClient

from cfg import config
from cfg.valid_data import valid_mail
from cfg.color import Color

clr = Color()


def stdout(*text, sep=' ', end=''):
    if not debug: return
    print(*text, sep, end)


class Mongo:
    def __init__(self):
        self.url = config.get_url() or "mongodb://localhost:27017/"
        stdout("Connect to " + clr.yellow(self.url))

        self.cluster_name = config.get_cluster() or "testDB"
        self.collection_name = config.get_collection() or "testCollection"

        self.client = MongoClient(self.url)
        self.db = self.client[self.cluster_name]
        self.collection = self.db[self.collection_name]

        stdout("Set to default cluster and collection.")
        stdout(self.cluster_name, self.collection_name, sep='  :  ')

        stdout("Connected\n")

    def __repr__(self):
        result = f"url: {self.url},\ncluster: {self.cluster_name}\ncollection: {self.collection_name}\n"
        return result

    def __del__(self):
        self.client.close()
        stdout("Disconnected")

    @staticmethod
    def stdout_arrays(array: list, string: str):
        """ Output to arrays """
        stdout(string if string.endswith(":") else string + ":")
        for element in array:
            stdout('\t' + element)
        stdout()

    def show_available_dbs(self, out: bool = False):
        list_dbs = self.client.list_database_names()

        if out:
            self.stdout_arrays(list_dbs, f"Available clusters in this db")
        return list_dbs

    def show_available_collections(self, out: bool = False):
        list_collections = self.db.list_collection_names()

        if out:
            self.stdout_arrays(list_collections, f"Available collections in {self.cluster_name}")
        return list_collections

    def get_cluster(self):
        """ Get current DB """
        return self.cluster_name

    def get_collection(self):
        """ Get current collection """
        return self.collection_name

    def set_user_collections(self):
        self.set_cluster('user-collections')
        self.set_collection('collections')

    def set_user_data(self):
        self.set_cluster(config.get_cluster())
        self.set_collection(config.get_collection())

    def set_new_collection(self, username, collection):
        username = username.lower()
        self.set_user_data()
        self.collection.update_one({'username.private':username}, {'$push' : {'collections' : collection}})
        self.set_user_collections()

    def set_cluster(self, new_cluster):
        """ Set another DB """
        self.db = self.client[new_cluster]
        self.cluster_name = new_cluster

        self.collection = None

        if new_cluster not in self.show_available_dbs():
            stdout("~~ This cluster does not exist. ~~")
            stdout("~~     (It's not an error)      ~~")
        stdout("Cluster set to: " + self.cluster_name)
        stdout("Please, choose collection.")

    def set_collection(self, new_collection):
        """ Set another collection """
        self.collection = self.db[new_collection]
        self.collection_name = new_collection

        if new_collection not in self.show_available_collections():
            stdout(clr.yellow("~~            This collection does not exist.                  ~~"))
            stdout("~~  (It's not an error, if you want to create new collection)  ~~")
        stdout("Collection set to: " + self.collection_name)

    def new_user(self, *args):
        """ Insert to DB """
        invalid = filter(lambda x: type(x) is not dict, args)
        args = filter(lambda x: type(x) is dict, args)
        for arg in args:
            self.collection.insert_one(arg)
            stdout(f'Inserted: {arg}')

        print(clr.green('~~ DONE ~~'))

        for arg in invalid:
            stdout(f'{type(arg)} ~~ INVALID DOCUMENT: {arg}')

    def update_user(self, name: str, docs: dict):
        """ Work with user's DATABASE """

        for en, ru in docs.items():
            new_value = {'$set': {f'words.{en}': ru}}
            self.collection.update_one({'name': name}, new_value, upsert=True)
            stdout(f'Updated: {en} : {ru}')

        print(clr.green('~~ DONE ~~'))

    def read(self, params=None):
        """ Read from DB """
        if params is None:
            params = {}
        result = self.collection.find(params)
        return result

    def user_validate(self, username: str, pw: str):
        """ Used for check users """
        if self.collection.find_one({'username.private': username.lower(), 'pw': pw}):
            return True
        return False

    def user_reg(self):
        stdout("Register new account...")

        # EMAIL
        email = None
        while not email:
            email = input("Email: ").lower()
            if not valid_mail(email):
                print("Your email " + clr.red("is not ") + "correct. Try again...")
                email = None

        if self.collection.find_one({'email': email}):
            stdout("This email is already exist.")
            return False

        # USERNAME
        print('Username ' + clr.red("can't") + ' exist any specific symbols, '
              + clr.red("can't") + "start's with digit.")
        username = None
        while not username:
            username = input("Username: ")

        if self.collection.find_one({'username.private': username.lower()}):
            stdout("This username is already exist.")
            return False

        # PASSWORD
        pw = 0
        pw_conf = 1
        while pw != pw_conf:
            pw = input("Password: ")
            pw_conf = input("Confirm password: ")

        self.new_user({'email': email,
                       'username': {'public': username, 'private': username.lower()},
                       'pw': pw, 'collections': [], 'default': 'trial'
                       })

        # DONE
        return True


def choose_param():
    """ For switch-case construction """
    arg = input()

    if 'exit' == arg:
        exit(0)
    elif 'help' == arg:
        cmds = (
            'exit', 'show dbs', 'show collections', 'get db', 'get collection',
            'use *db*', 'set *collection*'
        )
        stdout('Available commands:')
        stdout(*cmds, sep='; ')

    elif 'show dbs' == arg:
        client.show_available_dbs(out=True)
    elif 'show collections' == arg:
        client.show_available_collections(out=True)

    elif 'get db' == arg:
        db = client.get_cluster()
        stdout(db)
    elif 'get collection' == arg:
        collection = client.get_collection()
        stdout(collection)

    elif arg.startswith('use '):
        arg = arg[4:]
        client.set_cluster(arg)
    elif arg.startswith('set '):
        arg = arg[4:]
        client.set_collection(arg)

    elif arg.startswith('read'):
        arg = {}
        result = client.read(arg)

        for doc in result.limit(20):
            stdout(doc)

    else:
        stdout('Not available command')


if __name__ == '__main__':
    debug = True
    client = Mongo()

    while True:
        choose_param()
else:
    debug = False
