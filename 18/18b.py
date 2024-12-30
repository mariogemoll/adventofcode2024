import sys

from yaspin import yaspin

from eighteen import load_input, find_shortest_path_length


@yaspin()
def find_breaking_pos(input):
    n = 1025
    while True:
        if find_shortest_path_length(set(input[:n])) is None:
            return input[n-1]
        n += 1


def main():
    if len(sys.argv) != 2:
        print(f'Usage: python {sys.argv[0]} <input_file>')
        sys.exit(1)
    input = load_input(sys.argv[1])
    print(find_breaking_pos(input))


if __name__ == '__main__':
    main()
