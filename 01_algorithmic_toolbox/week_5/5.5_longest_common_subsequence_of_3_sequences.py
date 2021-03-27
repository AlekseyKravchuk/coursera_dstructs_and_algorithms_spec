# calculate DP table for longest common subsequence(LCS) of 3 sequences problem
def lcs(s1, s2, s3):
    n_layers, n_rows, n_cols = len(s1), len(s2), len(s3)
    F = [[[None for k in range(n_cols + 1)] for i in range(n_rows + 1)] for i in range(n_layers + 1)]

    # fill in top surface of cube with zeros
    for i in range(n_layers + 1):
        for k in range(n_cols + 1):
            F[i][0][k] = 0

    # fill in front surface of cube with zeros
    for j in range(n_rows + 1):
        for k in range(n_cols + 1):
            F[0][j][k] = 0

    # fill in left surface of cube with zeros
    for i in range(n_layers + 1):
        for j in range(n_rows + 1):
            F[i][j][0] = 0

    for j in range(n_rows + 1):
        F[0][j][0] = 0
    for k in range(n_cols + 1):
        F[0][0][k] = 0

    for i, ch1 in enumerate(s1, start=1):
        for j, ch2 in enumerate(s2, start=1):
            for k, ch3 in enumerate(s3, start=1):
                if ch1 == ch2 == ch3:
                    F[i][j][k] = 1 + F[i - 1][j - 1][k - 1]
                else:
                    F[i][j][k] = max(F[i][j][k - 1], F[i][j - 1][k], F[i - 1][j][k])
    return F


if __name__ == '__main__':
    m = int(input())
    s1 = input().split()
    assert m == len(s1), 'Number of characters in string and its length does not match'
    if not s1[0].isalpha():
        s1 = list(map(int, s1))

    n = int(input())
    s2 = input().split()
    assert n == len(s2), 'Number of characters in string and its length does not match'
    if not s2[0].isalpha():
        s2 = list(map(int, s2))

    k = int(input())
    s3 = input().split()
    assert k == len(s3), 'Number of characters in string and its length does not match'
    if not s3[0].isalpha():
        s3 = list(map(int, s3))

    dp_table = lcs(s1, s2, s3)
    print(dp_table[-1][-1][-1])
