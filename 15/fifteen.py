def locate_robot(grid):
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == '@':
                return (i, j)


def load_input(filename):
    with open(filename, 'r') as file:
        lines = file.read().split('\n')
        if lines[-1] == '':
            lines = lines[:-1]
    in_grid = True
    grid = []
    movements = []
    for i, line in enumerate(lines):
        if in_grid:
            if line == '':
                in_grid = False
            else:
                grid.append(list(line))
        else:
            movements += list(line)
    return grid, movements


def print_grid(grid):
    height = len(grid)
    width = len(grid[0])
    for row in range(height):
        for col in range(width):
            print(grid[row][col], end='')
        print()


def get_next(row, col, movement):
    next_row, next_col = row, col
    if movement == '^':
        next_row -= 1
    elif movement == '>':
        next_col += 1
    elif movement == 'v':
        next_row += 1
    elif movement == '<':
        next_col -= 1
    else:
        raise Exception('Invalid movement')
    return next_row, next_col


def move_train(grid, movement, train):
    vacant = set()
    for (row, col), symbol in train:
        vacant.add((row, col))
        next_row, next_col = get_next(row, col, movement)
        grid[next_row][next_col] = symbol
        if (next_row, next_col) in vacant:
            vacant.remove((next_row, next_col))
    for row, col in vacant:
        grid[row][col] = '.'


def gps(symbol, grid):
    height = len(grid)
    width = len(grid[0])
    val = 0
    for row in range(height):
        for col in range(width):
            if grid[row][col] == symbol:
                val += row * 100 + col
    return val
