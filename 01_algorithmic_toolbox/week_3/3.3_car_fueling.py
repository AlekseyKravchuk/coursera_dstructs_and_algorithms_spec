def minRefills(x, max_dist_without_refill):
    curr_idx = 0
    num_refills = 0
    second_last_idx = len(x) - 2

    while curr_idx <= second_last_idx:
        last_refill_idx = curr_idx
        while curr_idx <= second_last_idx and (x[curr_idx + 1] - x[last_refill_idx]) <= max_dist_without_refill:
            curr_idx += 1
        if last_refill_idx == curr_idx:
            return -1
        if curr_idx <= second_last_idx:
            num_refills += 1
    return num_refills


def main():
    d = [int(input())]
    max_dist_without_refill = int(input())
    n = int(input())
    x = [0] + [k for k in map(int, input().split())] + d
    assert (len(x) - 2) == n

    print(minRefills(x, max_dist_without_refill))


if __name__ == '__main__':
    main()
