from common import checksum


def load_input(filename):
    with open(filename, 'r') as f:
        line = f.read().strip()
        fs = []
        id = 0
        for i in range(len(line)):
            length = int(line[i])
            if i % 2 == 0:
                for _ in range(length):
                    fs.append(id)
                id += 1
            else:
                for _ in range(length):
                    fs.append('.')
        return fs


def main():
    fs = load_input('input')
    left = 0
    right = len(fs) - 1
    while left < right:
        # Move left to the first available free space
        if fs[left] != '.':
            left += 1
            continue

        # Skip any white space on the right
        if fs[right] == '.':
            right -= 1
            continue

        fs[left] = fs[right]
        fs[right] = '.'
    print(checksum(fs))


if __name__ == '__main__':
    main()
