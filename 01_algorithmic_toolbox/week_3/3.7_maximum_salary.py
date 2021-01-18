import functools


def compare(num_1, num_2):
    l1 = len(num_1)
    l2 = len(num_2)


def main():
    n = int(input())
    numbers = list(map(int, input().split()))
    assert len(numbers) == n
    res_lst = sorted(numbers, key=functools.cmp_to_key(compare))
    print(res_lst)


if __name__ == '__main__':
    main()
