import sys

from twenty_three import load_input, find_sets_of_three


def main():
    matrix, name_to_id, _ = load_input(sys.argv[1])
    names_starting_with_t = [name for name in list(name_to_id.keys()) if name[0] == 't']
    ids_of_t_names = [name_to_id[name] for name in names_starting_with_t]
    result = find_sets_of_three(matrix)
    count = 0
    for triple in result:
        if any([id in ids_of_t_names for id in triple]):
            count += 1
    print(count)


if __name__ == '__main__':
    main()
