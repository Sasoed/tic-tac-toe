GROUPS_COUNT = 9
CELLS_COUNT = 9

CELLS = list(range(CELLS_COUNT))
GROUPS = list(range(GROUPS_COUNT))

GROUPS_CELLS = [
    (group, cell)
    for group in GROUPS
    for cell in CELLS
]



type Player = str

type State = dict

type Cell = tuple[int, int]

type Move = tuple[Player, Cell]


def create_new_game() -> State:
    return {
        'groups': [
            [None for cell_index in range(CELLS_COUNT)]
            for group_index in range(GROUPS_COUNT)
        ],
        'active_group': None,
    }


def get_valid_moves(state: State) -> list[Move]:
    if state['active_group'] is None:
        groups = range(GROUPS_COUNT)
    else:
        groups = [state['active_group']]

    current_player = get_current_player(state)

    return [
        (current_player, (group, cell))
        for group in groups
        for cell in range(CELLS_COUNT)
        if state['groups'][group][cell] is None
    ]


def make_move(state: State, move: Move) -> State:
    pass


def get_winner(state: State) -> Player | None:
    pass


###

def get_current_player(state: State) -> Player:
    if get_count(state, 'x') > get_count(state, 'o'):
        return 'o'
    else:
        return 'x'


def get_count(state, player):
    return sum(
        1
        for group, cell in GROUPS_CELLS
        if state['groups'][group][cell] == player
    )




