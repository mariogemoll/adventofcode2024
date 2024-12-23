import sys
from tqdm import tqdm

from fourteen import load_input, update_positions, generate_grid, calculate_safety_factor, draw_grid


def flatten(positions):
    flat_list = []
    for x, y in positions:
        flat_list.append(x)
        flat_list.append(y)
    return tuple(flat_list)


def main():
    initial_positions, velocities = load_input(sys.argv[1])

    flat_initial_position = flatten(initial_positions)
    
    positions = initial_positions.copy()

    # At some point we'll find a loop, i.e. all robots will be in the same position as in the
    # beginning. We'll try to find the number of iterations in the loop. We'll also want to rank
    # all the grids by some randomness score to identify the one with the christmas tree. I tried
    # entropy but didn't get far with this, however simply taking the safety factor worked (I must
    # admit I got the safety factor idea from reddit).
    safety_factors = []
    i = 0
    print('Scoring all possible formations...')
    while True:
        update_positions(velocities, positions)
        i += 1
        safety_factor = calculate_safety_factor(generate_grid(positions))
        safety_factors.append((safety_factor, i))
        flat_positions = flatten(positions)
        if flat_positions == flat_initial_position:
            break

    # The christmas tree formation is the one with the lowest safety factor
    safety_factors.sort()
    xmas_iteration = safety_factors[0][1]

    positions = initial_positions.copy()
    print('Generating christmas tree...')
    for i in tqdm(range(xmas_iteration)):
        update_positions(velocities, positions)

    print()
    draw_grid(generate_grid(positions))
    print()
    print(xmas_iteration)


if __name__ == '__main__':
    main()
