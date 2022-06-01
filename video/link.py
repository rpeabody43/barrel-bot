import requests as r
import json

def __find_pitch (team_data: 'list[str]', at_bat: int, pitch_num: int) -> str:
    ab_pitches = []
    for pitch in team_data:
        if pitch['ab_number'] == at_bat:
            ab_pitches.append(pitch)
    if ab_pitches == []: return ''
    if pitch_num == -1:
        pitch = ab_pitches[len(ab_pitches)-1]
    else: 
        pitch = ab_pitches[pitch_num-1]
    return pitch['play_id']

def __play_id (game_pk: int, at_bat: int, pitch_num: int) -> str:
    endpoint = f'https://baseballsavant.mlb.com/gf?game_pk={game_pk}'
    data = json.loads(r.get(endpoint).text)
    home_team = data['team_home']
    home_test = __find_pitch(home_team, at_bat, pitch_num)
    if home_test != '':
        return home_test
    away_team = data['team_away']
    return __find_pitch(away_team, at_bat, pitch_num)

def get_link (game_pk: int, at_bat: int, pitch_num = -1) -> str:
    play_id = __play_id(game_pk, at_bat, pitch_num)
    return f'https://baseballsavant.mlb.com/sporty-videos?playId={play_id}'