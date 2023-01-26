from elasticsearch import Elasticsearch

NODES = [
    "http://localhost:9200"
]

client = Elasticsearch(NODES, basic_auth=("elastic", "heqwElWrxK8EE4tnmxlk"))


def insert(_tweet):
    _id = _tweet['id']
    _content = _tweet['content']
    _doc = {
        'id': _id,
        'content': _content
    }
    resp = client.index(index="twitter", id=_id, document=_doc)


def delete():
    resp = client.delete(index="customer", id=1)


def read():
    resp = client.get(index="customer", id=2)
    print("First Name: {}\nLast Name: {}".format(resp["_source"]["firstname"], resp["_source"]["lastname"]))


def search(prop, words):
    resp = client.search(index="customer", query={"match": {prop: words}})
    print(resp)
