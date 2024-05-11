from ..engine import create_new_game, get_current_player

from .tests_utils import parse_state

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