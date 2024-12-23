import numpy as np


def load_input(filename):
    with open(filename, 'r') as file:
        parts = file.read().split('\n\n')
        machines = []
        for part in parts:
            lines = part.split('\n')
            if lines[-1] == '':
                lines = lines[:-1]
            assert len(lines) == 3
            a = tuple([int(val[2:]) for val in lines[0][10:].split(', ')])
            b = tuple([int(val[2:]) for val in lines[1][10:].split(', ')])
            prize = tuple([int(val[2:]) for val in lines[2][7:].split(', ')])
            machines.append((a, b, prize))
        return machines


def find_combination(a, b, prize):
    A = np.array([[a[0], b[0]], [a[1], b[1]]])
    b = np.array([prize[0], prize[1]])
    x, y = [round(val) for val in np.linalg.solve(A, b)]
    if x >= 0 and y >= 0 and np.all(np.isclose(A@np.array([x, y]), b)):
        return x, y
    else:
        return None


def find_combination_with_constant(a, b, prize, c):
    A = np.array([[a[0], b[0]], [a[1], b[1]]])
    b = np.array([prize[0], prize[1]])
    x = np.linalg.solve(A, b)

    # We have x s.t. Ax = b. Now we want to find y s.t. Ay = b + c.
    # Let y = x + z. Then:
    # A(x+z) = b + c
    # Az + Ax = b + c
    # Az + Ax = Ax + c
    # Az = c
    z = np.linalg.solve(A, c)
    y1, y2 = [round(val) for val in x + z]
    if y1 >= 0 and y2 >= 0 and np.all(np.isclose(A@np.array([y1, y2]), b + c)):
        return y1, y2
    else:
        return None
