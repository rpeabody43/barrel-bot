from pybaseball import statcast
import video

def to_normal_name (name: str) -> str:
    first_name = name[name.index(',')+2:]
    last_name = name[:name.index(',')]
    return f'{first_name} {last_name}'

def fmt_string (name: str, velo: int, link: str) -> str:
    return f'The fastest pitch was {velo} mph by {name}\n{link}'


def fastest_pitch (day: str) -> str:
    data = statcast(start_dt=day, verbose=False)
    pitch_data = {
        'velo' : -1,
        'game_pk': -1,
        'at_bat_number': -1
    }
    idx = data['release_speed'].idxmax()
    pitch_data['velo'] = data.at[idx, 'release_speed']
    pitch_data['game_pk'] = data.at[idx, 'game_pk']
    pitch_data['at_bat'] = data.at[idx, 'at_bat_number']
    
    link = video.get_link(pitch_data['game_pk'], pitch_data['at_bat'])
    pitcher = to_normal_name(data.at[idx, 'player_name'])
    return fmt_string(pitcher, pitch_data['velo'], link)