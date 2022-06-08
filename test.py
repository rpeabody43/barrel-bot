from datetime import date, timedelta

def main():
    # auto_open = True
    # date = input('YYYY-MM-DD: ')
    # pitch = barrel(date)
    # filepath = video_file.get_video(pitch)
    yesterday = date.today() - timedelta(days=1)
    yesterday_str = yesterday.strftime('%Y-%m-%d')
    print(yesterday_str)


if __name__  == '__main__':
    main()
