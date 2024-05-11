from ..engine import get_count

from .tests_utils import parse_state


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
