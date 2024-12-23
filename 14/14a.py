import sys

from fourteen import load_input, update_positions, generate_grid, calculate_safety_factor


def main():
    positions, velocities = load_input(sys.argv[1])

    for i in range(100):
        update_positions(velocities, positions)

    grid = generate_grid(positions)
    print(calculate_safety_factor(grid))


if __name__ == '__main__':
    main()
