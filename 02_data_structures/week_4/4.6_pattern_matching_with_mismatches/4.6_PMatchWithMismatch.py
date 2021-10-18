# python3

import sys
from collections import deque


def get_ht(s, q, x):
    ht = list([] for _ in range(len(s) + 1))
    ht[0] = 0
    for i in range(1, len(s) + 1):
        ht[i] = (ht[i-1] * x + ord(s[i-1])) % q
    return ht


def get_hash(ht, q, x, start, length):
    y = pow(x, length, q)
    hash_value = (ht[start + length] - y * ht[start]) % q
    return hash_value


def get_suffixes_htables(text, pattern):
    global m, x
    h1 = get_ht(text, m, x)
    h2 = get_ht(pattern, m, x)
    return h1, h2


def check(a_start, length, p_len, k):
    global m, h1, h2
    stack = deque()
    stack.append((a_start, 0, length, 1))
    stack.append((a_start+length, length, p_len-length, 1))
    count = 0
    temp = 2
    C = 0
    while stack:
        a, b, L, n = stack.popleft()
        u1 = get_hash(h1, m, x, a, L)
        v1 = get_hash(h2, m, x, b, L)
        if temp != n:
            count = C
        if u1 != v1:
            count += 1
            if L > 1:
                stack.append((a, b, L//2, n+1))
                stack.append((a + L//2, b + L//2, L - L//2, n+1))
            else:
                C += 1
        if count > k:
            return False
        temp = n
    if count > k:
        return False
    else:
        return True


def get_results(t, p, k):
    global h1, h2
    h1, h2 = get_suffixes_htables(t, p)
    pos = []
    for i in range(len(t) - len(p) + 1):
        if check(i, len(p) // 2, len(p), k):
            pos.append(i)
    return pos


m = 1000000007
x = 263

for line in sys.stdin.readlines():
    k, t, p = line.split()
    results = get_results(t, p, int(k))
    print(len(results), *results)
