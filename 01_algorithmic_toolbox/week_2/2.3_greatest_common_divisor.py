# def gcd_recursive(a, b):
#     if b == 0:
#         return a
#     else:
#         return gcd(b, a % b)


def gcd(a, b):
    a, b = max(a, b), min(a, b)
    while b:
        a, b = b, a % b
    return a


def main():
    a, b = map(int, input().split())
    print(gcd(a, b))


if __name__ == '__main__':
    main()
