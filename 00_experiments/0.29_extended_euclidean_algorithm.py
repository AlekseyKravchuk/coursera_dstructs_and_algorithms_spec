def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# extended Euclidean algorithm
def xgcd(a, b):
    # base case
    if b == 0:
        x, y = 1, 0  # ax + by = gcd(a,b) => gcd(a,b)*x + 0*y = gcd(a,b) => x = 1, y = 0 (y can be whatever)
        return a, x, y

    # recursion body
    _gcd, x1, y1 = xgcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return _gcd, x, y


# calculates modulo multiplicative inverse for the given number 'a' by a given modulo 'm'
def modinv(a, m):
    _gcd, x, y = xgcd(a, m)

    if _gcd != 1:
        raise Exception('Multiplicative inverse does not exist!')
    else:
        return x % m


if __name__ == '__main__':
    a, b = map(int, input().split())
    # gcd, x, y = xgcd(a, b)
    # print(f'gcd({a}, {b}) = {gcd}, equation: {a}*({x}) + {b}*({y}) = {gcd}')
    _mod_inv = modinv(a, b)
    print(f'Multiplicative inverse of {a} by modulo {b} is {_mod_inv}')
