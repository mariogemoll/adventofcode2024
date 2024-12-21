import re


def get_ltr_diag(input, start_row, start_col):
    row = start_row
    col = start_col
    result = []
    while True:
        if row >= len(input) or col >= len(input[0]):
            break
        result.append(input[row][col])
        row += 1
        col += 1
    return "".join(result)


def get_rtl_diag(input, start_row, start_col):
    row = start_row
    col = start_col
    result = []
    while True:
        if row >= len(input) or col < 0:
            break
        result.append(input[row][col])
        row += 1
        col -= 1
    return "".join(result)


def get_left_to_right_diagonals(input):
    num_rows = len(input)
    num_cols = len(input[0])

    diagonals = []

    # In the first row, we need to extract diagonals starting from each cell
    for col in range(num_cols):
        diagonals.append(get_ltr_diag(input, 0, col))

    # For all other rows, we just need the diagonal starting from the first cell
    for row in range(1, num_rows):
        diagonals.append(get_ltr_diag(input, row, 0))
    return diagonals


def get_right_to_left_diagonals(input):
    num_cols = len(input[0])

    diagonals = []

    # In the first row, we need to extract diagonals starting from each cell
    for col in range(num_cols - 1, -1, -1):
        diagonals.append(get_rtl_diag(input, 0, col))

    # For all other rows, we just need the diagonal starting from the last cell
    for row in range(1, num_cols):
        diagonals.append(get_rtl_diag(input, row, num_cols - 1))
    return diagonals 


def get_cols(input):
    num_rows = len(input)
    num_cols = len(input[0])

    cols = []

    for col in range(num_cols):
        col_data = []
        for row in range(num_rows):
            col_data.append(input[row][col])
        cols.append("".join(col_data))
    return cols


def main():
    lines = open('input').read().split('\n')
    if lines[-1] == '':
        lines.pop()
    seqs = []
    seqs.extend(lines)
    seqs.extend(get_cols(lines))
    seqs.extend(get_left_to_right_diagonals(lines))
    seqs.extend(get_right_to_left_diagonals(lines))
    reverse = []
    for seq in seqs:
        reverse.append("".join(reversed(seq)))
    seqs.extend(reverse)

    regex = re.compile(r'XMAS')
    count = 0
    for seq in seqs:
        count += len(regex.findall(seq))
    print(f"Found {count} instances of XMAS")


if __name__ == '__main__':
    main()
