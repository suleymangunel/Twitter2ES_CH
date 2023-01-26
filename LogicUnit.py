import ElasticSearchUnit as ESu
import ClickHouseUnit as CHu
import TwitterClient as TWc


def get_top_tweets(top_limit):
    result_ch = CHu.get_top(top_limit)
    results_es = []
    for _res in result_ch.result_rows:
        _id = _res[0]
        result_es = ESu.read(_id)
        results_es.append(result_es)
    return results_es


def collect_tweets():
    print("Tweets collecting...")
    tweets = TWc.get_tweet()
    print("Tweets collected: {}".format(len(tweets)))
    for tweet in tweets:
        _tweet = {'id': tweet.id, 'content': tweet.rawContent}
        _tweet_counts = {'id': tweet.id,
                         'retweetCount': tweet.retweetCount,
                         'replyCount': tweet.replyCount,
                         'likeCount': tweet.likeCount,
                         'quoteCount': tweet.quoteCount}
        print(_tweet_counts)
        ESu.insert(_tweet)
        CHu.insert(_tweet_counts)
