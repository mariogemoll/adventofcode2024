import sys


def blink(memory, val, blinks_left):
    if (val, blinks_left) in memory:
        return memory[(val, blinks_left)]

    result = None
    if blinks_left == 0:
        result = 1
    elif val == 0:
        result = blink(memory, 1, blinks_left - 1)
    else:
        val_str = str(val)
        val_str_len = len(val_str)
        if val_str_len % 2 == 0:
            midpoint = int(val_str_len/2)
            first_val = int(val_str[:midpoint])
            second_val = int(val_str[midpoint:])
            result = blink(memory, first_val, blinks_left - 1) + blink(memory, second_val, blinks_left - 1)
        else:
            result = blink(memory, val * 2024, blinks_left - 1)
    memory[(val, blinks_left)] = result
    return result


def main():
    filename = sys.argv[1]
    num_blinks = int(sys.argv[2])
    input = [int(x) for x in open(filename).read().split(' ')]
    memory = {}
    sum = 0
    for val in input:
        sum += blink(memory, val, num_blinks)
    print(sum)


if __name__ == '__main__':
    main()
