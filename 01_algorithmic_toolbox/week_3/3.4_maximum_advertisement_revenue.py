import numpy as np


def main():
    n = int(input())
    a = np.array(sorted([x for x in map(int, input().split())], reverse=True))
    b = np.array(sorted([y for y in map(int, input().split())], reverse=True))

    assert len(a) == len(b) == n

    # print(sum(a * b))
    print(np.dot(a, b))


if __name__ == '__main__':
    main()
