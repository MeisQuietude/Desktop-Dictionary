import os

import pymongo
from pymongo import MongoClient

from cfg import config


class Mongo:
    def __init__(self):
        self.url = config.get_url() or "mongodb://localhost:27017/"
        print("Connect to " + self.url)

        self.cluster_name = config.get_cluster() or "testDB"
        self.collection_name = config.get_collection() or "testCollection"

        self.client = MongoClient(self.url)
        self.db = self.client[self.cluster_name]
        self.collection = self.db[self.collection_name]

        print("Set to default cluster and collection.")
        print(self.cluster_name, self.collection_name, sep='  :  ')

        print("Connected\n")

    def __repr__(self):
        result = f"url: {self.url},\ncollection: {self.collection_name}\n"
        return result

    def __del__(self):
        self.db.close()
        print("Disconnected")

    @staticmethod
    def stdout_arrays(array:list, string:str):
        """ Output to arrays """
        print(string if string.endswith(":") else string + ":")
        for element in array:
            print('\t' + element)
        print()

    def show_available_dbs(self, out:bool = False):
        list_dbs = self.client.list_database_names()

        if out:
            self.stdout_arrays(list_dbs, f"Available clusters in this db")
        return list_dbs

    def show_available_collections(self, out:bool = False):
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

    def set_cluster(self, new_cluster):
        """ Set another DB """
        self.db = self.client[new_cluster]
        self.cluster_name = new_cluster

        self.collection = None

        if new_cluster not in self.show_available_dbs():
            print("~~ This cluster does not exist. ~~")
            print("~~     (It's not an error)      ~~")
        print("Cluster set to: " + self.cluster_name)
        print("Please, choose collection.")

    def set_collection(self, new_collection):
        """ Set another collection """
        self.collection = self.db[new_collection]
        self.collection_name = new_collection

        if new_collection not in self.show_available_collections():
            print("~~ This collection does not exist. ~~")
            print("~~       (It's not an error)       ~~")
        print("Collection set to: " + self.collection_name)


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
        print('Available commands:')
        print(*cmds, sep='; ')

    elif 'show dbs' == arg:
        client.show_available_dbs(out=True)
    elif 'show collections' == arg:
        client.show_available_collections(out=True)

    elif 'get db' == arg:
        db = client.get_cluster()
        print(db)
    elif 'get collection' == arg:
        collection = client.get_collection()
        print(collection)

    elif arg.startswith('use '):
        arg = arg[4:]
        client.set_cluster(arg)
    elif arg.startswith('set '):
        arg = arg[4:]
        client.set_collection(arg)

    else:
        print('Not available command')


if __name__ == '__main__':
    client = Mongo()

    while True:
        choose_param()
