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


def get_register_content(s):
    letter = s[9:10]
    val = int(s[12:])
    return letter, val


def load_input(filename):
    register_section, program_section = get_sections(filename)
    registers = {}
    for line in register_section:
        letter, content = get_register_content(line)
        registers[letter] = content
    assert list(registers.keys()) == ['A', 'B', 'C']
    assert len(program_section) == 1
    program_str = program_section[0][9:]
    program = [int(val) for val in program_str.split(',')]
    return registers, program


def combo(registers, operand):
    if 0 <= operand <= 3:
        return operand
    elif operand == 4:
        return registers['A']
    elif operand == 5:
        return registers['B']
    elif operand == 6:
        return registers['B']
    else:
        raise Exception('Invalid combo operand')


def div(registers, operand):
    return int(registers['A'] / (2 ** combo(registers, operand)))


def run(registers, program):
    ptr = 0
    output = []
    while ptr < len(program):
        opcode = program[ptr]
        operand = program[ptr + 1]
        next_ptr = ptr+2
        if opcode == 0:
            # adv
            div_result = div(registers, operand)
            registers['A'] = div_result
        elif opcode == 1:
            # bxl
            xor_result = registers['B'] ^ operand
            registers['B'] = xor_result
        elif opcode == 2:
            # bst
            mod_result = combo(registers, operand) % 8
            registers['B'] = mod_result
        elif opcode == 3:
            # jnz
            if registers['A'] != 0:
                next_ptr = operand
        elif opcode == 4:
            # bxc
            xor_result = registers['B'] ^ registers['C']
            registers['B'] = xor_result
        elif opcode == 5:
            # out
            mod_result = combo(registers, operand) % 8
            output.append(mod_result)
        elif opcode == 6:
            # bdv
            div_result = div(registers, operand)
            registers['B'] = div_result
        elif opcode == 7:
            # cdv
            div_result = div(registers, operand)
            registers['C'] = div_result
        else:
            raise Exception('Invalid opcode')

        ptr = next_ptr
    return output
