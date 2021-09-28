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
    for i, char_code in enumerate(char_codes, start=1):
        h[i] = (x * h[i-1] + char_code) % q
    return h


# get hash of substring specified by 0-based 'start' and 'end'(INCLUSIVE) indices
# 'h': array of precomputed hashes
def get_hash(h, start, end):
    return (h[end+1] - pow(x, end-start+1, q) * h[start]) % q


def get_middle(left, right):
    return left + (right - left) // 2


# адаптированный для решения задачи алгоритм bin_search
def check_window(s, p, k, win_start_idx=0):
    countMismatch = 0
    s_left, p_left = win_start_idx, 0
    s_right, p_right = s_left +len(p) - 1, len(p)-1
    s_middle, p_middle = get_middle(s_left, s_right), get_middle(p_left, p_right)

    if s[s_middle] != p[p_middle]:
        countMismatch += 1

    # TODO!!!!!!
    if get_hash(get_str_suffixes_hashes(s[s_left:s_right+1])) != get_hash(get_str_suffixes_hashes(p[s_left:s_right+1])):
        pass


if __name__ == '__main__':
    lines = my_readlines()

    for line in lines:
        k, s1, s2 = line.split()
        k = int(k)
        print(f'k = {k}, s1 = {s1}, s2 = {s2}')
