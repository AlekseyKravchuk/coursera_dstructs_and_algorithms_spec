def gcd(a, b):
    a, b = max(a, b), min(a, b)
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return int(a * b / gcd(a, b))


def main():
    a, b = map(int, input().split())
    print(lcm(a, b))


if __name__ == '__main__':
    main()
