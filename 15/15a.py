import sys
from tqdm import tqdm

from fifteen import load_input, locate_robot, get_next, move_train, gps


def move(grid, movement):
    robot_pos = locate_robot(grid)
    train = [(robot_pos, '@')]
    while True:
        head_row, head_col = train[0][0]
        next_row, next_col = get_next(head_row, head_col, movement)
        next = grid[next_row][next_col]
        if next == '#':
            return
        elif next == '.':
            move_train(grid, movement, train)
            return
        elif next == 'O':
            train.insert(0, ((next_row, next_col), 'O'))
            continue
        else:
            raise Exception('Not implemented')


def main():
    if len(sys.argv) != 2:
        print(f'Usage: python {sys.argv[0]} <input_file>')
        sys.exit(1)
    grid, movements = load_input(sys.argv[1])
    for movement in tqdm(movements):
        move(grid, movement)
    print(gps('O', grid))


if __name__ == '__main__':
    main()
