def get_pisano_period(m):
    first, second = 0, 1
    for i in range(m ** 2):
        first, second = second, (first + second) % m
        if (first, second) == (0, 1):
            return i + 1


def get_last_digit_Fib(n):
    if n < 2:
        return n
    first, second = 0, 1

    for _ in range(2, n + 1):
        first, second = second % 10, (first + second) % 10
    return second


def get_last_digit_of_sum_of_N_Fib_nums(n):
    # the key idea is that sum(N_fib_nums) = (F(N+2) - 1)
    # so it is the case for dealing with corresponding remainders
    period = get_pisano_period(10)
    idx = (n + 2) % period
    last_digit = get_last_digit_Fib(idx)
    return (last_digit - 1) % 10


def main():
    n = int(input())
    # print(f'last digit of sum of {n} first numbers in Fibonacci sequence = {get_last_digit_of_sum_of_N_Fib_nums(n)}')
    print(get_last_digit_of_sum_of_N_Fib_nums(n))


if __name__ == '__main__':
    main()
