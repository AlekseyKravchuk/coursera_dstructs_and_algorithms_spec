from collections import Counter
from math import floor


def main():
    n = int(input())
    cnt = Counter(map(int, input().split()))

    if cnt.most_common(1)[0][1] > floor(n / 2):
        print(1)
    else:
        print(0)


if __name__ == '__main__':
    main()
