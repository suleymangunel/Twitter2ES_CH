import tweepy
import snscrape.modules.twitter as sntwitter


def get_tweet():
    query = "python"
    tweets = []
    limit = 30
    for tweet in sntwitter.TwitterSearchScraper(query).get_items():
        if tweet.retweetCount*tweet.replyCount*tweet.likeCount*tweet.quoteCount > 0:
            if len(tweets) >= limit:
                return tweets
            else:
                tweets.append(tweet)









