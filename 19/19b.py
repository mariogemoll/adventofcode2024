import sys
from functools import cache

from tqdm import tqdm

from nineteen import load_input


@cache
def num_ways(towels, design):
    if design == '':
        return 1
    ways = 0
    for towel in towels:
        if len(towel) <= len(design) and design[:len(towel)] == towel:
            ways += num_ways(towels, design[len(towel):])
    return ways


def main():
    if len(sys.argv) != 2:
        print(f'Usage: python {sys.argv[0]} <input_file>')
        sys.exit(1)
    towels, designs = load_input(sys.argv[1])
    print(sum([num_ways(towels, design) for design in tqdm(designs)]))


if __name__ == '__main__':
    main()
