def load_input(filename):
    grid = []
    for line in open(filename):
        vals = list(line[:-1])
        grid.append(vals)
    height = len(grid)
    width = len(grid[0])
    antennas = {}
    for row in range(len(grid)):
        assert len(grid[row]) == width
        for col in range(width):
            freq = grid[row][col]
            if freq == '.':
                continue
            if freq not in antennas:
                antennas[freq] = []
            antennas[freq].append((row, col))
    return height, width, antennas


def sub(a, b):
    return (a[0] - b[0], a[1] - b[1])


def print_grid(height, width, antennas, antinodes):
    for row in range(height):
        for col in range(width):
            val = '.'
            if (row, col) in antinodes:
                val = '#'
            else:
                for (freq, positions) in antennas.items():
                    if (row, col) in positions:
                        val = freq
                        break
            print(val, end='')
        print()
