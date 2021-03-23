from math import inf
from collections import deque


def restore_solution(A, F, prev):
    max_F = max(F)
    max_F_indices = [i for i, x in enumerate(F) if x == max_F]

    j = max_F_indices[0]  # j is index of max value in array F
    solution = deque()
    while j > 0:
        solution.appendleft(j)
        j = prev[j]

    return max_F, solution


def get_LIS(A):
    F = [1 for _ in range(len(A))]  # because each standalone element represents a sequence with length = 1
    prev = [-inf for _ in range(len(A))]

    for i in range(len(A)):
        for j in range(i):
            if A[j] < A[i] and (F[j] + 1) > F[i]:
                F[i] = 1 + F[j]
                prev[i] = j
    return restore_solution(A, F, prev)


if __name__ == '__main__':
    # A = [7, 2, 1, 3, 8, 4, 9, 1, 2, 6, 5, 9, 3, 8, 1]
    A = [7, 2, 1, 3, 8, 4, 9, 1, 2, 6, 5, 9, 3, 8, 1]
    len_of_LIS, LIS = get_LIS(A)
    print(f'len of LIS: {len_of_LIS}')
    print(f'indices of LIS: {LIS}')
    for i in LIS:
        print(A[i], end=' ')
