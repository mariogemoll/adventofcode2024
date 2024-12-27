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

    start_row, start_col = find_cell(grid, 'S')
    end_row, end_col = find_cell(grid, 'E')

    graph = get_matrix(grid)
    return graph, start_row, start_col, end_row, end_col


def find_cell(grid, symbol):
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == symbol:
                return (i, j)
    raise Exception('Start not found')


def next_node(row, col, direction):
    if direction == Direction.N:
        row -= 1
    elif direction == Direction.E:
        col += 1
    elif direction == Direction.S:
        row += 1
    elif direction == Direction.W:
        col -= 1
    return row, col, direction


def get_options(grid, node):
    row, col, dir = node
    options = []
    # Option 1: Go one step in the current direction
    next_row, next_col, _ = next_node(row, col, dir)
    next = grid[next_row][next_col]
    if next != '#':
        options.append(((next_row, next_col, dir), 1))

    # Options 2 and 3: Turn 90 degrees left or right (no use turning around 180 degrees and go back)
    for dir_change in [+1, -1]:
        new_direction = Direction((dir + dir_change) % 4)
        # It only makes sense to turn if we can go in the new direction in the next step
        next_row, next_col, _ = next_node(row, col, new_direction)
        next = grid[next_row][next_col]
        if next != '#':
            options.append(((row, col, new_direction), 1000))
    return options


def get_matrix(grid):
    start_row, start_col = find_cell(grid, 'S')
    start_dir = Direction.E
    start_node = start_row, start_col, start_dir
    matrix = {}
    next = set([start_node])
    visited = set()
    while len(next) > 0:
        new_next = set()
        for node in next:
            visited.add(node)
            if node not in matrix:
                matrix[node] = {}
            options = get_options(grid, node)
            for neighbor, cost in options:
                matrix[node][neighbor] = cost
                if neighbor not in visited:
                    new_next.add(neighbor)
        next = new_next
    return matrix
