def normal_fib_list(n):
    fibs = [0, 1]
    for i in range(2, n+1):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs


def generator_fib(n):
    x_1 = 0
    x_2 = 1

    yield x_1

    yield x_2

    for _ in range(2, n+1):
        yield x_1 + x_2
        x_1, x_2 = x_2, x_1 + x_2


# def get_Fib(n):
#     if n < 2:
#         return n
#     first = 0
#     second = 1
#     for _ in range(2, n+1):
#         first, second = second, first + second
#     return second


if __name__ == '__main__':
    n = 10

    normal_fibonacci = normal_fib_list(n)
    gen_fibonacci = generator_fib(n)

    print(normal_fibonacci)

    for x in gen_fibonacci:
        print(x, end=' ')
    print()
