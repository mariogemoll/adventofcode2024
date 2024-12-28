import sys

from seventeen import load_input, run


def main():
    if len(sys.argv) != 2:
        print(f'Usage: python {sys.argv[0]} <input_file>')
        sys.exit(1)
    _, program = load_input(sys.argv[1])

    # The following worked with my input, not sure if it works with all (AOC 2024 day 17) inputs.
    # Important observations about the program in my input:
    # * There is a single loop.
    # * Each iteration of the loop "processes" 3 bits of A.
    # * B and C are set in each iteration of the loop and depend on A only.
    # We try to get the program to output longer and longer substrings of itself, starting from the
    # last element.
    a_candidates = [0]
    for n in range(1, len(program) + 1):
        partial_program = program[len(program) - n:]
        new_a_candidates = []
        for a in a_candidates:
            a = a << 3
            for i in range(8):
                output = run({'A': a + i, 'B': 0, 'C': 0}, program)
                if output == partial_program:
                    new_a_candidates.append(a + i)
        if len(new_a_candidates) == 0:
            raise Exception('Something went wrong')
        a_candidates = new_a_candidates

    a_candidates.sort()
    print(a_candidates[0])


if __name__ == '__main__':
    main()
