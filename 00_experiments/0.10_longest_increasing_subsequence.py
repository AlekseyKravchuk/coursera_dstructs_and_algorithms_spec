###### calculate LIS (Longest Increasing Subsequence)
from collections import defaultdict


def get_LIS(G, d):
    if not G[-1]:
        d[len(G) - 1] = G[-1]
        return d

    d[len(G) - 1] = G[len(G) - 1]
    for index in G[len(G) - 1]:
        get_LIS(G[:index + 1], d)


def restore_LISes(A, F, G):
    LISes = []
    max_F = max(F)
    root_indices = [i for i, x in enumerate(F) if x == max_F]

    for index in root_indices:
        LISes.append(get_LIS(G[:index + 1], {-1: index}))
    print(LISes)

    return max_F, LISes


def LISBottomUP(A):
    F = [1 for _ in range(len(A))]
    G = [[] for _ in range(len(A))]

    # F[i] is the length of LIS ending in element A[i]
    for i in range(len(A)):
        for j in range(i):
            if A[j] < A[i]:
                if (F[j] + 1) == F[i]:
                    G[i].append(j)
                elif (F[j] + 1) > F[i]:
                    F[i] = 1 + F[j]
                    G[i] = [j]

    return restore_LISes(A, F, G)


if __name__ == '__main__':
    A = [7, 2, 1, 3, 8, 4, 9, 1, 2, 6, 5, 9, 3, 8, 1]
    max_val, LISes = LISBottomUP(A)
    print(f'Max length of LIS for a sequence {A} is {max_val}')
    print(f'LISes:')
    for LIS in LISes:
        print(f'\t{LIS}')
