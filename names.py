import re
from pybaseball import playerid_reverse_lookup as prl
from pandas import DataFrame

def fmt_name (name: str) -> str:
    name = name.title()
    new_str = name[0]
    for i in range(1, len(name)):
        if name[i-1] == '.':
            new_str += name[i].upper()
        else:
            new_str += name[i]
    return new_str

def get_player_name (id: int, des=''):
    player = prl([id])
    first_name = player.at[0, 'name_first']
    re.sub(r'\W+', '', first_name)
    last_name = player.at[0, 'name_last']
    re.sub(r'\W+', '', last_name)
    name = fmt_name(f'{first_name} {last_name}')
    if des == '':
        return name
    else:
        name = des[:len(name)]
    return name
