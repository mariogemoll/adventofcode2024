import sys

from twenty_four import load_input


def fire(op, in_a, in_b):
    if op == 'AND':
        return in_a and in_b
    elif op == 'OR':
        return in_a or in_b
    elif op == 'XOR':
        return in_a ^ in_b
    else:
        raise 'Unknown operator'


def main():
    if len(sys.argv) != 2:
        print(f'Usage: python {sys.argv[0]} <input_file>')
        sys.exit(1)
    initial_values, gates = load_input(sys.argv[1])

    wires = {}
    for wire, val in initial_values.items():
        wires[wire] = val

    while len(gates) > 0:
        gate_candidates = gates.copy()
        for gate in gate_candidates.items():
            (op, inputs), out = gate
            in_a, in_b = inputs
            if in_a in wires and in_b in wires:
                output = fire(op, wires[in_a], wires[in_b])
                wires[out] = output
                del gates[(op, inputs)]

    output_wires = {wire: val for wire, val in wires.items() if wire[:1] == 'z'}
    keys = list(output_wires.keys())
    keys.sort(reverse=True)
    bits = [1 if output_wires[key] else 0 for key in keys]
    print(int("".join(str(i) for i in bits), 2))


if __name__ == '__main__':
    main()
