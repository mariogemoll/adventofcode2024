from common import is_safe


def main():
    safe_count = 0
    # Read file line by line
    with open('input') as f:
        while True:
            line = f.readline()
            if not line:
                break
            # split at whitespace
            levels = [int(part) for part in line.split()]
            if is_safe(levels):
                safe_count += 1
    print(f'Safe count: {safe_count}')


if __name__ == '__main__':
    main()