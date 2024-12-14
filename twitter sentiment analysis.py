import tweepy
from textblob import TextBlob
def twitter_sentiment_analysis():
    consumer_key = 'your_consumer_key'
    consumer_secret = 'your_consumer_secret'
    access_token = 'your_access_token'
    access_token_secret = 'your_access_token_secret'
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    tweet = input("Enter tweet to analyze: ")
    analysis = TextBlob(tweet)
    print(f"Sentiment: {analysis.sentiment}")
twitter_sentiment_analysis()
