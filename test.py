# Move into ./lambda_deploy before running first for relative paths to work
# Strictly for testing the pybaseball / baseballsavant video aspect of the program
from datetime import date, timedelta
from stats import get_max_barrel as barrel
from video import get_video

def main():
    auto_open = True
    date = input('YYYY-MM-DD: ')
    try:    
        pitch = barrel(date) # Automatically prints link to Baseball Savant page
    except Exception as e:
        if str(e) == 'Empty DataFrame':
            print('no games on this day')
        return
    # filepath = get_video(pitch)
    # yesterday = date.today() - timedelta(days=1)
    # yesterday_str = yesterday.strftime('%Y-%m-%d')


if __name__  == '__main__':
    main()
