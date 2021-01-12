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


def get_last_digit_of_PARTIAL_sum(m, n):
    # There are 2 main ideas:
    # 1. sum(N_fib_nums) = (F(N+2) - 1), it is the case for dealing with corresponding remainders
    # 2. S[m, n] = S(n) - S[0, m) = S(n) - S(m-1), it is the case for dealing with corresponding remainders
    period = get_pisano_period(10)
    n_idx = (n + 2) % period
    m_idx = ((m - 1) + 2) % period
    last_dig_full_sum = (get_last_digit_Fib(n_idx) - 1) % 10
    last_dig_first_part_sum = (get_last_digit_Fib(m_idx) - 1) % 10

    return (last_dig_full_sum - last_dig_first_part_sum) % 10


def main():
    m, n = map(int, input().split())
    print(get_last_digit_of_PARTIAL_sum(m, n))


if __name__ == '__main__':
    main()
