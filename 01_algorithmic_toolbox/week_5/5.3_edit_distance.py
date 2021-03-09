def delta(ch1, ch2):
    return int(ch1 != ch2)


def edit_dist(a, b):
    # m: number of rows in DP table
    # n: number of columns in DP table
    m, n = (len(a) + 1, len(b) + 1)
    F = [[None for _ in range(n)] for _ in range(m)]

    for i in range(m):
        F[i][0] = i
    for j in range(n):
        F[0][j] = j

    for i in range(1, m):
        for j in range(1, n):
            insertion = 1 + F[i][j - 1]
            subs_or_matching = F[i - 1][j - 1] + delta(a[i - 1], b[j - 1])
            deletion = 1 + F[i - 1][j]
            F[i][j] = min(insertion, subs_or_matching, deletion)
    return F[m - 1][n - 1]


if __name__ == '__main__':
    a = input()
    b = input()
    print(edit_dist(a, b))

