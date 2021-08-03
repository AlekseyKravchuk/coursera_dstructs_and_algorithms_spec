def factorization(n):
    ans = []
    initial = n
    d = 2
    while d * d <= initial:
        while n % d == 0:
            ans.append(d)
            n //= d
        d += 1
    return ans


def factorization_naive(n):
    ans = []
    for d in range(2, n + 1):
        if n % d == 0:
            # ans.append(d)
            while n % d == 0:
                ans.append(d)
                n //= d
    return ans


def factorization_naive_recursive(n):
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    if d * d <= n:
        ans = [d] + factorization_naive_recursive(n // d)
    else:
        ans = [n]
    return ans


if __name__ == '__main__':
    n = 120
    # n = 12
    print(factorization_naive(n))
    print(factorization(n))
    # print(factor_naive(n))
    # print(factorization_naive_recursive(n))
