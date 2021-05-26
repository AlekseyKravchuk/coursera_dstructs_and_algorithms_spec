import numpy as np
import sys

x = 263
p = 1000000007
m = 43
n = 26


def get_hash(s):
    res = 0
    for i, ch in enumerate(s):
        res += ord(ch) * x ** i
    print(f'sum_result = {res}')
    return (res % p) % m

# ##################### !!!!!!!! INTEGER OVERFLOW !!!!!!!!!! #####################
# using numpy even with np.ulonglong type leads to integer overflow, so this function will give wrong hashes
def get_hash_using_numpy(s):
    n = len(s)
    ords = [ord(ch) for ch in reversed(s)]
    powers_of_x = np.power([x] * n, np.arange(n, dtype=np.longlong), dtype=np.longlong)
    sum_result = np.sum(ords * powers_of_x)
    temp_res = sum_result % p
    res = temp_res % m
    return res


if __name__ == '__main__':
    in_file_name = 'strings_to_be_hashed.txt'
    with open(in_file_name, 'r') as in_file:
        for s in in_file:
            s = s.strip()
            hash = get_hash(s)
            hash_using_numpy = get_hash_using_numpy(s)
            if hash != hash_using_numpy:
                print(f'Failure: my_hash({s}) = {hash}  hash_using_numpy = {hash_using_numpy}')



