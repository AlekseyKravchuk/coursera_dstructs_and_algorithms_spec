def gcd_iter(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def gcd_recur(a, b):
    # return gcd_recur(a, b) if b != 0 else a
    if b == 0:
        return a
    return gcd_recur(a, b)


if __name__ == '__main__':
    a, b = map(int, input().split())
    a, b = max(a, b), min(a, b)
    # print(f'gcd({a}, {b}) = {gcd_iter(a, b)}')
    print(f'gcd({a}, {b}) = {gcd_iter(a, b)}')
