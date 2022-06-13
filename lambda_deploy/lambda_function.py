from datetime import date, timedelta

from twitter import tweet_with_video
from stats import get_max_barrel as barrel
from video import get_video


def lambda_handler(event, context):
    yesterday = date.today() - timedelta(days=1)
    yesterday_str = yesterday.strftime('%Y-%m-%d')
    print(yesterday_str + ':')

    # TODO: handle days with no mlb games
    pitch = barrel(yesterday_str)

    path = get_video(pitch)
    tweet_id = tweet_with_video(pitch, path)

    if not pitch['is_hr']:
        hr_makeup = barrel(yesterday_str, require_hr=True)
        path = get_video(hr_makeup)
        tweet_with_video(hr_makeup, path, tweet_id)

if __name__  == '__main__':
    import time
    start_time = time.time()
    lambda_handler('', '')
    print("--- %s seconds ---" % (time.time() - start_time))
    
