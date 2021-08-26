from collections import deque


class RabinKarp:
    # q = 1000000007: prime number big enough to minimize collisions while hashing and small enough to fit into int_64
    # x = 59: the nearest prime number to 52 as the Latin alphabet consists of 52 letters
    def __init__(self, pattern, text, x=59, q=1000000007):
        self.p = pattern
        self.t = text

        self.M = len(pattern)
        self.x = x
        self.q = q
        self.ms_term = 1  # holder for most significant term in polynomial

        # start index of current hash window
        self.window_start = 0

        # end index of current hash window
        self.window_end = self.window_start + len(self.p) - 1

        self.window_hash = None
        self.positions = []  # positions of pattern (self.p) occurrences within the text self.t

        # precomputed value for the most significant term x^(M-1)mod_q
        for i in range(self.M - 1):
            self.ms_term = (self.ms_term * self.x) % self.q

    def get_occurrences(self):
        return self.positions

    # calculates h = (ord(s[0])*x^(m-1) + ord(s[1])*x^(m-2) + ... + ord(s[m-1])*x^0)mod_q using Horner's rule
    def str_hash(self, s):
        coeffs = list(map(ord, s))  # coefficients of polynomial of degree (self.M - 1)
        h = 0

        for i, _ in enumerate(coeffs):
            h = (h * self.x + coeffs[i]) % self.q
        return h

    def update_window(self):
        self.window_start += 1
        self.window_end += 1

    def move_hash_window(self):
        if self.window_start < len(self.t) - len(self.p):
            char2remove = ord(self.t[self.window_start]) * self.ms_term
            char2add = ord(self.t[self.window_end + 1])
            self.window_hash = ((self.window_hash - char2remove) * self.x + char2add) % self.q
        self.update_window()

    # as it turned out it is BAD practice to implement in Python your own string comparison function
    # !!!! always use '==' and corresponding slicing
    # def is_match(self):
    #     for i, _ in enumerate(self.p):
    #         if self.t[self.window_start + i] != self.p[i]:
    #             return False
    #     return True

    def run(self):
        pattern_hash = self.str_hash(self.p)
        self.window_hash = self.str_hash(self.t[0:len(self.p)])

        for _ in range(len(self.t) - len(self.p) + 1):
            if self.window_hash == pattern_hash:
                # String comparison below leads to time limit exceeded: Time used: 8.99/4.50. Who would ever suppose!!!
                # if self.is_match():  # VERY VERY BAD !!!
                # Check using slices and '==' works PERFECTRLY: Max time used: 0.74/4.50
                if self.t[self.window_start:self.window_end + 1] == self.p:
                    self.positions.append(self.window_start)
            self.move_hash_window()


if __name__ == '__main__':
    pattern = input().strip()
    text = input().strip()

    rk = RabinKarp(pattern, text)
    rk.run()
    print(*rk.get_occurrences())
