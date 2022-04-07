import requests as r
import json

def find_pitch (team_data: list[str], at_bat: int) -> str:
    ab_pitches = []
    for pitch in team_data:
        if pitch['ab_number'] == at_bat:
            ab_pitches.append(pitch)
    if ab_pitches == []: return ''
    pitch = ab_pitches[len(ab_pitches)-1]
    return pitch['play_id']

def get_play_id (game_pk: int, at_bat: int) -> str:
    endpoint = f'https://baseballsavant.mlb.com/gf?game_pk={game_pk}'
    data = json.loads(r.get(endpoint).text)
    home_team = data['team_home']
    home_test = find_pitch(home_team, at_bat)
    if home_test != '':
        return home_test
    away_team = data['team_away']
    return find_pitch(away_team, at_bat)

def get_link (game_pk: int, at_bat: int) -> str:
    play_id = get_play_id(game_pk, at_bat)
    return f'https://baseballsavant.mlb.com/sporty-videos?playId={play_id}'