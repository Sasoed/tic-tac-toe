from ..engine import create_new_game, get_valid_moves

from .tests_utils import parse_state

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

