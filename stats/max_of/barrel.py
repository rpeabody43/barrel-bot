from pybaseball import statcast

from stats import get_pitch

# This isn't exact but it's good enough
def is_barrel (speed: int, ang: int) -> bool:
    if speed < 98: return False
    increase = speed - 98
    lower_bound = 26 - increase
    upper_bound = 30 + (1.2*increase)
    if lower_bound < ang < upper_bound:
        return True
    return False

def __fmt (name: str, velo: int, ang: int) -> str:
    return f'{name} hit the hardest barrel at {velo} mph and {ang}°'

def get_max_barrel (day: str) -> str:
    df = statcast(start_dt=day, verbose=False)
    velo = 0
    ang = 0
    hit_data = {}
    while True:
        if df.size == 0: return 'There were no barrels on this day'
        idx = df['launch_speed'].idxmax()
        velo = df.at[idx, 'launch_speed']
        ang = df.at[idx, 'launch_angle']
        if is_barrel(velo, ang) and df.at[idx, 'type'] == 'X':
            hit_data = get_pitch.data_from_idx(df, idx, day, video=True)
            break
        else:
            df.drop([idx], axis=0, inplace=True)
    return __fmt(hit_data['batter_name'], velo, ang)