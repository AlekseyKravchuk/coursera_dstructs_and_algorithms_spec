# evaluates polynomial specified by its 'coeffs' in the given point 'x'
def evaluate_polynom_gorner_modulo_q(coeffs, x, q):
    p = 0
    for i, coeff in enumerate(coeffs):
        p = (p * x + coeff) % q
    return p


def evaluate_polynom_gorner(coeffs, x):
    p = 0
    for i, coeff in enumerate(coeffs):
        p = p * x + coeff
    return p


def repr_polynomial(coeffs):
    s = ''
    for i, coeff in enumerate(coeffs):
        s += str(coeff) + f'x^{len(coeffs) - 1 - i}' + f'{" + " if i != len(coeffs) - 1 else ""}'
    return s


if __name__ == '__main__':
    # coeffs = [5, 4, 1, 6]  # 5x^3 + 4x^2 + 1x^1 + 6
    coeffs = [1, 2, 3, 4, 5, 6]  # x^5 + 2x^4 + 3x^3 + 4x^2 + 5x + 6
    # res = evaluate_polynom_gorner_modulo_q(coeffs, 3, 17)
    res = evaluate_polynom_gorner(coeffs, 3)
    print(repr_polynomial(coeffs))
    print(f'val = {res}')
