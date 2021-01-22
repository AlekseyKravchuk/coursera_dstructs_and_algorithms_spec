import numpy as np
import timeit
from math import floor
import random
from collections import deque


def selection_sort(x):
    for i, elm in enumerate(x):
        min_idx = i
        for j in range(i + 1, len(x)):
            if x[j] < x[min_idx]:
                min_idx = j
        if min_idx != i:
            x[min_idx], x[i] = x[i], x[min_idx]
    return x


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


def main():
    nums = np.random.randint(1, 101, 1000).tolist()
    # nums = [8, 4, 2, 5, 2, 19, 11, 17, 3, 100, 98, 18, 4]
    # nums = [7, 2, 5, 3, 7, 13, 1, 6]

    t_o_sel_sort = timeit.Timer(lambda: selection_sort(nums[:]))
    t_o_default_sort = timeit.Timer(lambda: sorted(nums[:]))
    t_o_merge_sort = timeit.Timer(lambda: merge_sort(nums[:]))
    execution_num = 10

    # print(f'unsorted array: {nums}')
    # print(f'Sorting by my selection_sort(x) function: {selection_sort(nums[:])}, time2sort = {t_o_sel_sort.timeit(execution_num):.2}')
    # print(f'Sorting by DEFAULT sort function: {sorted(nums[:])}, time2sort = {t_o_default_sort.timeit(execution_num):.2}')
    # print(f'Sorting by merge_sort(x): {merge_sort(nums[:])}, time2sort = {t_o_merge_sort.timeit(execution_num):.2}')

    print(f'SORTED by my selection_sort(x) function: time2sort = {t_o_sel_sort.timeit(execution_num):.4f} seconds')
    print(f'SORTED by DEFAULT sort function: time2sort = {t_o_default_sort.timeit(execution_num):.4f} seconds')
    print(f'SORTED by merge_sort(x): time2sort = {t_o_merge_sort.timeit(execution_num):.4f} seconds')


if __name__ == '__main__':
    main()
