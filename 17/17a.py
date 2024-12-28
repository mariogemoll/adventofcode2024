import sys

from seventeen import load_input, run


def main():
    if len(sys.argv) != 2:
        print(f'Usage: python {sys.argv[0]} <input_file>')
        sys.exit(1)
    registers, program = load_input(sys.argv[1])
    output = run(registers, program)
    print(','.join([str(val) for val in output]))


if __name__ == '__main__':
    main()
