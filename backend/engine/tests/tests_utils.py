import re

from ..engine import create_new_game

def parse_state(src, active_group=None):
    state = create_new_game()
    state['active_group'] = active_group
    src = re.sub('[^_xo]', '', src)
    for i, symbol in enumerate(src):
        if symbol == '_':
            symbol = None

        row = i // 9
        col = i % 9

        macro_row = row // 3
        macro_col = col // 3

        group = macro_row * 3 + macro_col

        micro_row = row % 3
        micro_col = col % 3

        cell = micro_row * 3 + micro_col

        state['groups'][group][cell] = symbol
    return state


def test_parse_state():
    state = parse_state('''
        0 1 2  _ _ _  _ _ _
        3 4 5  _ _ _  _ _ _
        6 7 8  _ _ _  _ _ _

        _ _ _  _ _ _  _ _ _
        _ _ _  _ _ _  _ _ _
        _ _ _  _ _ _  _ _ _

        _ _ _  _ _ _  0 1 2
        _ _ _  _ _ _  3 4 5
        _ _ _  _ _ _  6 7 8
    ''', active_group=0)
    print(state)