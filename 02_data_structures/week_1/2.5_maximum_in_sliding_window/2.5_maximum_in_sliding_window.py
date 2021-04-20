from collections import deque


def sliding_window(nums, k):
    n = len(nums)
    q = deque()
    res = []  # stores indices of maximum value in each of n-k+1 windows

    def append_item_to_queue(idx):
        if not q:
            q.append(idx)
        else:
            while q and nums[q[-1]] < nums[idx]:
                q.pop()
            q.append(idx)

    def handle_window(start, end):  # start, end - indices specifying current window
        if res and start > res[-1]:
            q.popleft()

        if end < k:  # this means that we handle first window, so we need to initialize it
            for idx in range(k):
                append_item_to_queue(idx)
        else:  # handling of subsequent windows, one window per handle_window(start, end) invocation
            append_item_to_queue(end)

        res.append(q[0])

    # (n-k+1) is the total number of windows
    for i in range(n-k+1):  # i: start index of current window
        j = i+k-1           # j: end index of current window
        handle_window(i, j)

    return res


if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))
    assert n == len(nums)
    k = int(input())

    indices = sliding_window(nums, k)
    for i in indices:
        print(nums[i], end=' ')
    print()
