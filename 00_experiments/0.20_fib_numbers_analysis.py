def fib_num_brute_force(i):
    if i < 2:
        return i
    return fib_num_brute_force(i - 1) + fib_num_brute_force(i - 2)


def fib_num_DP_BU(n):
    prev, next = 0, 1

    for i in range(n):
        prev, next = next, prev + next
    return prev


if __name__ == '__main__':
    n = 1000
    # lst = [fib_num_brute_force(x) for x in range(n)]
    # lst = [fib_num_DP_BU(x) for x in range(n + 1)]
    #
    # for idx in range(n + 1):
    #     print('|{:^6}'.format(idx), end='')
    # print('|')
    # for num in lst:
    #     print('|{:^6}'.format(num), end='')
    # print('|')

    print(fib_num_DP_BU(n))
