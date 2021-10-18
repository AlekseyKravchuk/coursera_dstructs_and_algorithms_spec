import random
from copy import deepcopy
from collections import namedtuple
import string

# k: maximum allowed number of mismatches;
# s: string to search in;
# p: pattern to search for in string 's' with at most 'k' mismatches
Request = namedtuple('Request', ['k', 's', 'p'])


def rand_str(str_len):
    # alphabet = string.ascii_lowercase
    # return ''.join(random.choice(alphabet) for _ in range(str_len))

    alphabet = 'abc'
    return ''.join(random.choices(alphabet, weights=[1, 1, 2], k=str_len))


def get_requests():
    requests = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        if line:
            k, s, p = line.split()
            requests.append(Request(int(k), s, p))
        else:
            break
    return requests


# class for Pattern Matching with Mismatches
class PMM:
    # x = 59
    # q1 = 10**9 + 7
    # q2 = 10**9 + 9
    x = 29
    q1 = 1000000000039
    q2 = 1000000000061

    def __init__(self, r: Request):
        self.k = r.k
        self.s = r.s
        self.p = r.p

        # placeholder for resulting array containing positions 'i' where 'p' occurs in 's' with at most 'k' mismatches
        self.result = []

        # We need to store precomputed hashes (given by 2 different modulo)
        # of all SUFFIXES in string 's' and in pattern 'p'; so 4 holders are needed
        # self.s_suff_q1[i] holds the hash of suffix of length 'i', so self.sh1[0] = 0
        self.s_suff_q1 = [0] * (len(self.s) + 1)
        self.s_suff_q2 = deepcopy(self.s_suff_q1)

        self.p_suff_q1 = [0] * (len(self.p) + 1)
        self.p_suff_q2 = deepcopy(self.p_suff_q1)

        # Additionally to prevent wasteful recurrent computations we need to create 2D-arrays
        # MxM (for string 's') and NxN (for pattern 'p') designed to store hashes of overlapping parts in 's' and in 'p'
        # specified by 'win_start' = i (offset in 's') and left and right positions.
        # So self.s_h_q1[i][j] correspond to hash of substring 's[i:j+1]' given by modulo PMM.q1
        M, N = len(self.s), len(self.p)
        self.sh_q1 = [[None for _ in range(M)] for _ in range(M)]
        self.sh_q2 = [[None for _ in range(M)] for _ in range(M)]
        self.ph_q1 = [[None for _ in range(N)] for _ in range(N)]
        self.ph_q2 = [[None for _ in range(N)] for _ in range(N)]

        # calculate hashes for all possible suffixes in string 's' and pattern 'p'
        self.fill_suff_hashes()
        # *********** END of __init__ ***********

    # calculate hashes of ALL suffixes in 'self.s' and 'self.p'
    # self.sh1[i] is hash for substring s[0]s[1]s[2]...s[i-1]
    # for example:
    # s = 'trololo', len(s)=7 =>
    # we should calculate hashes for 7 prefixes: 1)'t', 2)'tr', 3)'tro', 4)'trol', 5)'trolo', 6)'trolol', 7)'trololo'
    def fill_suff_hashes(self):
        s_codes = [ord(ch) for ch in self.s]
        p_codes = [ord(ch) for ch in self.p]

        # calculating hashes of all suffixes in 's' and in 'p' using Horner's rule by 2 different modules: PMM.q1,PMM.q2
        for i, ch_code in enumerate(s_codes, start=1):
            self.s_suff_q1[i] = (PMM.x * self.s_suff_q1[i - 1] + ch_code) % PMM.q1
            self.s_suff_q2[i] = (PMM.x * self.s_suff_q1[i - 1] + ch_code) % PMM.q2
        for j, ch_code in enumerate(p_codes, start=1):
            self.p_suff_q1[j] = (PMM.x * self.p_suff_q1[j - 1] + ch_code) % PMM.q1
            self.p_suff_q2[j] = (PMM.x * self.p_suff_q1[j - 1] + ch_code) % PMM.q2

    # check if current overlapped regions in string 'self.s' and in pattern 'self.p' are the same
    # overlapping region is specified by window start position 'i' and 0-based 'l' and 'r' (INCLUSIVE) indices
    # self.sh_q1[i][j] corresponds to hash of substring in 's': 's[left:right+1]' given by modulo PMM.q1
    # self.sh_q2[i][j] corresponds to hash of substring in 's': 's[left:right+1]' given by modulo PMM.q2 and so on
    def is_overlapped_parts_equal(self, i, l, r):
        y = r - l + 1
        p_l, p_r = l - i, r - i

        # there is no offset, so hash for substring is equal to hash of corresponding suffix
        if i == 0 and l == 0:
            if self.sh_q1[l][r] is None:
                self.sh_q1[l][r] = self.s_suff_q1[r + 1]
                self.sh_q2[l][r] = self.s_suff_q2[r + 1]
                self.ph_q1[p_l][p_r] = self.p_suff_q1[p_r + 1]
                self.ph_q2[p_l][p_r] = self.p_suff_q2[p_r + 1]
        else:
            if self.sh_q1[l][r] is None:
                self.sh_q1[l][r] = (self.s_suff_q1[r + 1] - pow(PMM.x, y, PMM.q1) * self.s_suff_q1[l]) % PMM.q1
                self.sh_q2[l][r] = (self.s_suff_q2[r + 1] - pow(PMM.x, y, PMM.q2) * self.s_suff_q2[l]) % PMM.q2

                self.ph_q1[p_l][p_r] = (self.p_suff_q1[p_r + 1] - pow(PMM.x, y, PMM.q1) * self.p_suff_q1[p_l]) % PMM.q1
                self.ph_q2[p_l][p_r] = (self.p_suff_q2[p_r + 1] - pow(PMM.x, y, PMM.q2) * self.p_suff_q2[p_l]) % PMM.q2

        if self.sh_q1[l][r] == self.ph_q1[p_l][p_r] and self.sh_q2[l][r] == self.ph_q2[p_l][p_r]:
            return True
        else:
            return False

    # count_mismatches() will be invoked recursively
    def count_mismatches(self, i, l, r):
        mismatches = 0
        # **** BASE CASE #1 ****
        if l > r:
            return 0

        # **** BASE CASE #2 ****:
        if l == r:
            if self.s[l] == self.p[l - i]:
                return 0
            else:
                return 1

        # **** BASE CASE #3 ****:
        flag = self.is_overlapped_parts_equal(i, l, r)
        if flag:
            return 0

        # **** BASE CASE #4 ****
        if mismatches > self.k:
            return

        mid = l + (r - l) // 2
        p_mid = mid - i if mid != 0 else mid
        if self.s[mid] != self.p[p_mid]:
            mismatches += 1
            # CURRENTLY COMMENTED OUT
            # BASE CASE #5: the number of mismatches became one more than allowed 'k'
            # if mismatches > self.k:
            #     return mismatches

        mismatches += self.count_mismatches(i, l, mid - 1)
        # middle check to avoid unnecessary checking the right part of overlapping
        # if mismatches > self.k:
        #     return mismatches
        mismatches += self.count_mismatches(i, mid + 1, r)
        return mismatches

    def handle_request_debug(self, out_file='./tests/02.out'):
        from contextlib import redirect_stdout

        # CORNER CASE:
        if self.k >= len(self.p):
            with open(out_file, 'a') as f:
                with redirect_stdout(f):
                    print(len(self.s) - len(self.p) + 1, end=' ')
                    for num in range(len(self.s) - len(self.p) + 1):
                        print(num, end=' ')
                    print()
        else:
            for i in range(len(self.s) - len(self.p) + 1):
                n_mismatches = self.count_mismatches(i, i, i + len(self.p) - 1)
                if n_mismatches <= self.k:
                    self.result.append(i)

            with open(out_file, 'a') as f:
                with redirect_stdout(f):
                    if not self.result:
                        print(0)
                    else:
                        print(len(self.result), *self.result)

    def handle_request(self):
        windows_num = len(self.s) - len(self.p) + 1
        # CORNER CASE:
        if self.k >= len(self.p):
            self.result.append(windows_num)
            for pos in range(windows_num):
                self.result.append(pos)
        else:
            for i in range(windows_num):
                n_mismatches = self.count_mismatches(i, i, i + len(self.p) - 1)
                if n_mismatches <= self.k:
                    self.result.append(i)

            if not self.result:
                self.result.append(0)
            else:
                self.result = [len(self.result)] + self.result

    def naive_handle_request(self):
        indices = []
        for win_start in range(len(self.s) - len(self.p) + 1):
            count_mismatches = 0
            for j in range(win_start, win_start + len(self.p)):
                if self.s[j] != self.p[j - win_start]:
                    count_mismatches += 1
                    if count_mismatches > self.k:
                        break
            if count_mismatches <= self.k:
                indices.append(win_start)
        return [len(indices)] + indices


