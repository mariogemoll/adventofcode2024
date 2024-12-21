from tqdm import tqdm

from common import load_input, find_combination


def main():
    input = load_input('input')
    found = 0
    total = 0
    pbar = tqdm(input)
    for result, vals in pbar:
        found, _ = find_combination(result, vals, True)
        if found:
            total += result
            pbar.set_postfix({'found': found, 'total': total})
    print(f'Total: {total}')


if __name__ == '__main__':
    main()
