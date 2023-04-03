import tweepy

from .credentials import load_credentials
from .formatting import hashtags, outcomes

def authenticate () -> tweepy.API:
    keys = load_credentials()
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

def tweet_with_video (pitch: dict, filepath: str, reply: int = None):
    text = _fmt_tweet(pitch)
    is_reply = reply != None
    if is_reply:
        text = '@mlb_barrels\nHere\'s the hardest hit ball that left the yard yesterday\n' + text
    api = authenticate()
    media: tweepy.Media = api.media_upload(filepath, media_category='tweet_video')
    media_id = media.media_id_string
    # print(media)
    response: tweepy.Tweet = api.update_status(status=text, media_ids=[media_id], in_reply_to_status_id=reply)
    id = response.id
    return id
    # print(response)

def _fmt_tweet (pitch: dict):
    print(pitch)
    date = pitch['date']
    hitter_name = pitch['batter_name']
    pitcher_name = pitch['pitcher_name']

    tweet_with_hashtag: bool = True
    try:
        team_hashtag = hashtags[pitch['batting_team']]
    except KeyError:
        htag_key = pitch['batting_team']
        print(f'exception on hashtag key {htag_key}')
        tweet_with_hashtag = False
    
    outcome = outcomes[pitch['outcome']]
    ev = pitch['velo']
    ang = pitch['ang']
    xba = '{0:.3f}'.format(float(pitch['xba']))
    if pitch['xba'] != 1.0:
        xba = xba[1:]
    lines = [ 
        f'{hitter_name} off {pitcher_name}',
        f'🔥 {ev} mph, {ang}°',
        f'{outcome} ({xba} xBA)',
        '']

    if tweet_with_hashtag: lines.append(team_hashtag)

    out = ''
    for str in lines:
        out += str + '\n'
    out = out[:len(out)-1]

    return out
