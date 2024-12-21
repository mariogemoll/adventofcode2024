from tqdm import tqdm

from common import load_input, sub, print_grid


def get_antinodes(height, width, a, b):
    diff = sub(b, a)
    row, col = sub(a, diff)
    antinodes = []
    while 0 <= row < height and 0 <= col < width:
        antinodes.append((row, col))
        row, col = sub((row, col), diff)
    return antinodes


def main():
    height, width, antennas = load_input('input')
    antinodes = set()
    for freq in tqdm(antennas):
        num_pos = len(antennas[freq])
        for i in range(len(antennas[freq])):
            for j in range(i+1, num_pos):
                a, b = antennas[freq][i], antennas[freq][j]
                antinodes.add(a)
                antinodes.add(b)
                antinodes_a = get_antinodes(height, width, a, b)
                antinodes_b = get_antinodes(height, width, b, a)
                antinodes.update(antinodes_a)
                antinodes.update(antinodes_b)
    print_grid(height, width, antennas, antinodes)
    print(len(antinodes))


if __name__ == '__main__':
    main()
