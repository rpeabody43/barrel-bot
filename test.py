# Strictly for testing the pybaseball / baseballsavant video aspect of the program
from datetime import date, timedelta
from lambda_deploy.stats import get_max_barrel as barrel
from lambda_deploy.video import get_video

def main():
    auto_open = True
    date = input('YYYY-MM-DD: ')
    pitch = barrel(date) # Automatically prints link to Baseball Savant page
    # filepath = get_video(pitch)
    yesterday = date.today() - timedelta(days=1)
    yesterday_str = yesterday.strftime('%Y-%m-%d')


if __name__  == '__main__':
    main()
