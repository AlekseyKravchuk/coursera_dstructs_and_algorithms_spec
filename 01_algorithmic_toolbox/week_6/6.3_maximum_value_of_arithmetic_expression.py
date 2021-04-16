from math import inf

op = {'+': lambda x, y: x + y,
      '-': lambda x, y: x - y,
      '*': lambda x, y: x * y}


def minAndMax(tbl_min, tbl_max, ops, i, j):
    _min = inf
    _max = -inf
    for k in range(i, j):
        a = op[ops[k]](tbl_max[i][k], tbl_max[k + 1][j])
        b = op[ops[k]](tbl_max[i][k], tbl_min[k + 1][j])
        c = op[ops[k]](tbl_min[i][k], tbl_max[k + 1][j])
        d = op[ops[k]](tbl_min[i][k], tbl_min[k + 1][j])
        _min = min(_min, a, b, c, d)
        _max = max(_max, a, b, c, d)

    return _min, _max


def parenthesize_DP_Bottom_Up(s: str) -> int:
    nums = [int(ch) for i, ch in enumerate(s) if i % 2 == 0]
    ops = [ch for i, ch in enumerate(s) if i % 2]
    n = len(nums)  # n - the number of operands (integers)

    M = [[-inf if i != j else nums[i] for j in range(n)] for i in range(n)]  # DP table for storing MAX values
    m = [[inf if i != j else nums[i] for j in range(n)] for i in range(n)]   # # DP table for storing MIN values

    # L - the number of operands involved in expression, L = 2, 3, ..., n; L=1 corresponds to main diagonal in DP tables
    for L in range(2, n + 1):
        for i in range(n - L + 1):
            j = i + L - 1
            m[i][j], M[i][j] = minAndMax(m, M, ops, i, j)
    return M[0][n - 1]


if __name__ == '__main__':
    s = input()
    ans = parenthesize_DP_Bottom_Up(s)
    print(ans)
