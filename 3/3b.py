from enum import Enum


def main():
    input = open('input').read()
    State = Enum('State', [
        ("ENABLED", 1), ("READING_FIRST_NUM", 2), ("READING_SECOND_NUM", 3), ("DISABLED", 4)
    ])

    sum = 0

    state = State.ENABLED

    cursor = 0

    first_num_str = ""
    second_num_str = ""
    while cursor < len(input):
        if state == State.ENABLED:
            if input[cursor:cursor+4] == 'mul(':
                state = State.READING_FIRST_NUM
                cursor += 4
            elif input[cursor:cursor+7] == 'don\'t()':
                state = State.DISABLED
                cursor += 7
            else:
                cursor += 1
        elif state == State.READING_FIRST_NUM:
            # check if digit
            if input[cursor].isdigit():
                first_num_str += input[cursor]
                cursor += 1
            elif input[cursor] == ',':
                state = State.READING_SECOND_NUM
                cursor += 1
            else:
                state = State.ENABLED
                first_num_str = ""
                second_num_str = ""
        elif state == State.READING_SECOND_NUM:
            if input[cursor].isdigit():
                second_num_str += input[cursor]
                cursor += 1
            elif input[cursor] == ')':
                result = int(first_num_str) * int(second_num_str)
                sum += result
                state = State.ENABLED
                first_num_str = ""
                second_num_str = ""
                cursor += 1
            else:
                first_num_str = ""
                second_num_str = ""
                state = State.ENABLED
        elif state == State.DISABLED:
            if input[cursor:cursor+4] == 'do()':
                state = State.ENABLED
                cursor += 4
            else:
                cursor += 1

    print(sum)


if __name__ == '__main__':
    main()
