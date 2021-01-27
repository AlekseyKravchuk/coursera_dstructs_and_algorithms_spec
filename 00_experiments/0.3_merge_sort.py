import numpy as np
import timeit
from math import floor


def merge(b, c):
    d = []
    i = j = 0

    while i < len(b) and j < len(c):
        if b[i] < c[j]:
            d.append(b[i])
            i += 1
        else:
            d.append(c[j])
            j += 1
    if i == len(b):
        d.extend(c[j:])
    else:
        d.extend(b[i:])
    return d


def merge_sort(x):
    if len(x) == 1:
        return x
    m = floor(len(x) / 2)

    b = merge_sort(x[:m])
    c = merge_sort(x[m:])

    return merge(b, c)


if __name__ == '__main__':
    # nums = np.random.randint(1, 101, 1000).tolist()
    # nums = [8, 4, 2, 5, 2, 19, 11, 17, 3, 100, 98, 18, 4]
    # nums = [7, 2, 5, 3, 7, 13, 1, 6]
    # a = [1, 3, 2, 4, 6, 5]
    # a = [1, 3, 5, 2, 4, 6]
    a = [2, 4, 6, 1, 3, 3]
    b = merge_sort(a.copy())

    print(f'unsorted array: {a}')
    print(f'sorted array: {b}')


