import os

def load_credentials() -> dict:
    return {
        'ACCESS_TOKEN' : os.environ['ACCESS_TOKEN'],
        'ACCESS_SECRET' : os.environ['ACCESS_TOKEN_SECRET'],
        'CONSUMER_KEY' : os.environ['CONSUMER_KEY'],
        'CONSUMER_SECRET' : os.environ['CONSUMER_SECRET']
    }