def get_lines(filename):
    with open(filename, 'r') as file:
        lines = file.read().split('\n')
        if lines[-1] == '':
            lines = lines[:-1]
    return lines


def get_sections(filename):
    lines = get_lines(filename)
    sections = []
    current_section = []
    for line in lines:
        if line == '':
            sections.append(current_section)
            current_section = []
        else:
            current_section.append(line)
    sections.append(current_section)
    return sections


def load_input(filename):
    sections = get_sections(filename)
    assert len(sections) == 2

    initial_values = {}
    for line in sections[0]:
        wire, val_str = line.split(': ')
        initial_values[wire] = int(val_str)

    gates = {}
    for line in sections[1]:
        wire_a, op, wire_b, _, wire_out = line.split(' ')
        gates[(op, frozenset([wire_a, wire_b]))] = wire_out

    return initial_values, gates
