from collections import deque
from math import floor


def bin_search_for_single_key(nums, low, high, key):

    while low <= high:
        mid = floor(low + (high - low) / 2.0)
        if key == nums[mid]:
            return mid
        elif key < nums[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1


def bin_search_for_list_of_keys(nums, unsorted_keys):
    low = 0
    high = len(nums) - 1
    d = dict()

    sorted_keys = sorted(unsorted_keys)

    for key in sorted_keys:
        if key not in d:
            if key > nums[-1]:
                d[key] = -1
            else:
                idx = bin_search_for_single_key(nums, low, high, key)
                d[key] = idx
                if high > idx >= 0:
                    low = idx + 1

    for key in unsorted_keys:
        print(d[key], end=' ')


def main():
    n, *nums = map(int, input().split())
    k, *keys = map(int, input().split())
    assert n == len(nums)
    assert k == len(keys)

    bin_search_for_list_of_keys(nums, keys)


if __name__ == '__main__':
    main()
