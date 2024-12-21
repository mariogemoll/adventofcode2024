from collections import Counter


def main():
    with open('input') as f:
        lines = f.readlines()

    vals_a = []
    vals_b = []

    for line in lines:
        # split at whitespace
        parts = line.split()
        assert len(parts) == 2
        vals_a.append(int(parts[0]))
        vals_b.append(int(parts[1]))

    assert len(vals_a) == len(vals_b)

    vals_a.sort()
    vals_b.sort()

    distances = []
    for i in range(len(vals_a)):
        distances.append(abs(vals_a[i] - vals_b[i]))

    total_distance = sum(distances)
    print(f'Total distance: {total_distance}')

    c = Counter()
    for val in vals_b:
        c[val] += 1

    score = 0
    for val in vals_a:
        score += c[val] * val
    print(f'Similarity score: {score}')


if __name__ == '__main__':
    main()