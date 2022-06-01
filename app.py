from flask import Flask
import twitter.tweet

application = Flask(__name__)

@application.route('/')
def index():
    return 'follow @mlb_barrels!'

if __name__  == '__main__':
    twitter.tweet.test_tweet()
    # application.run(port=5000, debug=True)

