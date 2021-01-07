import timeit
import random


def maxPairWiseProduct_Naive(n, nums):
    assert len(nums) == n
    res = 0

    for i in range(0, n):
        for j in range(i + 1, n):
            # print(f'({i},{j})', end=' ')
            if nums[i] * nums[j] > res:
                res = nums[i] * nums[j]
        # print()
    return res


def maxPairWiseProduct_Fast(n, nums):
    assert len(nums) == n
    first_max, second_max = sorted(nums)[-2:]
    return first_max * second_max


# n = 20
# nums = [random.randint(1, 100) for _ in range(n)]
# print(f'nums = {nums}')
# print(f'maximum pairwise product = {maxPairWiseProduct_Naive(n, nums)}')

# ################### Checking the performance ###########################
# print(f'time(maxPairWiseProduct_Naive) = {timeit.timeit(lambda: maxPairWiseProduct_Naive(n, nums), number=1000000):.3}')
# print(f'time(maxPairWiseProduct_Fast) = {timeit.timeit(lambda: maxPairWiseProduct_Fast(n, nums), number=1000000):.3}')

# ################### Stress testing ########################
while True:
    n = random.randint(2, 20)
    print(f'n = {n}')
    nums = [random.randint(1, 100) for _ in range(n)]
    print(f'nums = {nums}')

    res_Naive = maxPairWiseProduct_Naive(n, nums)
    res_Fast = maxPairWiseProduct_Fast(n, nums)
    if res_Naive != res_Fast:
        print(f'Wrong answer: res_Naive = {res_Naive}, res_Fast = {res_Fast}')

# n = int(input())
# nums = [int(x) for x in input().split()]
# n = 6
# nums = [2, 4, 1, 5, 7, 4]

# n = 10
# nums = [random.randint(1, 100) for _ in range(n)]
# print(f'nums = {nums}')
# print(f'maximum pairwise product = {maxPairWiseProduct_Naive(n, nums)}')
#
# t_Naive = timeit.Timer(lambda: maxPairWiseProduct_Naive(n, nums))
# print(f'time for maxPairWiseProduct_Naive = {t_Naive.timeit(number=1000000):.2}')
