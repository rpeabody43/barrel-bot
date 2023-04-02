# Move into ./lambda_deploy before running first for relative paths to work
# Strictly for testing the pybaseball / baseballsavant video aspect of the program
from datetime import date, timedelta
from stats import get_max_barrel as barrel
from video import get_video
from twitter.tweet import _fmt_tweet

def main():
    auto_open = True
    date = input('YYYY-MM-DD: ')
    # try:    
    pitch = barrel(date) # Automatically prints link to Baseball Savant page
    # except Exception as e:
    #     print(e)
    #     if str(e) == 'Empty DataFrame':
    #         print('no games on this day')
    #     return
    print(_fmt_tweet(pitch))


if __name__  == '__main__':
    main()
