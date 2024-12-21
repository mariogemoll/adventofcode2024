from common import load_input, run
from tqdm import tqdm
from multiprocessing import Pool


def find_dots(grid):
    dots = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '.':
                dots.append((row, col))
    return dots


def process_dot(args):
    original_grid, row, col, direction, obstacle_row, obstacle_col = args
    grid = [list(vals) for vals in original_grid]
    grid[obstacle_row][obstacle_col] = '#'
    loop, _ = run(grid, row, col, direction)
    return loop


def main():
    original_grid, row, col, direction = load_input('input')
    dots = find_dots(original_grid)
    num_loops = 0

    with Pool() as pool:
        args = [(original_grid, row, col, direction, obstacle_row, obstacle_col) for obstacle_row, obstacle_col in dots]
        pbar = tqdm(pool.imap(process_dot, args), total=len(dots))
        for loop in pbar:
            if loop:
                num_loops += 1
                pbar.set_postfix({'num_loops': num_loops})

    print()
    print(f"Found {num_loops} loops")


if __name__ == '__main__':
    main()