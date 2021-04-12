"""
Test input:
4
50 20
20 1
1 10
10 100
"""
from typing import List


def check_if_matrix_sizes_consistent(sizes: List[int]) -> bool:
    for i in range(1, len(sizes) - 2, 2):
        if sizes[i] != sizes[i + 1]:
            return False
    return True


def matrix_mult_TD(F, i, j, sizes):
    if F[i][j] is None:
        if i == j:
            F[i][j] = 0
        else:
            for k in range(i, j):
                l = matrix_mult_TD(F, i, k, sizes)
                r = matrix_mult_TD(F, k + 1, j, sizes)
                F[i][j] = min(F[i-1][j], l + r + sizes[i - 1] * sizes[j] * sizes[k])
            return F[i][j]


if __name__ == '__main__':
    n = int(input())
    matrix_sizes = []
    for _ in range(n):
        matrix_sizes.extend(map(int, input().split()))

    if not check_if_matrix_sizes_consistent(matrix_sizes):
        print('Sizes are inconsistent!')
    else:
        F = [[None for j in range(len(matrix_sizes))] for i in range(len(matrix_sizes))]
        matrix_mult_TD(F, 1, len(F[0]) - 1, matrix_sizes)
        print(F)
