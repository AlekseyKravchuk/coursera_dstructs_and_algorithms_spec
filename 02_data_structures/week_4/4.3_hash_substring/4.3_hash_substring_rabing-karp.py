def check(s, p, pos2start):  # s - string, p - pattern to search
    for i in range(len(p)):
        if s[pos2start + i] != p[i]:
            return False
    return True


def find_substring_brute_force(s, p):  # s - string, p - pattern to search
    positions = []

    for pos in range(len(s) - len(p) + 1):
        if check(s, p, pos):
            positions.append(pos)

    return positions


if __name__ == '__main__':
    p = input().strip()
    s = input().strip()

    res = find_substring_brute_force(s, p)
    print(*res)
