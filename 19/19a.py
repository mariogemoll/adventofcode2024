import sys

from nineteen import load_input


def possible(towels, design):
    if design == '':
        return True
    for towel in towels:
        if len(towel) <= len(design) and design[:len(towel)] == towel:
            if possible(towels, design[len(towel):]):
                return True
    return False


def main():
    if len(sys.argv) != 2:
        print(f'Usage: python {sys.argv[0]} <input_file>')
        sys.exit(1)
    towels, designs = load_input(sys.argv[1])
    print(sum([1 for design in designs if possible(towels, design)]))


if __name__ == '__main__':
    main()
