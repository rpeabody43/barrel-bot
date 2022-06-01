import tweepy
import twitter.credentials as creds
import requests

def authenticate () -> tweepy.Client:
    auth = creds.load_credentials()
    client = tweepy.Client(
        consumer_key=auth['CONSUMER_KEY'], 
        consumer_secret=auth['CONSUMER_SECRET'], 
        access_token=auth['ACCESS_TOKEN'], 
        access_token_secret=auth['ACCESS_SECRET']
        )
    return client

def test_tweet ():
    client = authenticate()
    while True:
        tweet = input('TWEET: ')
        response = client.create_tweet(text=tweet)
        print(response)

def fmt_tweet (pitch: dict) -> str:
    return ''
