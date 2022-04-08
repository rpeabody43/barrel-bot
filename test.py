from stats.barrel import get_max_barrel as barrel
from stats.pitch_velo import fastest_pitch as pitch

def main():
    date = '2018-10-26'
    print(pitch(date))

if __name__  == '__main__':
    main()
