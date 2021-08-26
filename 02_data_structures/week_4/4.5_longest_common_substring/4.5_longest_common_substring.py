from sys import stdin
from collections import namedtuple

Query = namedtuple('Query', ['s1', 's2'])

x = 29
p1 = 1000000007
p2 = 1000000009

# the number of buckets, it should be enough to store all substring hashes with reasonable load factor
# M = 100003
M = 50


def get_substr_hashes(s, win_len, p):
    L = len(s)
    coeffs = list(map(ord, s))
    h = [None] * M

    # precomputed values of x^(str_len-1) by given modulo
    mult = pow(x, win_len - 1, p)

    # Calculate the hash value of first window, w
    w = 0
    for i, _ in enumerate(coeffs):
        w = (x * w + coeffs[i]) % p
    # h[w % M] = (start_pos_of_substring, its_lenght)
    h[w % M] = (0, win_len)

    # Calculate hashes for all substrings of length=roll_hash_win_len of a given string
    for i in range(1, L - win_len + 1):
        next_idx = i + win_len - 1
        w = ((w - mult * coeffs[i - 1]) * x + coeffs[next_idx]) % p
        h[w % M] = (i, win_len)
    return h


def get_common_substring_info(hash_table, s2, ss_len, _modulo):
    L = len(s2)
    coeffs = list(map(ord, s2))

    # precomputed values of x^(str_len-1) by given modulo
    mult = pow(x, ss_len - 1, _modulo)

    # Calculate the hash value of first window, w
    w = 0
    for i, _ in enumerate(coeffs):
        w = (x * w + coeffs[i]) % _modulo
    h = w % M  # 'h' the hash value, corresponds to bucket index in hash table
    if hash_table[h] is not None:
        return hash_table[h][0], 0, ss_len

    # Calculate hashes of subsequent substrings of 'ss_len' length in string 's2' using rolling hash
    for i in range(1, L - ss_len + 1):
        next_char_idx = i + ss_len - 1
        w = ((w - mult * coeffs[i - 1]) * x + coeffs[next_char_idx]) % _modulo
        h = w % M  # 'h' the hash value, corresponds to bucket index in hash table
        if hash_table[h] is not None:
            return hash_table[h][0], i, ss_len
    # if we reach this place then there is no common substring of length ss_len
    return None


def search_LCS(s1, s2):
    if len(s1) <= len(s2):
        direct_order = True
    else:
        direct_order = False
        s1, s2 = s2, s1

    sz = len(s1)

    l, h = 1, sz
    a = list(range(1, sz + 1))  # array to hold all possible lengths of LCS
    while l != h:
        mid = l + (h - l) // 2

        # a[mid] is current length to be checked
        ht1 = get_substr_hashes(s1, a[mid], p1)
        ht2 = get_substr_hashes(s1, a[mid], p2)

        # tuples have following spec: (start_index_in_s1, start_index_in_s2, ss_len)
        tup1 = get_common_substring_info(ht1, s2, a[mid], p1)
        tup2 = get_common_substring_info(ht2, s2, a[mid], p2)
        if tup1 is not None and tup2 is not None:
            if tup1 == tup2:  # common substring of length 'a[mid]' is found
                l = mid + 1
            else:  # tup1 != tup2
                print(f'Hash collision:')
                print(f'\ts1 = {s1}, s2 = {s2}')
                print(f'\tsubstr in s1 = {s1[tup1[0]:tup1[0]+tup1[2]-1]}, it\'s start 0-based index in s1: {tup1[0]}')
                print(f'\tsubstr in s2 = {s2[tup2[0]:tup2[0]+tup2[2]-1]}, it\'s start 0-based index in s1: {tup1[0]}')
                l = mid + 1
        else:
            h = mid - 1

    # if we reach there than l == r and tup1 holds info about LCS
    if direct_order:
        print(*tup1)
    else:
        print(tup1[1], tup1[0], tup1[2])


if __name__ == '__main__':
    for line in stdin.readlines():
        s1, s2 = line.split()
        search_LCS(s1, s2)
