def get_Fib(n):
    if n < 2:
        return n
    first = 0
    second = 1
    for _ in range(2, n):
        first, second = second, first + second
    return second


def main():
    n = int(input('Type in the n in order to calculate F(n): '))
    print(f'F({n}) = {get_Fib(n)}')


if __name__ == '__main__':
    main()
