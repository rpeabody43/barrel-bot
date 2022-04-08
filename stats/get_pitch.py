from pandas import DataFrame
from video import video_file
import names

def data_from_idx (df: DataFrame, idx: int, date: str, video: bool = False) -> dict:
    batter_id = df.at[idx, 'batter']
    description = df.at[idx, 'des']
    data = {
        'date' : date,
        'game_pk' : df.at[idx, 'game_pk'],
        'at_bat' : df.at[idx, 'at_bat_number'],
        'pitch_num' : df.at[idx, 'pitch_number'],
        # For some reason only the pitcher gets their formatted name listed
        'pitcher_name' : names.to_normal_name(df.at[idx, 'player_name']),
        'batter_name' : names.get_player_name(batter_id, description)
    }

    if video:
        __vid_from_data(data)
    return data

def __vid_from_data (data: dict) -> None:
    video_file.get_video(data['game_pk'], data['at_bat'], data['pitch_num'], data['date'])
