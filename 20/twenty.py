from collections import Counter

from tqdm import tqdm


class Direction(int):
    N = 0
    E = 1
    S = 2
    W = 3


def load_input(filename):
    with open(filename, 'r') as file:
        lines = file.read().split('\n')
        if lines[-1] == '':
            lines = lines[:-1]
    grid = []
    for line in lines:
        grid.append(list(line))
    return grid


def find_symbol(symbol, grid):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == symbol:
                return row, col


def get_next_pos(dir, pos):
    row, col = pos
    if dir == Direction.N:
        row -= 1
    elif dir == Direction.E:
        col += 1
    elif dir == Direction.S:
        row += 1
    elif dir == Direction.W:
        col -= 1
    else:
        raise RuntimeError('Invalid direction', dir)
    return row, col


def find_next(grid, prev, pos):
    for dir in range(4):
        next_pos = get_next_pos(dir, pos)
        next_row, next_col = next_pos
        if next_pos != prev and on_grid(grid, next_pos):
            next = grid[next_row][next_col]
            if next == '.' or next == 'E':
                return (next_row, next_col), next == 'E'


def on_grid(grid, pos):
    row, col = pos
    return 0 <= row < len(grid) and 0 <= col < len(grid[0])


def val(grid, pos):
    row, col = pos
    return grid[row][col]


def get_racetrack(grid):
    pos = find_symbol('S', grid)
    racetrack = [pos]
    pos, done = find_next(grid, None, pos)
    racetrack.append(pos)
    while not done:
        pos, done = find_next(grid, racetrack[-2], racetrack[-1])
        racetrack.append(pos)
    return racetrack


def get_reachable(grid, pos, max_num_steps):
    all_reachable = set()
    reachable = set([pos])
    for n in range(max_num_steps):
        new_reachable = set()
        for pos in reachable:
            for dir in range(4):
                next_pos = get_next_pos(dir, pos)
                if on_grid(grid, next_pos) and next_pos not in all_reachable:
                    new_reachable.add(next_pos)
        all_reachable.update(new_reachable)
        reachable = new_reachable
    return all_reachable


def get_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def solution(filename, max_steps):

    grid = load_input(filename)
    racetrack = get_racetrack(grid)

    # Write the number of each step in the racetrack to the corresponding position on the grid
    for i, (row, col) in enumerate(racetrack):
        grid[row][col] = i

    counter = Counter()
    for i, pos in enumerate(tqdm(racetrack)):
        orig_val = val(grid, pos)
        reachable = get_reachable(grid, pos, max_steps)
        for dst in reachable:
            new_val = val(grid, dst)
            if new_val == '#':
                continue
            if new_val > orig_val:
                distance = get_distance(pos, dst)
                saving = new_val - orig_val - distance
                counter[saving] += 1

    return sum([val for saving, val in counter.items() if saving >= 100])
