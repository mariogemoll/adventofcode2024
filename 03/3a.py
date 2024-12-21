import re


def main():
    input = open('input').read()
    sum = 0
    for match in re.finditer(r'mul\((\d+),(\d+)\)', input):
        sum += int(match.groups()[0]) * int(match.groups()[1])
    print(sum)


if __name__ == '__main__':
    main()