def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def gcd_extended(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = gcd_extended(b, a % b)
        return d, y, x - y * (a // b)


if __name__ == '__main__':
    a, b = map(int, input().split())
    # print(f'gcd({a},{b}) = {gcd(max(a,b), min(a,b))}')
    print(gcd_extended(a, b))