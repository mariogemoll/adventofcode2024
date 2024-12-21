def xmas_at(input, row, col):
    center = input[row][col]
    ul = input[row - 1][col - 1]
    ur = input[row - 1][col + 1]
    ll = input[row + 1][col - 1]
    lr = input[row + 1][col + 1]
    str_1 = ul + center + lr
    str_2 = ur + center + ll
    return (str_1 == 'MAS' or str_1 == 'SAM') and (str_2 == 'MAS' or str_2 == 'SAM')


def main():
    lines = open('input').read().split('\n')
    if lines[-1] == '':
        lines.pop()
    count = 0
    for row in range(1, len(lines) - 1):
        for col in range(1, len(lines[0]) - 1):
            if xmas_at(lines, row, col):
                count += 1
    print(count)


if __name__ == '__main__':
    main()
