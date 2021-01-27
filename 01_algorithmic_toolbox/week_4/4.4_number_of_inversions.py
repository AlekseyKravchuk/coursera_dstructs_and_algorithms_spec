import random


def merge(b, c, inv_cnt=0):
    d = []
    i = j = 0

    while i < len(b) and j < len(c):
        if b[i] <= c[j]:
            d.append(b[i])
            i += 1
        else:
            d.append(c[j])
            j += 1
            inv_cnt += len(b) - i
    if i == len(b):
        d.extend(c[j:])
    else:
        d.extend(b[i:])
    return d, inv_cnt


def count_inversions_merge_sort(a, inv_cnt=0):
    if len(a) == 1:
        return a, inv_cnt
    m = len(a) // 2

    b, inv_cnt = count_inversions_merge_sort(a[:m], inv_cnt)
    c, inv_cnt = count_inversions_merge_sort(a[m:], inv_cnt)

    return merge(b, c, inv_cnt)


def count_inversions_brute_force(a):
    cnt = 0
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] > a[j]:
                cnt += 1
    return cnt


if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))
    _, num_of_inversions = count_inversions_merge_sort(nums.copy())
    print(num_of_inversions)

    # ############### Stress Testing ###############
    # while True:
    #     a = [random.randint(1, 20) for _ in range(8)]
    #     num_of_inversions1 = count_inversions_brute_force(a.copy())
    #     _, num_of_inversions2 = count_inversions_merge_sort(a.copy())
    #     if num_of_inversions1 != num_of_inversions2:
    #         print('FAILURE')
    #         print(f'The number of inversions counted by BRUTE FORCE is: {num_of_inversions1}')
    #         print(f'The number of inversions counted by MERGE is: {num_of_inversions2}')
    #         break
    #     else:
    #         print('OK')
