import sys
from enum import Enum
from tqdm import tqdm


def load_input(filename):
    with open(filename) as file:
        lines = file.read().split('\n')
        if lines[-1] == '':
            lines = lines[:-1]
        return [list(line) for line in lines]


Direction = Enum('Direction', [
    ("UP", 1), ("RIGHT", 2), ("DOWN", 3), ("LEFT", 4)
])


# Returns direction (looking outward), row position, col position
def border(pos, neighbor):
    row_p, col_p = pos
    row_n, col_n = neighbor
    if row_n == row_p - 1 and col_n == col_p:
        # Neighbor is above pos
        return Direction.UP, row_p, col_n
    elif row_n == row_p and col_n == col_p + 1:
        # Neighbor is to the right of pos
        return Direction.RIGHT, row_n, col_n
    elif row_n == row_p + 1 and col_n == col_p:
        # Neighbor is below pos
        return Direction.DOWN, row_n, col_p
    elif row_n == row_p and col_n == col_p - 1:
        # Neighbor is to the left of pos
        return Direction.LEFT, row_n, col_p
    else:
        raise Exception('Not neighbors')


def flood_fill(grid, area_cells, visited, to_visit, pos):
    area_cells.add(pos)
    visited.add(pos)
    height = len(grid)
    width = len(grid[0])
    row, col = pos
    neighbors = [
        (row - 1, col),  # N,
        (row, col + 1),  # E,
        (row + 1, col),  # S,
        (row, col - 1)   # W
    ]
    fence_pieces = set()
    for neighbor in neighbors:
        n_row, n_col = neighbor
        if neighbor in area_cells:
            # Neighbor already in region cells
            continue
        elif n_row < 0 or n_row >= height or n_col < 0 or n_col >= width:
            # Neighbor outside the grid
            fence_pieces.add(border(pos, neighbor))
            # perimeter += 1
        elif grid[n_row][n_col] != grid[row][col]:
            # Neighbor has a different color
            fence_pieces.add(border(pos, neighbor))
            # perimeter += 1
        elif neighbor not in visited:
            # Visit the neighbor
            fence_pieces.update(flood_fill(grid, area_cells, visited, to_visit, neighbor))
    return fence_pieces


def find_sides(height, width, fence_pieces):
    horizontal_sides = []
    for row in range(height + 1):
        for dir in [Direction.UP, Direction.DOWN]:
            current_side = None
            for col in range(width):
                pos = (dir, row, col)
                if pos in fence_pieces:
                    if current_side is None:
                        current_side = []
                        horizontal_sides.append(current_side)
                    current_side.append((row, col))
                else:
                    if current_side is not None:
                        current_side = None

    vertical_sides = []
    for col in range(width + 1):
        for dir in [Direction.LEFT, Direction.RIGHT]:
            current_side = None
            for row in range(height):
                pos = (dir, row, col)
                if pos in fence_pieces:
                    if current_side is None:
                        current_side = []
                        vertical_sides.append(current_side)
                    current_side.append((row, col))
                else:
                    if current_side is not None:
                        current_side = None
    return horizontal_sides, vertical_sides


def main():
    grid = load_input(sys.argv[1])
    height = len(grid)
    width = len(grid[0])
    visited = set()
    regions = []
    for row in range(0, height):
        for col in range(0, width):
            if (row, col) in visited:
                continue
            color = grid[row][col]
            area = set()
            fence_pieces = flood_fill(grid, area, visited, set(), (row, col))
            regions.append((color, len(area), fence_pieces))
    total_a = 0
    total_b = 0
    for color, area, fence_pieces in tqdm(regions):
        h_sides, v_sides = find_sides(height, width, fence_pieces)
        num_sides = len(h_sides) + len(v_sides)
        perimeter = len(fence_pieces)
        price_a = area * perimeter
        total_a += price_a
        price_b = area * num_sides
        total_b += price_b
    print(f'Total price: {total_a} / {total_b}')


if __name__ == '__main__':
    main()
