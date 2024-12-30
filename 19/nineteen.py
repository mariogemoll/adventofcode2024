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
    towels_section, designs = get_sections(filename)
    return frozenset(towels_section[0].split(', ')), designs
