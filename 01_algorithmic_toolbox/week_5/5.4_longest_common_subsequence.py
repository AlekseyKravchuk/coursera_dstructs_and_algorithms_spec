
# TO DO: !!!!!!!!!!!!!!!!! NOT working
# calculate DP table for longest common subsequence problem
# each cell of DP table contains (F, argmax)
def lcs_with_argmax_storage(s1, s2):
    m, n = len(s1), len(s2)
    F = [[[None, None] for columns in range(n + 1)] for rows in range(m + 1)]
    for i in range(m + 1):
        F[i][0][0] = 0, None
    for j in range(n + 1):
        F[0][j][0] = 0
    for i, ch1 in enumerate(s1, start=1):
        for j, ch2 in enumerate(s2, start=1):
            if ch1 == ch2:
                F[i][j][0] = 1 + F[i-1][j-1][0]
                F[i][j][1] = [i-1, j-1]
            else:
                F[i][j][0] = max(F[i][j-1][0], F[i-1][j][0])
                F[i][j][1] = [i, j-1] if F[i][j-1][0] > F[i-1][j][0] else [i-1, j]
    return F


# calculate DP table for longest common subsequence problem
def lcs(s1, s2):
    m, n = len(s1), len(s2)
    F = [[None] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        F[i][0] = 0
    for j in range(n + 1):
        F[0][j] = 0
    for i, ch1 in enumerate(s1, start=1):
        for j, ch2 in enumerate(s2, start=1):
            if ch1 == ch2:
                F[i][j] = 1 + F[i-1][j-1]
            else:
                F[i][j] = max(F[i][j-1], F[i-1][j])
    return F


if __name__ == '__main__':
    m = int(input())
    s1 = list(map(int, input().split()))
    n = int(input())
    s2 = list(map(int, input().split()))

    # dp_table = lcs(s1, s2)
    # print(dp_table[-1][-1])

    dp_table = lcs_with_argmax_storage(s1, s2)
    print(dp_table)
