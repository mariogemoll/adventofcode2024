import sys
from tqdm import tqdm

from fifteen import load_input, locate_robot, move_train, gps


def stretch(grid):
    stretched_grid = []
    for row in grid:
        stretched_row = []
        for cell in row:
            if cell == '#':
                stretched = '##'
            elif cell == 'O':
                stretched = '[]'
            elif cell == '.':
                stretched = '..'
            elif cell == '@':
                stretched = '@.'
            else:
                raise Exception('Invalid cell')
            stretched_row += list(stretched)
        stretched_grid.append(stretched_row)
    return stretched_grid


def move_vertically(grid, movement):
    robot_pos = locate_robot(grid)
    frontier = set([robot_pos])
    train = [(robot_pos, '@')]
    while len(frontier) > 0:
        new_frontier = set()
        for (row, col) in frontier:
            next_row = row - 1 if movement == '^' else row + 1
            next = grid[next_row][col]
            if next == '#':
                return
            if next == '[':
                train.insert(0, ((next_row, col), '['))
                train.insert(0, ((next_row, col+1), ']'))
                new_frontier.update([(next_row, col), (next_row, col+1)])
            elif next == ']':
                train.insert(0, ((next_row, col-1), '['))
                train.insert(0, ((next_row, col), ']'))
                new_frontier.update([(next_row, col-1), (next_row, col)])
            else:
                assert next == '.'
        frontier = new_frontier
    move_train(grid, movement, train)


def move_horizontally(grid, movement):
    robot_pos = locate_robot(grid)
    train = [(robot_pos, '@')]
    while True:
        head_row, head_col = train[0][0]
        next_col = head_col + 1 if movement == '>' else head_col - 1
        next = grid[head_row][next_col]
        if next == '#':
            return
        if next == '.':
            move_train(grid, movement, train)
            return
        # If we're here then we're next to a box
        # then_row, then_col = get_next(, next_col, movement)
        then_col = next_col + 1 if movement == '>' else next_col - 1
        then = grid[head_row][then_col]
        assert next == '[' and then == ']' or next == ']' and then == '['
        train.insert(0, ((head_row, next_col), next))
        train.insert(0, ((head_row, then_col), then))


def move(grid, movement):
    if movement == '^' or movement == 'v':
        move_vertically(grid, movement)
    else:
        move_horizontally(grid, movement)


def main():
    if len(sys.argv) != 2:
        print(f'Usage: python {sys.argv[0]} <input_file>')
        sys.exit(1)
    grid, movements = load_input(sys.argv[1])
    grid = stretch(grid)
    for movement in tqdm(movements):
        move(grid, movement)
    print(gps('[', grid))


if __name__ == '__main__':
    main()
