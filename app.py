from flask import Flask
import twitter.tweet
from stats.max_of.barrel import get_max_barrel as barrel
from video import video_file

application = Flask(__name__)

@application.route('/')
def index():
    return 'follow @mlb_barrels!'

if __name__  == '__main__':
    date = input('YYYY-MM-DD: ')
    pitch = barrel(date)
    path = video_file.get_video(pitch)
    twitter.tweet.tweet_with_video(pitch, path)
    # application.run(port=5000, debug=True)

