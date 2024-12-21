def load_input(filename):
    grid = []
    trailheads = []
    for line in open(filename):
        grid.append([int(x) if x != '.' else None for x in line[:-1]])
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 0:
                trailheads.append((row, col))
    return grid, trailheads
