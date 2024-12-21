from math import floor
from common import load_input, is_valid


def main():
    rules, updates = load_input('input')
    sum = 0
    for update in updates:
        if is_valid(rules, update):
            sum += update[floor(len(update) / 2)]
    print(f'Sum: {sum}')


if __name__ == '__main__':
    main()
