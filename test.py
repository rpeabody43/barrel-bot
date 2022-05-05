import webbrowser
from video import video_file
from stats.max_of.barrel import get_max_barrel as barrel
from stats.max_of.pitch_velo import fastest_pitch as pitch


def main():
    auto_open = True
    date = input('YYYY-MM-DD: ')
    pitch = barrel(date, True)
    url = video_file.get_video(pitch)
    if auto_open:
        webbrowser.open(url, new=2)

if __name__  == '__main__':
    main()
