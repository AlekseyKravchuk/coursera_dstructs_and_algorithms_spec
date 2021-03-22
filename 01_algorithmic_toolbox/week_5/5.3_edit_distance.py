def delta(ch1, ch2):
    return int(ch1 != ch2)


# allows to restore optimal solution (output one of the optimal alignment)
def output_alignment(dp_table):
    pass


def edit_dist(s1, s2):
    # m,n: number of rows and columns in DP table respectively
    # there are one more row and column needed to store count=0 for empty string in the beginning of the words s1 and s2
    m, n = (len(s1) + 1, len(s2) + 1)

    # allocate memory for empty DP table
    F = [[None]*n for _ in range(m)]

    # initialize first column (with index 0)
    for i in range(m):
        F[i][0] = i

    # initialize first row (with index 0)
    for j in range(n):
        F[0][j] = j

    for i, ch1 in enumerate(s1, start=1):
        for j, ch2 in enumerate(s2, start=1):
            insertion = 1 + F[i][j - 1]
            subs_or_matching = F[i - 1][j - 1] + delta(ch1, ch2)
            deletion = 1 + F[i - 1][j]
            F[i][j] = min(insertion, subs_or_matching, deletion)
    return F[-1][-1]


# edit_dist_improved(a, b) needs only 2 rows from the whole DP table used in ordinary edit_dist(a, b) function
# !!! This function doesn't allow to restore solution (ways to achieve optimal alignment)
def edit_dist_improved(s1, s2):
    n = len(s2)  # n: number of columns

    # initialize the first row
    prev = list(range(n+1))  # we need one more column to store count=0 for empty string in the beginning of the word

    for i, ch1 in enumerate(s1, start=1):
        curr = [i]
        for j, ch2 in enumerate(s2, start=1):
            insertion = 1 + curr[-1]
            subs_or_matching = prev[j - 1] + delta(ch1, ch2)
            deletion = 1 + prev[j]

            curr.append(min(insertion, subs_or_matching, deletion))
        prev = curr

    return prev[-1]


if __name__ == '__main__':
    s1 = input()
    s2 = input()
    print(edit_dist(s1, s2))
    # print(edit_dist_improved(s1, s2))
