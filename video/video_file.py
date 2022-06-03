from video.link import get_link
import requests
from urllib import request as urlreq
from bs4 import BeautifulSoup

def get_video (data: dict) -> str:
    url = get_link(data['game_pk'], data['at_bat'], data['pitch_num'])
    filepath = __scrape_video(url) if data['date'] == '' else __scrape_video(url, data['date'])
    print(f'Baseball Savant: {url}')
    # print(f'Raw Video: {raw}')
    return filepath

def __scrape_video (url: str, f_name: str = 'temp') -> str:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    vid_url = soup.find('video', id='sporty').find('source')['src']
    # TODO change file name
    path = f'temp\\{f_name}.mp4'
    urlreq.urlretrieve(vid_url, path)
    return path



