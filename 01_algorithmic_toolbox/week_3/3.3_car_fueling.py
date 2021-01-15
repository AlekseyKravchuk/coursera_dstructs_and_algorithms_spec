def min_refills(x, max_dist_without_refill):
    idx = len(x) - 2  # index of the last possible refill station point
    curr = 0  # current index of refill station in array 'x'
    refills_count = 0

    while curr <= idx:
        last = curr
        while curr <= idx and x[curr + 1] - x[last] <= max_dist_without_refill:
            curr += 1
        if curr == last:
            return -1
        if curr > idx:
            return refills_count
        refills_count += 1
    return refills_count


def main():
    endpoint = [int(input())]
    max_dist_without_refill = int(input())
    n = int(input())
    x = [0] + [k for k in map(int, input().split())] + endpoint
    assert n == (len(x) - 2)

    print(min_refills(x, max_dist_without_refill))


if __name__ == '__main__':
    main()
