from os import getenv
from dotenv import load_dotenv

def load_credentials() -> dict:
    load_dotenv()
    return {
        'ACCESS_TOKEN' : getenv('ACCESS_TOKEN'),
        'ACCESS_SECRET' : getenv('ACCESS_TOKEN_SECRET'),
        'CONSUMER_KEY' : getenv('CONSUMER_KEY'),
        'CONSUMER_SECRET' : getenv('CONSUMER_SECRET')
    }