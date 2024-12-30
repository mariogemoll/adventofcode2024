import sys

from twenty import solution


def main():
    if len(sys.argv) != 2:
        print(f'Usage: python {sys.argv[0]} <input_file>')
        sys.exit(1)
    print(solution(sys.argv[1], 20))


if __name__ == '__main__':
    main()
