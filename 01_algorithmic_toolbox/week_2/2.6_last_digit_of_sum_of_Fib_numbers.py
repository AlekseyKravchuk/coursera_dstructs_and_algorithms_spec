def get_pisano_period(m):
    first, second = 0, 1
    for i in range(m ** 2):
        first, second = second, (first + second) % m
        if (first, second) == (0, 1):
            return i + 1


def get_remainder_of_sum_of_N_Fib_nums_in_Pisano_period(m):
    period = get_pisano_period(m)
    first, second = 0, 1
    fib_sum = first + second

    for _ in range(period - 2):
        first, second = second, (first + second) % 10
        fib_sum = (fib_sum + second) % 10
    return fib_sum


def main():
    m = int(input())
    print(f'remainder of sum of Fib numbers in period for modulo {m} = {get_remainder_of_sum_of_N_Fib_nums_in_Pisano_period(m)}')


if __name__ == '__main__':
    main()
