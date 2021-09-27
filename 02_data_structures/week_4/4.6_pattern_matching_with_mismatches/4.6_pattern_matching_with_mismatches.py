from copy import deepcopy

x = 59
q = 10 ** 9 + 7


def my_readlines():
    lines = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        lines.append(line)
    return lines


def get_str_suffixes_hashes(s):
    # h[prefix_length] is the hash of string prefix of length 'prefix_length'
    # or it can be thought such as h[3] is a hash for substring s1s2s3 with 1-based index numeration
    # h[0] = 0 by default
    # for example:
    # s = 'trololo', len(s)=7 =>
    # we should calculate hashes for 7 prefixes: 1)'t', 2)'tr', 3)'tro', 4)'trol', 5)'trolo', 6)'trolol', 7)'trololo'
    h = [None] * (len(s) + 1)
    h[0] = 0

    char_codes = [ord(ch) for ch in s]
    # calculating hashes using Horner's rule
    for i, ch_code in enumerate(char_codes, start=1):
        h[i] = (x * h[i-1] + ch_code) % q
    return h


# get hash of substring specified by 'start' and 'end' 0-based indices INCLUSIVE
def get_hash(s_pref_hashes, start, end):
    return (s_pref_hashes[end+1] - pow(x, end-start+1, q) * s_pref_hashes[start]) % q


def check_window(s, p, k, start_index=0):
    countMismatch = 0
    left = start_index
    right = len(p) - 1
    middle = left + (right - left) // 2

    if s[middle] != p[middle]:
        countMismatch += 1

    if get_hash(get_str_suffixes_hashes(s[left:right+1])) != get_hash(get_str_suffixes_hashes(p[left:right+1]))


if __name__ == '__main__':
    lines = my_readlines()

    for line in lines:
        k, s1, s2 = line.split()
        k = int(k)
        print(f'k = {k}, s1 = {s1}, s2 = {s2}')
