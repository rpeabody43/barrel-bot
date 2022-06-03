import tweepy
import twitter.credentials as creds
from twitter.formatting import hashtags, outcomes 

def authenticate () -> tweepy.API:
    keys = creds.load_credentials()
    auth = tweepy.OAuthHandler(keys['CONSUMER_KEY'], keys['CONSUMER_SECRET'])
    auth.set_access_token(keys['ACCESS_TOKEN'], keys['ACCESS_SECRET'])
    api = tweepy.API(auth)

    return api

def test_tweet ():
    api = authenticate()
    while True:
        tweet = input('DAY: ')
        response = api.update_status(tweet)
        print(response)

def tweet_with_video (pitch: dict, filepath: str):
    text = _fmt_tweet(pitch)
    api = authenticate()
    media: tweepy.Media = api.media_upload(filepath, media_category='tweet_video')
    id = media.media_id_string
    # print(media)
    response = api.update_status(status=text, media_ids=[id])
    # print(response)

def _fmt_tweet (pitch: dict):
    print(pitch)
    date = pitch['date']
    hitter_name = pitch['batter_name']
    pitcher_name = pitch['pitcher_name']
    team_hashtag = hashtags[pitch['batting_team']]
    outcome = outcomes[pitch['outcome']]
    ev = pitch['velo']
    ang = pitch['ang']
    lines = [ 
        f'{hitter_name} off {pitcher_name}',
        f'🔥 {ev} mph, {ang}°',
        outcome,
        '',
        team_hashtag]

    out = ''
    for str in lines:
        out += str + '\n'
    out = out[:len(out)-1]

    return out
