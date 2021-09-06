from sys import exit
from collections import namedtuple
from math import ceil

Query = namedtuple('Query', ['s1', 's2'])

x = 35
# p1 = 1000000007
# p2 = 1000000009

# p1 = 10007
# p2 = 701

p1 = 1000000000039
p2 = 1000000000061

# the number of buckets, it should be enough to store all substring hashes with reasonable load factor
M = 100003
# M = 50


def get_substr_hashes(s, win_len, modulo):
    L = len(s)
    coeffs = list(map(ord, s))
    h = [None] * M

    # precomputed values of x^(str_len-1) by given modulo
    mult = pow(x, win_len - 1, modulo)

    # Calculate the hash value of first window, w
    w = 0
    for i in range(win_len):
        w = (x * w + coeffs[i]) % modulo
    # h[w % M] = (start_pos_of_substring, its_lenght)
    h[w % M] = (0, win_len)

    # Calculate hashes for all substrings of length=roll_hash_win_len of a given string
    for i in range(1, L - win_len + 1):
        next_idx = i + win_len - 1
        w = ((w - mult * coeffs[i - 1]) * x + coeffs[next_idx]) % modulo
        h[w % M] = (i, win_len)
    return h


def get_LCS_positions(s1, s2, ht1, ht2, ss_len, p1, p2):
    L = len(s2)
    coeffs = list(map(ord, s2))

    # precomputed values of x^(str_len-1) by given modules
    mult1 = pow(x, ss_len - 1, p1)
    mult2 = pow(x, ss_len - 1, p2)

    w1, w2 = 0, 0
    # Calculate the hash value of first window
    for i in range(ss_len):
        w1 = (x * w1 + coeffs[i]) % p1
        w2 = (x * w2 + coeffs[i]) % p2
    hash1 = w1 % M  # 'hash1' the hash value, corresponds to bucket index in hash table ht1
    hash2 = w2 % M  # 'hash2' the hash value, corresponds to bucket index in hash table ht2
    if ht1[hash1] is not None and ht2[hash2] is not None:
        if ht1[hash1] == ht2[hash2]:
            # return (starting_pos_in_s1, starting_pos_in_s2, substring_len)
            return ht1[hash1][0], 0, ss_len
        else:
            exit(f"Collision was found: s1 = {s1}, s2 = {s2}")

    # Calculate hashes of substrings of 'ss_len' length in string 's2' using rolling hash for 2 different modules
    for i in range(1, L - ss_len + 1):
        last_after_win_end = i + ss_len - 1
        w1 = ((w1 - coeffs[i - 1] * mult1)*x + coeffs[last_after_win_end]) % p1
        w2 = ((w2 - coeffs[i - 1] * mult2)*x + coeffs[last_after_win_end]) % p2
        hash1 = w1 % M  # 'hash1' the hash value, corresponds to bucket index in hash table
        hash2 = w2 % M  # 'hash1' the hash value, corresponds to bucket index in hash table
        if ht1[hash1] is not None and ht2[hash2] is not None:
            if ht1[hash1] == ht2[hash2]:
                # return (starting_pos_in_s1, starting_pos_in_s2, substring_len)
                return ht1[hash1][0], i, ss_len
            else:
                exit(f"Collision was found: s1 = {s1}, s2 = {s2}")
    # if we reach this place then there is no common substring of length ss_len
    return None


def search_LCS(s1, s2):
    if len(s1) <= len(s2):
        direct_order = True
    else:
        direct_order = False
        s1, s2 = s2, s1

    sz = len(s1)

    low, high = 0, sz - 1

    # array to hold all possible lengths of LCS
    lengths = list(range(1, sz + 1))

    lcs = None
    prev_best_lcs = None
    while low != high:
        mid = low + (high - low) // 2
        # mid = low + ceil((high - low)/2)

        # lengths[mid] is current length to be checked
        ht1 = get_substr_hashes(s1, lengths[mid], p1)
        ht2 = get_substr_hashes(s1, lengths[mid], p2)

        # 'lcs' tuple has the following spec: (start_index_in_s1, start_index_in_s2, ss_len)
        lcs = get_LCS_positions(s1, s2, ht1, ht2, lengths[mid], p1, p2)
        if lcs is not None:
            prev_best_lcs = lcs
            low = mid + 1
        else:
            high = mid - 1
            if high < 0:
                break
            if high < low:
                lcs = prev_best_lcs
                break

    # if we reach there than low == r, so we found LCS (or not found)
    if lcs is not None:
        if direct_order:
            print(*lcs)
        else:
            print(lcs[1], lcs[0], lcs[2])
    else:
        print(0, 0, 0)


if __name__ == '__main__':
    lines = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        lines.append(line)

    for line in lines:
        s1, s2 = line.split()
        search_LCS(s1, s2)