def debug_solution(out_file):
    import os
    if os.path.exists(out_file):
        if os.path.getsize(out_file) > 0:
            open(out_file, 'w').close()

    rqs = get_requests()
    for n, r in enumerate(rqs):
        pmm = PMM(r)
        pmm.handle_request_debug()


if __name__ == '__main__':
    while True:
        # k = random.randint(0, 5)
        # text_len = random.randint(1, 20000)
        # patt_len = random.randint(1, min(text_len, 1000))
        k = 1
        text_len = 5
        patt_len = 2
        s = rand_str(text_len)
        p = rand_str(patt_len)

        # ########## PREDEFINED Test Case ##########
        # k = 2
        # s = 'baccbbcbcccb'
        # p = 'ccbb'
        # ##########################################
        r = Request(k, s, p)
        pmm = PMM(r)
        naive_result = pmm.naive_handle_request()
        pmm.handle_request()
        hashing_result = pmm.result
        if naive_result != hashing_result:
            print(f'Wrong answer!:')
            print(f'\tk = {pmm.k}; s = {pmm.s}; p = {pmm.p}')
            print(f'\tnaive_result = {naive_result}; hashing_result = {hashing_result}')
            break
        else:
            print('OK.')


    # for text_len, r in enumerate(requests):
    #     pmm = PMM(r)
    #     pmm.handle_request()
    # print(f'random string of length {n}: {rand_str(n)}')
