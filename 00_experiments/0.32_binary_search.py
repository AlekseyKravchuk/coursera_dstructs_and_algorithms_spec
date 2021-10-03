from bisect import bisect_left
from bisect import bisect_right


def bin_search_recursive(arr, left, right, key2search):
    # BASE CASE
    if left > right:
        return -1

    mid = left + (right - left) // 2
    if key2search == arr[mid]:
        return mid
    elif key2search < arr[mid]:
        return bin_search_recursive(arr, left, mid-1, key2search)
    elif key2search > arr[mid]:
        return bin_search_recursive(arr, mid+1, right, key2search)


def bin_search(arr, key):
    l, h = 0, len(arr) - 1

    while l <= h:
        mid = l + (h - l) // 2
        if key == arr[mid]:
            return mid
        elif key < arr[mid]:
            h = mid - 1
        else:  # key > a[mid]
            l = mid + 1

    # if we reach this point then the key was not found in array a
    return -1


def bin_search_bisect(arr, key, l=0, h=None):
    print(f'array: {arr}')
    print(f'key to search: {key}')
    if h is None:
        h = len(arr)
    pos = bisect_left(arr, key, l, h)
    return pos if pos != h and arr[pos] == key else -1


if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40, 50, 60]
    key = 40
    my_res = bin_search(arr, key)
    my_res_recursive = bin_search_recursive(arr, 0, len(arr) - 1, key)
    res_by_bisect = bin_search_bisect(arr, key)
    print(f'output by bisect: {res_by_bisect}')
    print(f'output by binsearch: {my_res}')
    print(f'output by binsearch RECURSIVE: {my_res_recursive}')
