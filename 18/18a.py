import sys
from eighteen import load_input, find_shortest_path_length


def main():
    if len(sys.argv) != 2:
        print(f'Usage: python {sys.argv[0]} <input_file>')
        sys.exit(1)
    input = load_input(sys.argv[1])
    print(find_shortest_path_length(set(input[:1024])))


if __name__ == '__main__':
    main()
