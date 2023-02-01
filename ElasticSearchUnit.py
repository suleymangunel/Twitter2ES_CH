from decouple import config
from elasticsearch import Elasticsearch


# NODES = [
#     config('ES_HOST')
# ]
#
# client = Elasticsearch(NODES, basic_auth=(config('ES_USERNAME'), config('ES_PASSWORD')))


class _Client:
    NODES = [config('ES_HOST')]
    username = config('ES_USERNAME')
    password = config('ES_PASSWORD')

    def client(self):
        return Elasticsearch(self.NODES, basic_auth=(self.username, self.password))


_client = _Client().client()


def insert(_tweet):
    _id = _tweet['id']
    _content = _tweet['content']
    _doc = {
        'id': _id,
        'content': _content
    }
    resp = _client.index(index="twitter", id=_id, document=_doc)


def delete():
    resp = _client.delete(index="twitter", id=1)


def read(_id):
    resp = _client.get(index="twitter", id=_id)
    return resp


def search(prop, words):
    resp = _client.search(index="twitter", query={"match": {prop: words}})
    print(resp)
