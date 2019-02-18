
def get_url():
    url = ""  # Null for localhost
    return url


def get_cluster():
    db = "dictionary"  # Null for 'testCollection'
    return db


def get_collection():
    collection = "eng-ru"  # Null for 'testDB'
    return collection


if __name__ == '__main__':
    print("It's config file. Don't touch it if you don't know what are you doing.")
