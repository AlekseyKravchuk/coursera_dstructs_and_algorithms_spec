# Optimization of inefficient brute force (recursive) solution of placing parenthesis problem using Dynamic Programming,
# Top to Down DP approach
# (minimization the number of multiplication operations by properly parenthesis placement)

"""
Test input:
4
50 20
20 1
1 10
10 100

Desired output:
7000
"""
from typing import List
from math import inf

N = 100  # maximum size of 2-dimensional DP table in each dimension
dp_table = [[-1 for _ in range(N)] for _ in range(N)]


def check_if_matrix_sizes_consistent(sizes: List[int]) -> bool:
    for i in range(1, len(sizes) - 2, 2):
        if sizes[i] != sizes[i + 1]:
            return False
    return True


# get the minimum number of multiplication operations needed to multiply matrices Ai x Ai+1 x ... x Aj
# that have the corresponding dimensions specified by array a:
# for example: a = [2,   3,   7,   5,   20], n+1 numbers
#                 A2x3 B3x7 C7x5 D5x20, n matrices
def mult_DP_TD(a: List[int], i, j) -> int:
    # Base case
    if i == j:
        dp_table[i][j] = 0
        return 0

    # Use memoization (for overlapping subproblems)
    if dp_table[i][j] != -1:
        return dp_table[i][j]

    ans = inf
    for k in range(i, j):
        # mult_recursive(a, i, k)   - multiplication operations needed to get intermediate matrix in LEFT subtree
        # mult_recursive(a, k+1, j) - multiplication operations needed to get intermediate matrix in RIGHT subtree
        # a[i-1] * a[j] * a[k]      - number of operation needed to multiply matrices in LEFT and RIGHT subtrees
        tmp = mult_DP_TD(a, i, k) + mult_DP_TD(a, k + 1, j) + (a[i - 1] * a[j] * a[k])
        ans = tmp if tmp < ans else ans
    dp_table[i][j] = ans
    return ans


if __name__ == '__main__':
    n = int(input())  # number of matrices to multiply
    a = []  # matrix_sizes
    for _ in range(n):
        a.extend(map(int, input().split()))

    if not check_if_matrix_sizes_consistent(a):
        print('Matrix sizes are inconsistent!')
    else:
        # simplify the form or array representing sizes of given matrices
        # for test input: a=[50, 20, 20, 1, 1, 10, 10, 100] -> a=[50, 20, 1, 10, 100]
        a = [elm for i, elm in enumerate(a) if i == 0 or i % 2]

        ans = mult_DP_TD(a, 1, n)
        print(f'Min number of multiplication operations needed to multiply matrices: {dp_table[n][n]} operations')
