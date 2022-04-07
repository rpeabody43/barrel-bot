from pybaseball import statcast
from names import get_player_name
import video

# This isn't exact but it's good enough
def is_barrel (speed: int, ang: int) -> bool:
    if speed < 98: return False
    increase = speed - 98
    lower_bound = 26 - increase
    upper_bound = 30 + (1.2*increase)
    if lower_bound < ang < upper_bound:
        return True
    return False

def fmt_string (id: int, velo: int, ang: int, des: str, link: str) -> str:
    name = get_player_name(id, des)
    return f'{name} hit the hardest barrel of {velo} mph at {ang}°\n{link}'

def get_max_barrel (day: str) -> str:
    data = statcast(start_dt=day, verbose=False)
    hit_data = {
        'velo' : -1,
        'ang' : -1,
        'batter_id' : -1,
        'des': '',
        'game_pk': -1,
        'at_bat_number': -1
    }
    while True:
        if data.size == 0: return 'There were no barrels on this day'
        idx = data['launch_speed'].idxmax()
        velo = data.at[idx, 'launch_speed']
        ang = data.at[idx, 'launch_angle']
        if is_barrel(velo, ang) and data.at[idx, 'type'] == 'X':
            hit_data['ang'], hit_data['velo'] = ang, velo
            hit_data['batter_id'] = data.at[idx, 'batter']
            hit_data['des'] = data.at[idx, 'des']
            hit_data['game_pk'] = data.at[idx, 'game_pk']
            hit_data['at_bat'] = data.at[idx, 'at_bat_number']
            break
        else:
            data.drop([idx], axis=0, inplace=True)
    
    link = video.get_link(hit_data['game_pk'], hit_data['at_bat'])
    return fmt_string(hit_data['batter_id'], hit_data['velo'], hit_data['ang'], hit_data['des'], link)