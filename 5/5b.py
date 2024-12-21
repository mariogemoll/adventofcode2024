from math import floor
from common import load_input, is_valid


def swap(values, i, j):
    swp = values[j]
    values[j] = values[i]
    values[i] = swp


def make_valid(rules, values):
    for i in range(len(values)):
        val = values[i]
        for a, b in rules:
            if a == val:
                for j in range(0, i):
                    if values[j] == b:
                        swap(values, i, j)
                        return make_valid(rules, values)
            elif b == val:
                for j in range(i + 1, len(values)):
                    if values[j] == a:
                        swap(values, i, j)
                        return make_valid(rules, values)
    return values


def main():
    rules, updates = load_input('input')
    sum = 0
    for update in updates:
        if not is_valid(rules, update):
            valid_update = make_valid(rules, update)
            sum += valid_update[floor(len(valid_update) / 2)]
    print(f'Sum: {sum}')


if __name__ == '__main__':
    main()
