import sys

from twenty_three import load_input, find_biggest_groups


def main():
    matrix, name_to_id, id_to_name = load_input(sys.argv[1])
    result = find_biggest_groups(matrix)
    assert len(result) == 1
    print(','.join([id_to_name[id] for id in list(result)[0]]))


if __name__ == '__main__':
    main()
