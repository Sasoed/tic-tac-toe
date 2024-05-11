from ..engine import create_new_game

def test_create_new_game():
    state = create_new_game()
    assert state is not None
