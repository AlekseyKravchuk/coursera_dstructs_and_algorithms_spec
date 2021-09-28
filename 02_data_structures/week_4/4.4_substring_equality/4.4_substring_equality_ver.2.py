from collections import namedtuple
from copy import deepcopy

Query = namedtuple('Query', ['a', 'b', 'len'])
x = 29
q1 = 10**9 + 7  # first modulo for calculating polynomial hashes
q2 = 10**9 + 9  # second modulo for calculating polynomial hashes


# precompute hashes for all prefixes in string 's'
def precompute_prefix_hashes(s):
    # h[prefix_length] is the hash of string prefix of length 'prefix_length'
    # h[0]
    # for example:
    # s = 'trololo', len(s)=7 =>
    # we should calculate hashes for 7 prefixes: 't', 'tr', 'tro', 'trol', 'trolo', 'trolol', 'trololo'
    h1 = [None]*(len(s)+1)
    h2 = deepcopy(h1)
    h1[0] = h2[0] = 0

    char_codes = [ord(ch) for ch in s]
    # calculating hashes using Horner's rule
    for i, ch_code in enumerate(char_codes, start=1):
        h1[i] = (x * h1[i-1] + ch_code) % q1
        h2[i] = (x * h2[i-1] + ch_code) % q2
    return h1, h2


def process_queries(s, queries):

    def handle_query():
        # calculate hashes for substring 's[a:a+l]'
        ss1_hash_q1 = (h1[q.arr + q.len] - mult1 * h1[q.arr]) % q1
        ss1_hash_q2 = (h2[q.arr + q.len] - mult2 * h2[q.arr]) % q2

        # calculate hashes for substring 's[b:b+l]'
        ss2_hash_q1 = (h1[q.b + q.len] - mult1 * h1[q.b]) % q1
        ss2_hash_q2 = (h2[q.b + q.len] - mult2 * h2[q.b]) % q2

        if ss1_hash_q1 == ss2_hash_q1 and ss1_hash_q2 == ss2_hash_q2:
            print('Yes')
        else:
            print('No')

    # h1, h2 are precomputed polynomial hash values for all string prefixes by 2 different modulo q1 and q2
    h1, h2 = precompute_prefix_hashes(s)
    for q in queries:
        # precompute value for 'x ** q.len' for each given length of substring
        mult1 = pow(x, q.len, q1)
        mult2 = pow(x, q.len, q2)
        handle_query()


if __name__ == '__main__':
    s = input()
    n = int(input())
    queries = [Query(*map(int, input().split())) for _ in range(n)]
    process_queries(s, queries)

