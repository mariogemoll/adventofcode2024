from functools import cache
from itertools import chain, product


def load_input(filename):
    with open(filename, 'r') as file:
        lines = file.read().split('\n')
        if lines[-1] == '':
            lines = lines[:-1]
    return lines


num_keypad = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    [None, '0', 'A']
]

dir_keypad = [
    [None, '^', 'A'],
    ['<', 'v', '>']
]


def advance(pos, command):
    row, col = pos
    if command == '^':
        row -= 1
    elif command == '>':
        col += 1
    elif command == 'v':
        row += 1
    elif command == '<':
        col -= 1
    else:
        raise RuntimeError('Invalid move command', command)
    return row, col


def on_grid(grid, pos):
    height = len(grid)
    width = len(grid[0])
    row, col = pos
    if not (0 <= row < height and 0 <= col < width):
        return False
    val = grid[row][col]
    if val is None:
        return False
    return True


def shortest_seqs(grid, start, end):
    if start == end:
        return []
    paths = [(start, [])]
    visited = set([start])
    final_paths = []
    while True:
        new_paths = []
        new_visited = set()
        for last_pos, steps in paths:
            for dir in ['^', '>', 'v', '<']:
                neighbor = advance(last_pos, dir)
                if not on_grid(grid, neighbor):
                    continue
                if neighbor in visited:
                    continue
                new_path = (neighbor, steps + [dir])
                if neighbor == end:
                    final_paths.append(steps + [dir])
                else:
                    new_paths.append(new_path)
                    new_visited.add(neighbor)
        if len(new_paths) == 0:
            min_len = min([len(p) for p in final_paths])
            return [p for p in final_paths if len(p) == min_len]
        paths = new_paths
        visited.update(new_visited)


def coordinate(grid, symbol):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == symbol:
                return row, col
    raise RuntimeError('Not found')


def get_shortest_paths(keypad):
    symbols = [x for x in list(chain.from_iterable(keypad)) if x is not None]
    ways = {}
    for start in symbols:
        for end in symbols:
            if start == end:
                ways_for_symbol = [['A']]
            else:
                start_pos = coordinate(keypad, start)
                end_pos = coordinate(keypad, end)
                ways_for_symbol = [seq + ['A'] for seq in shortest_seqs(keypad, start_pos, end_pos)]
            ways[(start, end)] = ways_for_symbol
    return ways


dir_ways = get_shortest_paths(dir_keypad)
num_ways = get_shortest_paths(num_keypad)


@cache
def dir_expand(pair, level):
    if level == 0:
        return min([len(way) for way in dir_ways[pair]])
    else:
        result = []
        for way in dir_ways[pair]:
            next_level_instructions = ['A'] + way
            next_level_pairs = list(zip(next_level_instructions, next_level_instructions[1:]))
            expanded = []
            for next_level_pair in next_level_pairs:
                expanded.append(dir_expand(next_level_pair, level - 1))
            result.append(sum(expanded))
        return min(result)


def get_shortest_seq_len(num_intermediary_robots, door_seq):
    desired_num_output = list(door_seq)
    num_robot_trajectory = ['A'] + desired_num_output
    num_robot_pairs = list(zip(num_robot_trajectory, num_robot_trajectory[1:]))

    chunks = [num_ways[pair] for pair in num_robot_pairs]
    ways = [list(chain.from_iterable(combination)) for combination in product(*chunks)]

    min_lengths = []
    for way in ways:
        last_robot_trajectory = ['A'] + way
        last_robot_pairs = list(zip(last_robot_trajectory, last_robot_trajectory[1:]))
        way_min_lengths = []
        for pair in last_robot_pairs:
            way_min_lengths.append(dir_expand(pair, num_intermediary_robots - 1))
        min_lengths.append(sum(way_min_lengths))
    return min(min_lengths)
