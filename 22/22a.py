import sys
from twenty_two import load_input, secret_number_n

def main():
    input = load_input(sys.argv[1])

    print(sum([secret_number_n(val, 2000) for val in input]))


if __name__ == '__main__':
    main()
