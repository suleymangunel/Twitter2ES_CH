from typing import Dict, Union

import tweepy
import snscrape.modules.twitter as sntwitter
import ElasticSearchUnit as ESu
import ClickHouseUnit as CHu


def get_tweets_from_elon_musk():
    query = "from:@elonmusk"
    tweets = []
    for tweet in sntwitter.TwitterSearchScraper(query).get_items():
        _tweet: dict[str, Union[str, int]] = {'id': tweet.id, 'content': tweet.rawContent}
        _tweet_counts = {'id': tweet.id, 'retweetCount': tweet.retweetCount, 'replyCount': tweet.replyCount,
                         'likeCount': tweet.likeCount, 'quoteCount': tweet.quoteCount}
        print(_tweet, _tweet_counts)
        ESu.insert(_tweet)
        CHu.insert(_tweet_counts)


def get_tweet():
    query = "python"
    tweets = []
    limit = 30
    for tweet in sntwitter.TwitterSearchScraper(query).get_items():
        if tweet.retweetCount * tweet.replyCount * tweet.likeCount * tweet.quoteCount > 0:
            if len(tweets) >= limit:
                return tweets
            else:
                tweets.append(tweet)
