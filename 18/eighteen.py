grid_height = 71
grid_width = 71


def load_input(filename):
    with open(filename, 'r') as file:
        lines = file.read().split('\n')
        if lines[-1] == '':
            lines = lines[:-1]
    # Use (row, col) coordinates for consistency with other days
    return [(int(y), int(x)) for x, y in [line.split(',') for line in lines]]


def get_neighbors(cell):
    row, col = cell
    candidates = set()
    if row - 1 >= 0:
        candidates.add((row - 1, col))
    if col + 1 < grid_width:
        candidates.add((row, col + 1))
    if row + 1 < grid_height:
        candidates.add((row + 1, col))
    if col - 1 >= 0:
        candidates.add((row, col - 1))
    return candidates


def find_shortest_path_length(corrupted):
    start = (0, 0)
    end = (grid_width - 1, grid_height - 1)
    visited = set()
    to_visit = set([start])
    num_steps = 0
    while len(to_visit) > 0:
        neighbors = set()
        for node in to_visit:
            visited.add(node)
            if node == end:
                return num_steps
            node_neighbors = get_neighbors(node)
            neighbors.update(node_neighbors)
        to_visit = neighbors - corrupted - visited
        num_steps += 1
