# Solution of placing parenthesis problem using Dynamic Programming, Bottom Up approach
# (minimization the number of multiplication operations by properly parenthesis placement)

"""
==============
Test input #1:
4
50 20
20 1
1 10
10 100

Desired output:
7000
==============

==============
Test input #2:
3
1 2
2 3
3 4

Desired output:
18
==============
"""
from typing import List
from math import inf


def check_if_matrix_sizes_consistent(sizes: List[int]) -> bool:
    for i in range(1, len(sizes) - 2, 2):
        if sizes[i] != sizes[i + 1]:
            return False
    return True


# get the minimum number of multiplication operations needed to multiply matrices Ai x Ai+1 x ... x Aj,
# that have the corresponding dimensions specified by array a:
# for example: a = [2,   3,   7,   5,   20], n+1 numbers specifying the sizes of corresponding matrices
#                 A2x3 B3x7 C7x5 D5x20,      n matrices
def mult_DP_Bottom_Up(a: List[int]) -> int:
    N = len(a)  # the number of elements in a[], equals to n+1, where n - the number of matrices to be multiplied
    # initialize dp table: elements on the main diagonal = 0 because it corresponds to single matrix, i.e. i = j
    dp = [[inf if i != j else 0 for j in range(N)] for i in range(N)]

    for L in range(2, N):  # L is the length of current matrix subsequence to be multiplied, L = 2, 3, ..., N-1
        for i in range(1, N-L+1):
            j = i + L - 1
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + a[i-1]*a[j]*a[k])
    return dp[1][N-1]


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

        ans = mult_DP_Bottom_Up(a)
        print(f'Min number of multiplication operations needed to multiply matrices: {ans} operations')
