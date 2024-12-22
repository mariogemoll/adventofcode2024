def load_input(filename):
    with open(filename, 'r') as file:
        return [int(x) for x in file.readlines()]


def secret_number(input):
    mul_result = input * 64
    result = input ^ mul_result
    result = result % 16777216

    div_result = int(result / 32)
    result = result ^ div_result
    result = result % 16777216

    mul_result = result * 2048
    result = result ^ mul_result
    result = result % 16777216
    return result


def secret_number_n(val, n):
    for _ in range(n):
        val = secret_number(val)
    return val


def price_seq(x, num_iterations):
    price = x % 10
    prev_price = price
    result = [(price, None)]
    for _ in range(num_iterations):
        x = secret_number(x)
        price = x % 10
        result.append((price, price - prev_price))
        prev_price = price
    return result
