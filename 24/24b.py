import sys

from twenty_four import load_input


def gate(a, op, b):
    return (op, frozenset([a, b]))


def swap(gates, swapped, key_a, key_b):
    wire_a = gates[key_a]
    wire_b = gates[key_b]
    gates[key_a] = wire_b
    gates[key_b] = wire_a
    swapped += [wire_a, wire_b]


def main():
    if len(sys.argv) != 2:
        print(f'Usage: python {sys.argv[0]} <input_file>')
        sys.exit(1)

    initial_values, gates = load_input(sys.argv[1])
    num_adders = int(len(initial_values.keys()) / 2)
    num_id_digits = max(2, len(str(num_adders)))

    # Initial half adder
    id = str(0).rjust(num_id_digits, '0')
    s00 = gates[(gate(f'x{id}', 'XOR', f'y{id}'))]
    c00 = gates[gate(f'x{id}', 'AND', f'y{id}')]
    assert s00 == f'z{id}'

    # Loop through the full adders
    c = c00
    i = 1
    swapped = []
    while i < num_adders:
        id = str(i).rjust(num_id_digits, '0')
        x = f'x{id}'
        y = f'y{id}'
        z = f'z{id}'

        inter_1 = gates[gate(x, 'AND', y)]
        inter_2 = gates[gate(x, 'XOR', y)]

        if inter_1 == z:
            # Swap the output wire of (x AND y) with the one for (inter_2 XOR c)
            swap(gates, swapped, gate(x, 'AND', y), gate(inter_2, 'XOR', c))
            continue

        if not gate(inter_2, 'XOR', c) in gates and gate(inter_1, 'XOR', c) in gates:
            swap(gates, swapped, gate(x, 'AND', y), gate(x, 'XOR', y))
            continue

        inter_3 = gates[gate(inter_2, 'AND', c)]
        if inter_3 == z:
            swap(gates, swapped, gate(inter_2, 'AND', c), gate(inter_2, 'XOR', c))
            continue

        inter2_xor_c = gates[gate(inter_2, 'XOR', c)]
        if inter2_xor_c != z:
            # Find the gate with the output wire z
            other_key = None
            for key, out in gates.items():
                if out == z:
                    other_key = key
                    break
            assert other_key is not None
            swap(gates, swapped, gate(inter_2, 'XOR', c), other_key)
            continue

        s = gates[gate(inter_2, 'XOR', c)]
        assert s == z
        c = gates[gate(inter_1, 'OR', inter_3)]
        i += 1

    swapped.sort()
    print(','.join(swapped))


if __name__ == '__main__':
    main()
