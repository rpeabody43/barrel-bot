from pybaseball import statcast
from stats import get_pitch

def __fmt (name: str, velo: int) -> str:
    return f'The fastest pitch was {velo} mph by {name}'

def fastest_pitch (day: str) -> str:
    data = statcast(start_dt=day, verbose=False)
    idx = data['release_speed'].idxmax()
    velo = data.at[idx, 'release_speed']
    pitch_data = get_pitch.data_from_idx(data, idx, day)

    print(__fmt(pitch_data['pitcher_name'], velo))
    return pitch_data