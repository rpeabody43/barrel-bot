from video.link import get_link
import requests
from urllib import request as urlreq
from bs4 import BeautifulSoup

def get_video (game_pk: int, at_bat: int, pitch_num: int = -1, date: str = ''):
    url = get_link(game_pk, at_bat, pitch_num)
    raw = __scrape_video(url) if date == '' else __scrape_video(url, date)
    print(f'Baseball Savant: {url}')
    print(f'Raw Video: {raw}')

def __scrape_video (url: str, f_name: str = 'temp') -> str:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    vid_url = soup.find('video', id='sporty').find('source')['src']
    # TODO change file name
    urlreq.urlretrieve(vid_url, f'temp\\{f_name}.mp4')
    return vid_url




