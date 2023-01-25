from elasticsearch import Elasticsearch

NODES = [
    "http://localhost:9200"
]

client = Elasticsearch(NODES, basic_auth=("elastic", "heqwElWrxK8EE4tnmxlk"))

doc = {
    'firstname': 'author_name',
    'lastname': 'Interensting content...'
}


def insert():
    resp = client.index(index="customer", id=1, document=doc)


def delete():
    resp = client.delete(index="customer", id=1)


def read():
    resp = client.get(index="customer", id=2)
    print("First Name: {}\nLast Name: {}".format(resp["_source"]["firstname"], resp["_source"]["lastname"]))


def search(prop, words):
    resp = client.search(index="customer", query={"match": {prop: words}})
    print(resp)


def main():
    search("firstname", "claire")
