def load_input(filename):
    # Read the lines of the input
    with open(filename, 'r') as file:
        lines = file.read().split('\n')
        if lines[-1] == '':
            lines = lines[:-1]

    # Identify the pairs, get the set of the computer names while at it
    pairs = []
    names = set()
    for line in lines:
        pair = line.split('-')
        assert len(pair) == 2
        pairs.append(pair)
        names.add(pair[0])
        names.add(pair[1])
    id_to_name = list(names)
    id_to_name.sort()

    # Convert the names to numbers
    name_to_id = {}
    for i, name in enumerate(id_to_name):
        name_to_id[name] = i
    pairs = [(name_to_id[pair[0]], name_to_id[pair[1]]) for pair in pairs]

    # Create an adjacency matrix
    n = len(names)
    matrix = []
    for row in range(n):
        matrix.append([False] * n)
    for a, b in pairs:
        matrix[a][b] = True
        matrix[b][a] = True

    return matrix, name_to_id, id_to_name


def find_sets_of_three(matrix):
    n = len(matrix)
    result = set()
    for i in range(n):
        for j in range(n):
            if not matrix[i][j]:
                continue
            for k in range(n):
                if matrix[i][k] and matrix[j][k]:
                    vals = [i, j, k]
                    vals.sort()
                    result.add(tuple(vals))
    return result


def find_group(matrix, pos):
    n = len(matrix)
    group = set([pos])
    to_visit = set([pos])
    visited = set()
    while len(to_visit) > 0:
        for pos in to_visit:
            visited.add(pos)
            new_to_visit = set()
            for neighbor_candidate in range(n):
                if neighbor_candidate in visited:
                    continue
                connected_to_all_members_so_far = True
                for member in group:
                    if not matrix[member][neighbor_candidate]:
                        connected_to_all_members_so_far = False
                        break
                if connected_to_all_members_so_far:
                    group.add(neighbor_candidate)
                    new_to_visit.add(neighbor_candidate)
        to_visit = new_to_visit
    return group


def find_biggest_groups(matrix):
    n = len(matrix)
    biggest_group_size = 0
    result = set()
    visited = set()
    for i in range(n):
        if i in visited:
            continue
        group = find_group(matrix, i)
        group_size = len(group)
        if group_size > biggest_group_size:
            biggest_group_size = group_size
            result = set()
        if group_size == biggest_group_size:
            group = list(group)
            group.sort()
            result.add(tuple(group))
    return result
