from math import floor, ceil

width = 101
height = 103


def load_input(filename):
    with open(filename, 'r') as file:
        lines = file.read().split('\n')
        if lines[-1] == '':
            lines = lines[:-1]
        initial_positions = []
        velocities = []
        for line in lines:
            pos, velocity = line.split(' ')
            initial_positions.append([int(val) for val in pos[2:].split(',')])
            velocities.append([int(val) for val in velocity[2:].split(',')])
        return initial_positions, velocities


def generate_grid(robot_positions):
    grid = []
    for _ in range(height):
        grid.append([0] * width)
    for col, row in robot_positions:
        grid[row][col] += 1
    return grid


def draw_grid(grid):
    for row in grid:
        print(''.join([str(val) if val > 0 else '.' for val in row]))


def update_positions(velocities, positions):
    assert len(velocities) == len(positions)
    for i in range(len(positions)):
        positions[i] = ((
            positions[i][0] + velocities[i][0]) % width,
            (positions[i][1] + velocities[i][1]) % height)


def subarea_sum(row_from, row_to, col_from, col_to, grid):
    sum = 0
    for row in range(row_from, row_to):
        for col in range(col_from, col_to):
            sum += grid[row][col]
    return sum


def calculate_safety_factor(grid):
    nw = subarea_sum(0, floor(height/2), 0, floor(width/2), grid)
    ne = subarea_sum(0, floor(height/2), ceil(width/2), width, grid)
    sw = subarea_sum(ceil(height/2), height, 0, floor(width/2), grid)
    se = subarea_sum(ceil(height/2), height, ceil(width/2), width, grid)
    return nw * ne * sw * se
