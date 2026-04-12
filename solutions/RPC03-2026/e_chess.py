import sys
from functools import lru_cache


sys.setrecursionlimit(10000)


def parse_loc(text):
    return ord(text[0]) - 65, int(text[1]) - 1


def sign(value):
    return (value > 0) - (value < 0)
 

n, m = map(int, sys.stdin.readline().split())
pieces = []
start_state = []

for _ in range(m):
    piece_type, location = sys.stdin.readline().split()
    row, col = parse_loc(location)
    pieces.append(piece_type)
    start_state.append(row * n + col)


def decode(position):
    return divmod(position, n)


def occupied_set(state):
    return {position for position in state if position != -1}


def is_legal_move(piece_type, state, source_index, target_index):
    source_row, source_col = decode(state[source_index])
    target_row, target_col = decode(state[target_index])
    delta_row = target_row - source_row
    delta_col = target_col - source_col
    occupied = occupied_set(state)
    occupied.discard(state[source_index])

    if piece_type == 'N':
        return (abs(delta_row), abs(delta_col)) in {(1, 2), (2, 1)}

    if piece_type == 'K':
        return max(abs(delta_row), abs(delta_col)) == 1

    if piece_type in {'R', 'Q'} and (delta_row == 0 or delta_col == 0):
        step_row = sign(delta_row)
        step_col = sign(delta_col)
    elif piece_type in {'B', 'Q'} and abs(delta_row) == abs(delta_col):
        step_row = sign(delta_row)
        step_col = sign(delta_col)
    else:
        return False

    current_row = source_row + step_row
    current_col = source_col + step_col
    while (current_row, current_col) != (target_row, target_col):
        if current_row < 0 or current_row >= n or current_col < 0 or current_col >= n:
            return False
        if current_row * n + current_col in occupied:
            return False
        current_row += step_row
        current_col += step_col

    return True


def generate_moves(state):
    moves = []
    alive = [index for index, position in enumerate(state) if position != -1]
    alive.sort(key=lambda index: decode(state[index]))

    for source_index in alive:
        source_row, source_col = decode(state[source_index])
        piece_type = pieces[source_index]
        for target_index in alive:
            if source_index == target_index:
                continue
            if not is_legal_move(piece_type, state, source_index, target_index):
                continue
            target_row, target_col = decode(state[target_index])
            moves.append((source_row, source_col, target_row, target_col, source_index, target_index))

    moves.sort()
    return moves


@lru_cache(maxsize=None)
def solve(state):
    alive_count = sum(position != -1 for position in state)
    if alive_count == 1:
        return ()

    for source_row, source_col, target_row, target_col, source_index, target_index in generate_moves(state):
        next_state = list(state)
        next_state[source_index] = target_row * n + target_col
        next_state[target_index] = -1
        solution = solve(tuple(next_state))
        if solution is not None:
            move = (pieces[source_index], source_row, source_col, target_row, target_col)
            return (move,) + solution

    return None


answer = solve(tuple(start_state))

if answer is None:
    print('No solution')
else:
    for piece_type, source_row, source_col, target_row, target_col in answer:
        print(f"{piece_type}: {chr(65 + source_row)}{source_col + 1} -> {chr(65 + target_row)}{target_col + 1}")