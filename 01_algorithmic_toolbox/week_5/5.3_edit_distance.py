from collections import deque


# returns 0 if ch1 == ch2, otherwise 1 (ch1 != ch2)
def delta(ch1, ch2):
    return int(ch1 != ch2)


# allows to restore optimal solution (output one of the optimal alignment)
def print_alignment(F, s1, s2):  # F is DP table, 2d array
    a1 = deque()
    a2 = deque()

    i, j = len(F) - 1, len(F[0]) - 1
    while F[i][j] != 0:
        # the last operation was INSERTION:
        if F[i][j] == F[i][j-1] + 1:
            a1.appendleft('-')
            a2.appendleft(s2[j-1])
            j -= 1
        # the last operation was DELETION
        elif F[i][j] == F[i-1][j] + 1:
            a1.appendleft(s1[i-1])
            a2.appendleft('-')
            i -= 1
        # the last operation was SUBSTITUTION (mismatch) or MATCH
        elif F[i][j] == F[i-1][j-1] + 1:
            a1.appendleft(s1[i-1].capitalize())
            a2.appendleft(s2[j-1].capitalize())
            i -= 1
            j -= 1
        # the last operation was MATCH
        elif F[i][j] == F[i - 1][j - 1]:
            a1.appendleft(s1[i-1])
            a2.appendleft(s2[j-1])
            i -= 1
            j -= 1
    for elm in a1:
        print(f' {elm} ', end='')
    print()
    for elm in a2:
        print(f' {elm} ', end='')
    print()


def edit_dist(s1, s2):
    # m,n: number of rows and columns in DP table respectively
    m, n = (len(s1), len(s2))

    # allocate memory for empty DP table
    # there are one more row and column needed to store count=0 for empty string in the beginning of the words s1 and s2
    F = [[None]*(n+1) for _ in range(m+1)]

    # initialize first column (j = 0) of DP table
    # edit distance between string of length 'i' and emtpy string
    for i in range(m+1):
        F[i][0] = i

    # initialize first row (i = 0) of DP table
    # edit distance between emtpy string and string of length 'j'
    for j in range(n+1):
        F[0][j] = j

    for i, ch1 in enumerate(s1, start=1):
        for j, ch2 in enumerate(s2, start=1):
            insertion = 1 + F[i][j - 1]
            subs_or_matching = F[i - 1][j - 1] + delta(ch1, ch2)
            deletion = 1 + F[i - 1][j]
            F[i][j] = min(insertion, subs_or_matching, deletion)
    return F


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
    dp_table = edit_dist(s1, s2)
    print(dp_table[-1][-1])
    print('Optimal alignment:')
    print_alignment(dp_table, s1, s2)

    # print(edit_dist_improved(s1, s2))
