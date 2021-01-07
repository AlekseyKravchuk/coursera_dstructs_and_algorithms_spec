def get_last_digit_Fib(n):
    if n < 2:
        return n
    first = 0
    second = 1
    for _ in range(2, n + 1):
        first, second = second % 10, (first + second) % 10
    return second


def main():
    n = int(input())
    print(get_last_digit_Fib(n))


if __name__ == '__main__':
    main()
