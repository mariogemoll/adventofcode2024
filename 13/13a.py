import sys

from thirteen import load_input, find_combination


def main():
    machines = load_input(sys.argv[1])
    tokens = 0
    for a, b, prize in machines:
        combination = find_combination(a, b, prize)
        if combination is not None:
            num_a, num_b = combination
            assert num_a * a[0] + num_b * b[0] == prize[0]
            assert num_a * a[1] + num_b * b[1] == prize[1]
            tokens += num_a * 3 + num_b
    print(tokens)


if __name__ == '__main__':
    main()
