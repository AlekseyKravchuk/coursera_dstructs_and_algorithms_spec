from copy import deepcopy
from collections import namedtuple

# k: maximum allowed number of mismatches;
# s: string to search in;
# p: pattern to search for in string 's' (with at most 'k' mismatches)
Request = namedtuple('Request', ['k', 's', 'p'])

x = 59
q1 = 10 ** 9 + 7
q2 = 10 ** 9 + 9


def get_requests():
    requests = []
    while True:
        try:
            line = input()
            k, s, p = line.split()
        except EOFError:
            break
        requests.append(Request(int(k), s, p))
    return requests


# precompute hashes for all prefixes in string 's'
def get_suff_hashes(s):
    # h[prefix_length] is the hash of string prefix of length 'prefix_length'
    # or it can be thought such as h[3] is a hash for substring s1s2s3 with 1-based index numeration
    # h[0] = 0 by default
    # for example:
    # s = 'trololo', len(s)=7 =>
    # we should calculate hashes for 7 prefixes: 1)'t', 2)'tr', 3)'tro', 4)'trol', 5)'trolo', 6)'trolol', 7)'trololo'
    h1 = [None]*(len(s)+1)
    h2 = deepcopy(h1)
    h1[0] = h2[0] = 0

    char_codes = [ord(ch) for ch in s]
    # calculating hashes using Horner's rule
    for i, ch_code in enumerate(char_codes, start=1):
        h1[i] = (x * h1[i-1] + ch_code) % q1
        h2[i] = (x * h2[i-1] + ch_code) % q2
    return h1, h2


# get hash of substring specified by 0-based 'left' and 'right'(INCLUSIVE) indices
# 'h': array of precomputed hashes, h[0] = 0
def get_hashes(h1, h2, left, right):
    win_len = right-left+1
    hash1 = (h1[right+1] - pow(x, win_len, q1) * h1[left]) % q1
    hash2 = (h2[right+1] - pow(x, win_len, q2) * h2[left]) % q2
    return hash1, hash2


# hash-based string comparison
def is_equal(s_h1, s_h2, p_h1, p_h2, left, right):
    s_hash_q1, s_hash_q2 = get_hashes(s_h1, s_h2, left, right)
    p_hash_q1, p_hash_q2 = get_hashes(p_h1, p_h2, left, right)


def get_mid(left, right):
    return left + (right - left) // 2

# k: maximum number of mismatches
# s: string to search within
# p: pattern, string to search for in string 's' with at most 'k' mismatches
def handle_request(k, s, p):

    # nested function; counts mismatches using binary search algorithm and hashing
    def count_mismatches(i=0, left=0, right=len(p)-1):
        mismatches = 0
        p_left = left-i
        p_right = right-i

        # BASE CASE
        # TODO
        if left > right or mismatches > k or hash(overlapped_part_in_s) == hash(overlapped_part_in_p):
            hash(overlapped_part_in_s) = hash(s[left]s[left+1]...s[right]) - pow(x, right-left+1, q) * hash(s[left]s[left+1]...s[left-1])
            return mismatches

        s_mid, p_mid = get_mid(left, right), get_mid(left-i, right-i)

        if s[s_mid] != p[p_mid]:
            mismatches += 1

        # TODO!!!!!!
        if get_hashes(get_suff_hashes(s[s_left:s_right + 1])) != get_hashes(
                get_suff_hashes(p[s_left:s_right + 1])):
            pass



if __name__ == '__main__':
    requests = get_requests()
    for r in requests:
        print(r)
