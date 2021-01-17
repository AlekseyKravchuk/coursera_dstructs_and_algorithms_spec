def get_max_number_of_prizes(n):
    if n <= 2:
        print(n)
        for i in range(1, n + 1):
            print(i, end=' ')
    cnt = 0
    i = 1
    while n > 0:
        n -= i
        i += 1
        if n >= 0:
            cnt += 1

    if n == 0:
        print(cnt)
        for i in range(1, cnt+1):
            print(i, end=' ')
    else:
        print('IMPOSSIBLE to represent as sum of terms of arithmetic progression')
        print(f'n = {n}')
        print(f'cnt = {cnt}')


def main():
    n = int(input())
    get_max_number_of_prizes(n)


if __name__ == '__main__':
    main()
