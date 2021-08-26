from bisect import bisect_left


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


def bin_search_bisect(a, key, l=0, h=None):
    if h is None:
        h = len(a)
    pos = bisect_left(a, key, l, h)
    return pos if pos != h and a[pos] == key else -1


if __name__ == '__main__':
    a = [2, 3, 4, 10, 40]
    key = 40
    res = bin_search(a, key)
    print(f'element was found at index {res}.' if res != -1 else f'element key = {key} isn\'t present in array {a}')
    res_by_bisect = bin_search_bisect(a, key)
    print(f'by bisect: {res_by_bisect}')
