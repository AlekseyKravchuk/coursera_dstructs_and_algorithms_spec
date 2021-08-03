# check for number primality
def is_prime(n):
    d = 2

    # цикл while может остановиться только в 2-х случаях:
    # 1) значение делителя d вышло за рамки диапазона: d * d > n ==> число ПРОСТОЕ
    # 2) был найден делитель, т.е. остаток (n % d) стал равен 0 ==> при выходе из цикла d: d * d < n
    while d * d <= n and n % d != 0:
        d += 1

    # ==> число является ПРОСТЫМ только в том случае, если цикл завершился по причине d * d > n
    return d * d > n


def is_prime_naive(n):
    for d in range(2, n):
        if n % d == 0:
            return False
    return True


def print_check_if_prime(n):
    s = 'The number {n} is {state}.'.format(n=n, state='prime' if is_prime(n) else 'not prime')
    print(s)


def stress_test(end=1000000):
    for n in range(2, end):
        res = is_prime(n)
        res_naive = is_prime_naive(n)
        if res_naive == res:
            print(f'{n} is prime')
        else:
            print(f'{res_naive} != {res}, n = {n}')
            break


if __name__ == '__main__':
    n = int(input())
    print_check_if_prime(n)

    # stress_test()
