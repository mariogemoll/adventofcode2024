import sys
import numpy as np

from thirteen import load_input, find_combination_with_constant


def main():
    machines = load_input(sys.argv[1])
    c = np.array([10000000000000, 10000000000000])
    tokens = 0
    for a, b, prize in machines:
        combination = find_combination_with_constant(a, b, prize, c)
        if combination is not None:
            num_a, num_b = combination
            if abs(num_a * a[0] + num_b * b[0] - prize[0] - c[0]) > 0:
                continue
            if abs(num_a * a[1] + num_b * b[1] - prize[1] - c[1]) > 0:
                continue
            tokens += num_a * 3 + num_b
    print(tokens)


if __name__ == '__main__':
    main()
