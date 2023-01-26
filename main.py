import ElasticSearchUnit as ESu
import ClickHouseUnit as CHu
import TwitterClient as TWc

if __name__ == '__main__':
    print("Tweets collecting...")
    tweets = TWc.get_tweet()
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

