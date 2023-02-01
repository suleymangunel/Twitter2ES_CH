import clickhouse_connect
from decouple import config


class _Client:
    host = config('CH_HOST')
    port = int(config('CH_PORT'))
    username = config('CH_USERNAME')
    password = config('CH_PASSWORD')

    def client(self):
        return clickhouse_connect.get_client(host=self.host, port=self.port,
                                             username=self.username, password=self.password)


_client = _Client().client()


def get_top(top_limit):
    query = "SELECT id FROM twitter ORDER BY twitter.retweetCount+twitter.likeCount DESC LIMIT {}".format(top_limit)
    result = _client.query(query)
    return result


def insert(_tweet_counts):
    _id = str(_tweet_counts['id'])
    _retweetCount = _tweet_counts['retweetCount']
    _replyCount = _tweet_counts['replyCount']
    _likeCount = _tweet_counts['likeCount']
    _quoteCount = _tweet_counts['quoteCount']
    tweet_count = [_id, _retweetCount, _replyCount, _likeCount, _quoteCount]
    tweet_counts = [tweet_count]
    # ic = client.create_insert_context(table='twitter', data=tweet_counts, wait_for_async_insert=0)
    # client.insert(context=ic)
    query = ("INSERT INTO twitter SETTINGS async_insert=1, wait_for_async_insert=0 VALUES('{}',{},{},{},{})".
             format(_id, _retweetCount, _replyCount, _likeCount, _quoteCount))
    _client.query(query)


def delete(_id):
    query = "SET allow_experimental_lightweight_delete = true;"
    _client.client.query(query)
    query = "DELETE FROM twitter WHERE id='{}'".format(_id)
    result = _client.query(query)
    return result


def search(_id):
    query = "SELECT * FROM twitter WHERE id='{}'".format(_id)
    result = _client.query(query)
    return result


def update(_id):
    query = "UPDATE twitter VALUES() WHERE id='{}'".format(_id)
    result = _client.query(query)
    return result
