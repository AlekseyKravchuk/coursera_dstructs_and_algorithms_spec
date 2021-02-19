def fib_num_recursive(n):
    if n < 2:
        return n

    return fib_num_recursive(n - 2) + fib_num_recursive(n - 1)


def fib_num_using_array(n):
    x = [None] * (n + 1)
    x[0] = 0
    x[1] = 1
    for i in range(2, n + 1):
        x[i] = x[i - 1] + x[i - 2]
    return x[-1]


def fib_num_simple(n):
    a = 0
    b = 1
    for i in range(2, n + 1):
        c = a + b
        a, b = b, c
    return c


if __name__ == '__main__':
    n = int(input())
    print(fib_num_recursive(n))
    print(fib_num_using_array(n))
    print(fib_num_simple(n))
