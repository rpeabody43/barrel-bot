from datetime import date, timedelta

from twitter.tweet import tweet_with_video
from stats.max_of.barrel import get_max_barrel as barrel
from video import video_file


def lambda_handler(event, context):
    yesterday = date.today() - timedelta(days=1)
    yesterday_str = yesterday.strftime('%Y-%m-%d')

    try:
        pitch = barrel(yesterday_str)
    except Exception as e:
        print(e)

    path = video_file.get_video(pitch)
    tweet_id = tweet_with_video(pitch, path)

    if not pitch['is_hr']:
        hr_makeup = barrel(yesterday_str, require_hr=True)
        path = video_file.get_video(hr_makeup, True)
        tweet_with_video(hr_makeup, path, tweet_id)

if __name__  == '__main__':
    lambda_handler('event', 'ctx')
