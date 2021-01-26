import random


# def partition_2parts(a, l, r):
#     j = l  # j is the last index of the left subarray, containing elements that are at most pivot element
#     pivot = a[l]
#     for i in range(l + 1, r + 1):
#         if a[i] <= pivot:
#             j += 1
#             a[j], a[i] = a[i], a[j]
#     a[j], a[l] = a[l], a[j]
#     return j


def partition_3parts(a, l, r):
    pivot = a[r]
    m1 = m2 = l
    for i in range(l, r):
        if a[i] < pivot:
            a[m2], a[i] = a[i], a[m2]
            a[m1], a[m2] = a[m2], a[m1]
            m1 += 1
            m2 += 1
        elif a[i] == pivot:
            a[i], a[m2] = a[m2], a[i]
            m2 += 1
    a[r], a[m2] = a[m2], a[r]
    return m1, m2


def partition_2parts(a, l, r):
    pivot = a[r]
    wall = l
    for i in range(l, r):
        if a[i] <= pivot:
            a[wall], a[i] = a[i], a[wall]
            wall += 1
    a[r], a[wall] = a[wall], a[r]
    return wall


def randomized_quick_sort_2parts(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[r], a[k] = a[k], a[r]
    m = partition_2parts(a, l, r)
    randomized_quick_sort_2parts(a, l, m - 1)
    randomized_quick_sort_2parts(a, m + 1, r)


def randomized_quick_sort_3parts(a, l, r):
    if l >= r:
        return
    # k = random.randint(l, r)
    k = r
    a[r], a[k] = a[k], a[r]
    m1, m2 = partition_3parts(a, l, r)
    randomized_quick_sort_3parts(a, l, m1 - 1)
    randomized_quick_sort_3parts(a, m2 + 1, r)


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    # randomized_quick_sort_2parts(a, 0, len(a)-1)
    randomized_quick_sort_3parts(a, 0, len(a)-1)
    for i in a:
        print(i, end=' ')

    # while True:
    #     a = [random.randint(1, 100) for _ in range(30)]
    #     a1 = a.copy()
    #     a2 = a.copy()
    #     # randomized_quick_sort_2parts(a1, 0, len(a) - 1)
    #     randomized_quick_sort_3parts(a1, 0, len(a) - 1)
    #     a2.sort()
    #     if a1 == a2:
    #         print(f'OK, sorted array: {a1}')
    #     else:
    #         print('FAILURE')
    #         print(f'a1 = {a1}')
    #         print(f'a2 = {a2}')
    #         print(f'initial array: {a}')
    #         break
