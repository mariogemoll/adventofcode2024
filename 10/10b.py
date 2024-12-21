import sys


from common import load_input


class Trail:
    def __init__(self, steps):
        self.steps = steps

    def __hash__(self):
        return hash(str(self.steps))

    def __str__(self):
        return str(self.steps)


def hike(grid, start):
    height = len(grid)
    width = len(grid[0])
    row, col = start
    level = grid[row][col]
    trails = set([Trail([start])])
    while level < 9:
        next_trails = set()
        for trail in trails:
            row, col = trail.steps[-1]
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
                new_trail = Trail(trail.steps.copy())
                new_trail.steps.append((next_row, next_col))
                next_trails.add(new_trail)
        trails = next_trails
        level += 1
    return len(trails)


def main():
    grid, trailheads = load_input(sys.argv[1])
    total = 0
    for trailhead in trailheads:
        score = hike(grid, trailhead)
        total += score
    print(total)


if __name__ == '__main__':
    main()
