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
    resp = client.delete(index="twitter", id=1)


def read(_id):
    resp = client.get(index="twitter", id=_id)
    return resp


def search(prop, words):
    resp = client.search(index="twitter", query={"match": {prop: words}})
    print(resp)


