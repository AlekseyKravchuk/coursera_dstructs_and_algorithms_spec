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
    x = 59
    s = 'baab'
    coeffs = [ord(ch) for ch in s]
    print(f'coeffs = {coeffs}')
    res = evaluate_polynom_gorner(coeffs, x)
    print(res)


    # coeffs = [5, 4, 1, 6]  # 5x^3 + 4x^2 + 1x^1 + 6
    # coeffs = [1, 2, 3, 4, 5, 6]  # x^5 + 2x^4 + 3x^3 + 4x^2 + 5x + 6
    # res = evaluate_polynom_gorner_modulo_q(coeffs, 3, 17)

    # s = 'HellO'
    # coeffs = list(map(ord, s))  # coefficients of polynomial of degree (self.M - 1)
    # x = 263
    # p = 1000000007
    # res = evaluate_polynom_gorner_modulo_q(coeffs, x, p)
    # print(repr_polynomial(coeffs))
    # print(f'val = {res}')
