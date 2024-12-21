from tqdm import tqdm

from common import load_input, sub, print_grid


def get_antinode(height, width, a, b):
    diff = sub(b, a)
    row, col = sub(a, diff)
    if 0 <= row < height and 0 <= col < width:
        return (row, col)
    else:
        return None


def main():
    height, width, antennas = load_input('input')
    antinodes = set()
    for freq in tqdm(antennas):
        num_pos = len(antennas[freq])
        for i in range(len(antennas[freq])):
            for j in range(i+1, num_pos):
                a, b = antennas[freq][i], antennas[freq][j]
                antinode_a = get_antinode(height, width, a, b)
                if antinode_a is not None:
                    antinodes.add(antinode_a)
                antinode_b = get_antinode(height, width, b, a)
                if antinode_b is not None:
                    antinodes.add(antinode_b)
    print_grid(height, width, antennas, antinodes)
    print(len(antinodes))


if __name__ == '__main__':
    main()
