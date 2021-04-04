# Problem statement
# Given a set of positive numbers, find if we can partition it into two subsets
# such that the sum of elements in both the subsets is equal.

# test inputs
"""
1 2 3 4
output: True

1 5 11 5
output: True

1 2 3 5
output: False
"""


def restore_DP_solution(db_table, nums):
    set1 = []
    set2 = []
    i, s = len(dp_table)-1, len(dp_table[0])-1
    while i != 0:
        # include number nums[i], i.e. include it to set1
        curr_num = nums[i-1]
        if s - curr_num >= 0:
            if db_table[i-1][s-curr_num]:
                set1.append(curr_num)
                i, s = i-1, s-curr_num
                continue
        # exclude number nums[i], in other words include it to another set (set2)
        if db_table[i-1][s]:
            set2.append(curr_num)
            i -= 1
    return set1, set2


def can_partition_in_2_subsets(nums):
    S = sum(nums)
    if S % 2 != 0:
        return [[False]]

    n = len(nums)
    # F[i, s] is bool value identifying if we can compose s (0<=s<=S/2) by using OR not using first i numbers
    F = [[False for s in range(S // 2 + 1)] for i in range(n + 1)]

    # populate the sum=0 column, as we can always have '0' sum without including any element
    for i in range(n+1):
        F[i][0] = True

    # having possible to use no elemements we can compose just sum = 0
    # this loop can be omitted as we already initialize DP table with False values
    for s in range(1, S // 2 + 1):
        F[0][s] = False

    # populate DP table
    for i, num in enumerate(nums, start=1):
        for s in range(1, S // 2 + 1):
            if s - num >= 0:
                F[i][s] = F[i - 1][s] or F[i - 1][s - num]
            else:
                F[i][s] = F[i - 1][s]

    return F


if __name__ == '__main__':
    nums = [int(x) for x in input().split()]

    dp_table = can_partition_in_2_subsets(nums)
    if dp_table[-1][-1]:
        set1, set2 = restore_DP_solution(dp_table, nums)
        print(f'Given numbers = {nums} can be splited into 2 set with equal nums:')
        print(f'set1 = {set1}')
        print(f'set2 = {set2}')
    else:
        print(f'Given numbers = {nums} CAN NOT be splited into 2 set with equal nums')
