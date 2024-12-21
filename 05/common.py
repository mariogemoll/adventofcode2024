def load_input(filename):
    lines = open(filename).read().split('\n')
    if lines[-1] == '':
        lines.pop()
    rules = []
    updates = []
    in_rules_section = True
    for line in lines:
        if line == '':
            in_rules_section = False
            continue
        if in_rules_section:
            first, second = [int(val) for val in line.split('|')]
            rules.append((first, second))
        else:
            updates.append([int(val) for val in line.split(',')])
    return rules, updates


def is_valid(rules, values):
    for i in range(len(values)):
        val = values[i]
        for a, b in rules:
            if a == val:
                for j in range(0, i):
                    if values[j] == b:
                        return False
            elif b == val:
                for j in range(i + 1, len(values)):
                    if values[j] == a:
                        return False
    return True