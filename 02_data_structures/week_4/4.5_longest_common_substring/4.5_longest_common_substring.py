# h1[i] = H(s[0]s[1]...,s[i-1]), h1[0] = 0 by default
def precompute_suffixes(s):
    L = len(s)
    x = 29
    m1 = 10 ** 9 + 7
    m2 = 10 ** 9 + 9
    h1, h2 = [None]*(L+1), [None]*(L+1)
    h1[0], h2[0] = 0, 0

    for i in range(1, L + 1):
        h1[i] = (x * h1[i - 1] + ord(s[i - 1])) % m1
        h2[i] = (x * h2[i - 1] + ord(s[i - 1])) % m2
    return h1, h2


def get_substrings_hashes(s):
    i = 0  # start index of window
    j = 0  # end index of window
    x = 29  # nearest prime number to 26, the number of lower case latin letters
    L = len(s)

    # may be set m = 1000033 ???
    m1 = 10 ** 9 + 7
    m2 = 10 ** 9 + 9

    pass


if __name__ == '__main__':
    pass
