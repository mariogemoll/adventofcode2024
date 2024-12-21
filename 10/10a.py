import sys

from common import load_input


def hike(grid, start):
    height = len(grid)
    width = len(grid[0])
    row, col = start
    level = grid[row][col]
    positions = set([start])
    while level < 9:
        next_positions = set()
        for row, col in positions:
            candidates = [
                (row - 1, col),  # N
                (row, col + 1),  # E
                (row + 1, col),  # S
                (row, col - 1)   # W
            ]
            for next_row, next_col in candidates:
                if not (0 <= next_row < height and 0 <= next_col < width):
                    continue
                if grid[next_row][next_col] != level + 1:
                    continue
                next_positions.add((next_row, next_col))
        positions = next_positions
        level += 1
    return len(positions)


def main():
    grid, trailheads = load_input(sys.argv[1])
    total = 0
    for trailhead in trailheads:
        score = hike(grid, trailhead)
        total += score
    print(total)


if __name__ == '__main__':
    main()
