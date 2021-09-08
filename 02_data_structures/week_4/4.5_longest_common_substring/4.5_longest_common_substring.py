from collections import namedtuple

Query = namedtuple('Query', ['s1', 's2'])

x = 29
p1 = 1000000000039
p2 = 1000000000061


# calculates hashes for all possible substrings of length 'win_len' of a given string 's' by given 'modulo'
def get_substr_hashes(s, win_len, p):
    L = len(s)
    coeffs = list(map(ord, s))
    d = dict()

    # precomputed values of x^(str_len-1) by given modulo
    mult = pow(x, win_len - 1, p)

    # Calculate the hash value of first window, w
    w = 0
    for i in range(win_len):
        w = (x * w + coeffs[i]) % p

    # d[w] = (start_pos_of_substring, its_lenght)
    d[w] = (0, win_len)

    # Calculate hashes for all substrings of length=roll_hash_win_len of a given string
    for i in range(1, L - win_len + 1):
        next_idx = i + win_len - 1
        w = ((w - mult * coeffs[i - 1]) * x + coeffs[next_idx]) % p
        d[w] = (i, win_len)
    return d


def get_LCS_positions(s2, d1, d2, ss_len, p1, p2):
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
    if w1 in d1 and w2 in d2:
        if d1[w1] == d2[w2]:
            # return (starting_pos_in_s1, starting_pos_in_s2, substring_len)
            return d1[w1][0], 0, ss_len
        else:
            return None

    # Calculate hashes of substrings of 'ss_len' length in string 's2' using rolling hash for 2 different modules
    for i in range(1, L - ss_len + 1):
        last_after_win_end = i + ss_len - 1
        w1 = ((w1 - coeffs[i - 1] * mult1) * x + coeffs[last_after_win_end]) % p1
        w2 = ((w2 - coeffs[i - 1] * mult2) * x + coeffs[last_after_win_end]) % p2
        if w1 in d1 and w2 in d2:
            if d1[w1] == d2[w2]:
                # return (starting_pos_in_s1, starting_pos_in_s2, substring_len)
                return d1[w1][0], i, ss_len
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
    while low <= high:
        mid = low + (high - low) // 2

        # d1 and d2 are dictionaries: {'substring_hash':(start_pos_in_s2, substring_length)}
        # lengths[mid] is current length to be checked for LCS
        d1 = get_substr_hashes(s1, lengths[mid], p1)
        d2 = get_substr_hashes(s1, lengths[mid], p2)

        # 'lcs' tuple has the following spec: (start_index_in_s1, start_index_in_s2, substring_len)
        lcs = get_LCS_positions(s2, d1, d2, lengths[mid], p1, p2)
        if lcs is not None:
            prev_best_lcs = lcs
            low = mid + 1
        else:
            high = mid - 1

    if lcs is not None:
        if direct_order:
            print(*lcs)
        else:
            print(lcs[1], lcs[0], lcs[2])
    else:  # lcs is None
        # check if there is prev_best_lcs
        if prev_best_lcs is not None:
            if direct_order:
                print(*prev_best_lcs)
            else:
                print(prev_best_lcs[1], prev_best_lcs[0], prev_best_lcs[2])
        else:  # prev_best_lcs is also None
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
