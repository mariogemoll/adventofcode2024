from math import floor
from enum import Enum
from time import sleep

Direction = Enum('Direction', [
    ("UP", 1), ("RIGHT", 2), ("DOWN", 3), ("LEFT", 4)
])

def load_input(filename):
    lines = open(filename).read().split('\n')
    if lines[-1] == '':
        lines.pop()
    grid = []
    width = len(lines[0])
    for line in lines:
        vals = list(line)
        assert len(vals) == width
        grid.append(vals)
    row, col, direction = find_guard(grid)
    grid[row][col] = '.'
    return grid, row, col, direction

def find_guard(grid):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '^':
                return row, col, Direction.UP
            elif grid[row][col] == '>':
                return row, col, Direction.RIGHT
            elif grid[row][col] == 'v':
                return row, col, Direction.DOWN
            elif grid[row][col] == '<':
                return row, col, Direction.LEFT

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
            if (row_num, col_num) in visited:
                print('X', end='')
            else:
                print(row[col_num], end='')
        print()

def run(grid, start_row, start_col, start_direction):
    row = start_row
    col = start_col
    direction = start_direction
    visited = set()
    visited_in_direction = set()
    i = 0
    while True:
        i += 1
        if (row, col, direction) in visited_in_direction:
            return True, visited
        visited.add((row, col))
        visited_in_direction.add((row, col, direction))
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
    return False, visited
