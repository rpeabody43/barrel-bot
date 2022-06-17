from pandas import DataFrame
import stats.names as names


def data_from_idx(df: DataFrame, idx: int, date: str) -> dict:
    batter_id = df.at[idx, 'batter']
    description = df.at[idx, 'des']
    data = {
        'date': date,
        'game_pk': df.at[idx, 'game_pk'],
        'at_bat': df.at[idx, 'at_bat_number'],
        'pitch_num': df.at[idx, 'pitch_number'],
        # For some reason only the pitcher gets their formatted name listed
        'pitcher_name': names.to_normal_name(df.at[idx, 'player_name']),
        'batter_name': names.get_player_name(batter_id, description),
        'batting_team': df.at[idx, 'home_team'] if df.at[idx, 'inning_topbot'] == 'Bot' else df.at[idx, 'away_team'],
        'type': df.at[idx, 'type'],
        'outcome': df.at[idx, 'events'],
        'xba' : df.at[idx, 'estimated_ba_using_speedangle']
    }
    return data
