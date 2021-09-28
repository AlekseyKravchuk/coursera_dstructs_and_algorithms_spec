from collections import namedtuple

Query = namedtuple('Query', ['a', 'b', 'l'])


# class SubstrEq (substring equality)
class SubstrEq:
    def __init__(self, m1=10 ** 9 + 7, m2=10 ** 9 + 9, x=53):
        self.s = input()
        self.L = len(self.s)
        n = int(input())
        self.queries = [Query(*map(int, input().split())) for _ in range(n)]
        assert n == len(self.queries)

        self.m1 = m1
        self.m2 = m2
        self.x = x

        # h1,h2 - arrays to store precomputed hashes for every string suffix
        self.h1 = [None] * (self.L + 1)
        self.h1[0] = 0
        self.h2 = [None] * (self.L + 1)
        self.h2[0] = 0

        self.results = []

    # h1[i] = H(s[0]s[1]...,s[i-1]), h1[0] = 0 by default
    def precompute_suffixes(self):
        for i in range(1, self.L + 1):
            self.h1[i] = (self.x * self.h1[i - 1] + ord(self.s[i-1])) % self.m1
            self.h2[i] = (self.x * self.h2[i - 1] + ord(self.s[i-1])) % self.m2

    def handle_query(self, q):
        mult_h1, mult_h2 = 1, 1  # precomputed values for x^(substring_len) by modulo self.m1 and self.m2 respectively:
        # BELOW, commented lines represent BAD APPROACH for Python, ALWAYS use pow(x,y,z)
        # for i in range(q.l):
        #     mult_h1 = (self.x * mult_h1) % self.m1
        #     mult_h2 = (self.x * mult_h2) % self.m2
        mult_h1 = pow(self.x, q.l, self.m1)
        mult_h2 = pow(self.x, q.l, self.m2)

        h_s1_mod_m1 = (self.h1[q.arr + q.l] - ((mult_h1 * self.h1[q.arr]) % self.m1)) % self.m1
        h_s2_mod_m1 = (self.h1[q.b + q.l] - ((mult_h1 * self.h1[q.b]) % self.m1)) % self.m1

        h_s1_mod_m2 = (self.h2[q.arr + q.l] - ((mult_h2 * self.h2[q.arr]) % self.m2)) % self.m2
        h_s2_mod_m2 = (self.h2[q.b + q.l] - ((mult_h2 * self.h2[q.b]) % self.m2)) % self.m2

        if h_s1_mod_m1 == h_s2_mod_m1 and h_s1_mod_m2 == h_s2_mod_m2:
            self.results.append('Yes')
        else:
            self.results.append('No')

    def process(self):
        self.precompute_suffixes()
        for _, q in enumerate(self.queries):
            self.handle_query(q)


if __name__ == '__main__':
    se = SubstrEq()
    se.process()
    for res in se.results:
        print(res)
