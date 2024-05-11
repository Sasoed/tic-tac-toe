from .engine import create_new_game, get_valid_moves, get_count, get_current_player


def test_create_new_game():
    state = create_new_game()
    assert state is not None


def test_valid_moves_for_new_game():
    state = create_new_game()
    moves = get_valid_moves(state)
    assert moves == [
        ('x', (group, cell))
        for group in range(9)
        for cell in range(9)
    ]


def test_valid_moves_checks_active_group():
    state = create_new_game()
    state['active_group'] = 0
    moves = get_valid_moves(state)
    assert moves == [
        ('x', (group, cell))
        for group in [0]
        for cell in range(9)
    ]


def test_valid_moves_checks_active_player():
    state = parse_state('''
        _ x _  _ _ _  _ _ _
        _ _ _  _ _ _  _ _ _
        _ _ _  _ _ _  _ _ _

        _ _ _  _ _ _  _ _ _
        _ _ _  _ _ _  _ _ _
        _ _ _  _ _ _  _ _ _

        _ _ _  _ _ _  _ _ _
        _ _ _  _ _ _  _ _ _
        _ _ _  _ _ _  _ _ _
    ''', active_group=None)
    moves = get_valid_moves(state)
    assert moves == [
        ('o', (group, cell))
        for group in range(9)
        for cell in range(9)
        if (group, cell) != (0, 1)
    ]


def test_valid_moves_checks_empty_cells():
    state = parse_state('''
        _ x _  _ _ _  _ _ _
        _ _ _  _ _ _  _ _ _
        _ _ _  _ _ _  _ _ _

        _ _ _  _ _ _  _ _ _
        _ _ _  _ _ _  _ _ _
        _ _ _  _ _ _  _ _ _

        _ _ _  _ _ _  _ _ _
        _ _ _  _ _ _  _ _ _
        _ _ _  _ _ _  _ _ _
    ''', active_group=0)
    moves = get_valid_moves(state)
    assert moves == [
        ('o', (0, cell))
        for cell in range(9)
        if cell != 1
    ]



import re

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


def test_get_count():
    state = parse_state('''
        _ x _  _ _ _  _ _ _
        _ _ _  o _ _  _ _ _
        _ _ _  o _ _  _ _ _

        _ _ _  _ _ _  _ _ _
        _ _ _  _ _ _  _ _ _
        _ _ _  _ _ _  _ _ _

        _ _ _  _ _ _  _ _ _
        _ _ _  _ _ _  _ _ _
        _ _ _  _ _ _  _ _ _
    ''')
    assert get_count(state, 'x') == 1
    assert get_count(state, 'o') == 2


def test_get_current_player_new_game():
    state = create_new_game()
    assert get_current_player(state) == 'x'


def test_get_current_player_next_move():
    state = parse_state('''
        _ x _  _ _ _  _ _ _
        _ _ _  _ _ _  _ _ _
        _ _ _  _ _ _  _ _ _

        _ _ _  _ _ _  _ _ _
        _ _ _  _ _ _  _ _ _
        _ _ _  _ _ _  _ _ _

        _ _ _  _ _ _  _ _ _
        _ _ _  _ _ _  _ _ _
        _ _ _  _ _ _  _ _ _
    ''')
    assert get_current_player(state) == 'o'