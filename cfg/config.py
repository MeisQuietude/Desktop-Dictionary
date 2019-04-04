
__version__ = '0.7.0'


def get_url():
    url = "mongodb+srv://admin:admin@dictionary-xtkrz.azure.mongodb.net/test?retryWrites=true"  # Null for localhost
    return url


def get_cluster():
    db = "users"  # Null for 'testCollection'
    return db


def get_collection():
    collection = "data"  # Null for 'testDB'
    return collection


if __name__ == '__main__':
    print("It's config file. Don't touch it if you don't know what are you doing.")
