import sys

from twenty_one import load_input, get_shortest_seq_len


def main():
    if len(sys.argv) != 2:
        print(f'Usage: python {sys.argv[0]} <input_file>')
        sys.exit(1)
    input = load_input(sys.argv[1])
    total = 0
    for door_seq in input:
        shortest_len = get_shortest_seq_len(25, door_seq)
        total += int(door_seq[:-1]) * shortest_len
    print(total)


if __name__ == '__main__':
    main()
