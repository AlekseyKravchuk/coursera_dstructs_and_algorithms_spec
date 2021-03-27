from collections import deque


# print one of the Longest Common Subsequences(LCSs) based on the given DP table and two strings
def print_one_of_LCSs(dp_table, s1, s2):
    q = deque()
    i, j = len(s1), len(s2)

    while dp_table[i][j] != 0:
        if s1[i-1] == s2[j-1]:
            q.appendleft(s1[i-1])
            i, j = i-1, j-1
        else:
            i, j = (i, j-1) if dp_table[i][j - 1] > dp_table[i - 1][j] else (i-1, j)
    print(f'One of the Longest Common Subsequences(LCSs):', end=' ')
    for ch in q:
        print(ch, end=' ')
    print()


# calculate DP table for longest common subsequence(LCS) of 2 sequences problem
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
                F[i][j] = 1 + F[i - 1][j - 1]
            else:
                F[i][j] = max(F[i][j - 1], F[i - 1][j])
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

    # Output for coursera assignment
    dp_table = lcs(s1, s2)
    print(dp_table[-1][-1])

    # Output to test restoring DP solution
    # dp_table = lcs(s1, s2)
    # print(f'The length of the Longest Common Subsequence equals to {dp_table[-1][-1]}')
    # print_one_of_LCSs(dp_table, s1, s2)

