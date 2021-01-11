def get_Fib(n):
    if n < 2:
        return n
    first = 0
    second = 1
    for _ in range(2, n + 1):
        first, second = second, first + second
    return second


def get_pisano_period(m):
    first, second = 0, 1
    for i in range(m ** 2):
        first, second = second, (first + second) % m
        if (first, second) == (0, 1):
            return i + 1


def get_remainder_Fib_N(n, m):
    pisano_period = get_pisano_period(m)
    idx = n % pisano_period
    return get_Fib(idx) % m


def main():
    n, m = map(int, input().split())
    # print(f'Pisano period for modulo {m} = {get_pisano_period(m)}')
    # print(f'F({n})mod{m} = {get_remainder_Fib_N(n, m)}')
    print(get_remainder_Fib_N(n, m))


if __name__ == '__main__':
    main()
