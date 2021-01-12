def get_pisano_period(m):
    first, second = 0, 1
    for i in range(m ** 2):
        first, second = second, (first + second) % m
        if (first, second) == (0, 1):
            return i + 1


def get_last_digit_of_sum_of_squares_of_Fib_Nums(n):
    pisano_period = get_pisano_period(10)
    idx = n % pisano_period
    if idx < 2:
        return idx
    first, second = 0, 1

    for _ in range(2, idx + 2):
        first, second = second % 10, (first + second) % 10
    return (first * second) % 10


def main():
    n = int(input())
    print(get_last_digit_of_sum_of_squares_of_Fib_Nums(n))


if __name__ == '__main__':
    main()
