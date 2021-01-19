import functools


def compare(a, b):
    ab = str(a) + str(b)
    ba = str(b) + str(a)

    if int(ab) > int(ba):
        return 1
    elif int(ab) < int(ba):
        return -1
    else:
        return 0


def main():
    n = int(input())
    numbers = list(map(int, input().split()))
    assert len(numbers) == n

    print(''.join(map(str, sorted(numbers, key=functools.cmp_to_key(compare), reverse=True))))


if __name__ == '__main__':
    main()
