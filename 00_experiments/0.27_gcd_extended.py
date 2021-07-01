def gcd(a, b):
    a, b = max(a, b), min(a, b)
    while b != 0:
        a, b = b, a % b
    return a


def gcd_recursive(a, b):
    a, b = max(a, b), min(a, b)
    if not b:
        return a
    else:
        return gcd(b, a % b)


def gcd_extended(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = gcd_extended(b, a % b)
        return d, y, x - y * (a // b)


if __name__ == '__main__':
    a, b = map(int, input().split())
    # print(f'gcd({a},{b}) = {gcd(a, b)}')
    print(f'gcd_extended({a},{b}) = {gcd_extended(a, b)}')
    # print(f'gcd_rec({a},{b}) = {gcd_recursive(a, b)}')
