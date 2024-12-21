from common import load_input, Direction


def print_grid(grid, visited, guard_row, guard_col, guard_direction):
    for row_num, row in enumerate(grid):
        for col_num in range(len(row)):
            if row_num == guard_row and col_num == guard_col:
                if guard_direction == Direction.UP:
                    print('^', end='')
                elif guard_direction == Direction.RIGHT:
                    print('>', end='')
                elif guard_direction == Direction.DOWN:
                    print('v', end='')
                elif guard_direction == Direction.LEFT:
                    print('<', end='')
            else:
                print(row[col_num], end='')
        print()


def run(grid, start_row, start_col, start_direction):
    row = start_row
    col = start_col
    direction = start_direction
    visited = set()
    while True:
        visited.add((row, col))
        next_position = None
        if direction == Direction.UP:
            next_position = (row - 1, col)
        elif direction == Direction.RIGHT:
            next_position = (row, col + 1)
        elif direction == Direction.DOWN:
            next_position = (row + 1, col)
        elif direction == Direction.LEFT:
            next_position = (row, col - 1)
        next_row, next_col = next_position
        if next_row < 0 or next_row >= len(grid) or next_col < 0 or next_col >= len(grid[0]):
            break
        if grid[next_row][next_col] == '#':
            if direction == Direction.UP:
                direction = Direction.RIGHT
            elif direction == Direction.RIGHT:
                direction = Direction.DOWN
            elif direction == Direction.DOWN:
                direction = Direction.LEFT
            elif direction == Direction.LEFT:
                direction = Direction.UP
        else:
            row = next_row
            col = next_col

    print_grid(grid, visited, row, col, direction)
    return visited


def main():
    grid, row, col, direction = load_input('input')
    visited = run(grid, row, col, direction)
    print(f"Visited {len(visited)} positions")


if __name__ == '__main__':
    main()
